from collections import defaultdict

train_data = [['Yes', 'No', 'No', 'Yes', 'Some', '$$$', 'No', 'Yes', 'French', '0-10', 'Yes'],
              ['Yes', 'No', 'No', 'Yes', 'Full', '$', 'No', 'No', 'Thai', '30-60', 'No'],
              ['No', 'Yes', 'No', 'No', 'Some', '$', 'No', 'No', 'Burger', '0-10', 'Yes'],
              ['Yes', 'No', 'Yes', 'Yes', 'Full', '$', 'No', 'No', 'Thai', '10-30', 'Yes'],
              ['Yes', 'No', 'Yes', 'No', 'Full', '$$$', 'No', 'Yes', 'French', '>60', 'No'],
              ['No', 'Yes', 'No', 'Yes', 'Some', '$$', 'Yes', 'Yes', 'Italian', '0-10', 'Yes'],
              ['No', 'Yes', 'No', 'No', 'None', '$', 'Yes', 'No', 'Burger', '0-10', 'No'],
              ['No', 'No', 'No', 'Yes', 'Some', '$$', 'Yes', 'Yes', 'Thai', '0-10', 'Yes'],
              ['No', 'Yes', 'Yes', 'No', 'Full', '$', 'Yes', 'No', 'Burger', '>60', 'No'],
              ['Yes', 'Yes', 'Yes', 'Yes', 'Full', '$$$', 'No', 'Yes', 'Italian', '10-30', 'No'],
              ['No', 'No', 'No', 'No', 'None', '$', 'No', 'No', 'Thai', '0-10', 'No'],
              ['Yes', 'Yes', 'Yes', 'Yes', 'Full', '$', 'No', 'No', 'Burger', '30-60', 'Yes']
              ]

n = len(train_data)
classif_dist = defaultdict(int)
attrib_dist = []

for row in train_data:
    classif_dist[row[10]] += 1

# Fill classif_dist or count of negative positives
for i in range(10):
    one_attrib_dist = {"Yes": defaultdict(int), "No": defaultdict(int)}
    for row in train_data:
        one_attrib_dist[row[10]][row[i]] += 1
    attrib_dist.append(one_attrib_dist)

print(classif_dist)
print(attrib_dist)
#print(classif_dist["Yes"])
#print(attrib_dist[3]["No"]["No"])


def classif_probability(attr, hyp):
    n_hyp = classif_dist[hyp]
    p = n_hyp / n
    for i in range(10):
        p *= (attrib_dist[i][hyp][attr[i]] + 1 / n_hyp)

    return p  # on number


print("hyp: Yes", classif_probability(['Yes', 'No', 'No', 'Yes', 'Some', '$$$', 'No', 'Yes', 'French', '0-10'], "Yes"))
print("hyp: No", classif_probability(['Yes', 'No', 'No', 'Yes', 'Some', '$$$', 'No', 'Yes', 'French', '0-10'], "No"))