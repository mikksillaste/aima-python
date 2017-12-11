import rl
import mdp
from collections import defaultdict
from utils import print_table


def heatmap(ap):
    hm = defaultdict(int)
    for k, v in ap.Nsa.items():
        s, a = k
        hm[s] += v
    return hm


def policy(ap):
    best_move = defaultdict(lambda: (0, 1))
    best_score = defaultdict(lambda: -1000)
    for k, v in ap.Q.items():
        s, a = k
        if v > best_score[s]:
            best_move[s] = a
            best_score[s] = v
    return best_move


env = mdp.sequential_decision_environment
ap = rl.QLearningAgent(env, 10, 1, alpha=lambda n: 60./(59+n))  # 10 - exploration trials, 1 - exploration reward
# jooksutab koodi mitu korda
for _ in range(10):
    rl.run_single_trial(ap, env)
print_table(env.to_grid(heatmap(ap)))
print_table(env.to_arrows(policy(ap)))


class SARSAAgent(rl.QLearningAgent):
    def __call__(self, percept):
        