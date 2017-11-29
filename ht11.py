import learning
import random
import struct


def load_mnist_images(fn):
    img_list = []
    with open(fn, "rb") as f:
        f.read(16)
        chunk_size = 28 * 28
        chunk = f.read(chunk_size)
        while chunk:
            img_list.append([px / 256 for px in list(chunk)])
            # print(list(chunk))
            chunk = f.read(chunk_size)
    return img_list


def load_mnist_labels(fn):
    label_list = []
    with open(fn, "rb") as f:
        f.read(8)
        chunk_size = 28 * 28
        chunk = f.read(chunk_size)
        while chunk:
            label_list.append(list(chunk)[0])
            # print(list(chunk))
            chunk = f.read(chunk_size)
    return label_list


imgs = load_mnist_images("/Users/mikksillaste/Downloads/aima-python/aima-data/MNIST/train-images-idx3-ubyte")
labels = load_mnist_labels("/Users/mikksillaste/Downloads/aima-python/aima-data/MNIST/train-labels-idx1-ubyte")

print(len(imgs))

train_data = []
for i in range(len(imgs)):
    train_data.append(imgs[i] + [labels[i]])
train_ds = learning.DataSet(random.sample(train_data, 100))

print("trainging...")
nn = learning.NeuralNetLearner(train_ds, hidden_layer_sizes=[20], epochs=20)
print("narvivork", nn(imgs[0]), "tegelikult", labels[0])

test_imgs = load_mnist_images("/Users/mikksillaste/Downloads/aima-python/aima-data/MNIST/t10k-images-idx3-ubyte")
test_labels = load_mnist_labels("/Users/mikksillaste/Downloads/aima-python/aima-data/MNIST/t10k-labels-idx1-ubyte")

test_data = []
for i in range(len(test_imgs)):
    test_data.append(test_imgs[i] + [test_labels[i]])
test_ds = learning.DataSet(random.sample(test_data, 100))

print(learning.err_ratio(nn, test_ds))


def load_bmp(fn):
    with open(fn, "rb") as f:
        header = f.read(54)
        offset = header[10:14]
        offs = struct.unpack("@L", offset)
        f.read(offs - 54)
        data = list(f.read(28 * 28))
        inv_data = []
        for i in range(27, -1, -1):
            inv_data += data[i * 28: (i + 1) * 28]
        return inv_data


bitmap = load_bmp("yks.bmp")

print("narvivork", nn(bitmap), "tegelikult", 1)
