import numpy as np

from games import SecurityGame
from origami_milp import OrigamiMILP

attacker_uncovered = np.array([[4.0], [3.0], [5.0], [7.0], [3.0]])
attacker_covered = np.array([[-7.0], [-1.0], [-6.0], [-3], [-10]])
defender_uncovered = np.array([[-10.0], [-4.0], [-1.0], [-9.0], [-9.0]])
defender_covered = np.array([[2.0], [7.0], [6.0], [9.0], [9.0]])

attacker_payoffs = np.array([
    [[4.0], [3.0], [5.0], [7.0], [3.0]],
    [[-7.0], [-1.0], [-6.0], [-3.0], [-10.0]]
])

defender_payoffs = np.array([
    [[-10.0], [-4.0], [-1.0], [-9.0], [-9.0]],
    [[2.0], [7.0], [6.0], [9.0], [9.0]]
])

testing_game = SecurityGame(
    num_targets=5,
    max_coverage=1,
    num_attacker_types=1,
    attacker_payoffs=attacker_payoffs,
    defender_payoffs=defender_payoffs
)

oriMILP = OrigamiMILP(testing_game)
oriMILP.solve()

print("ORI_MILP cov: {}".format(oriMILP.opt_coverage))