import numpy as np

from eraser import Eraser
from games import SecurityGame
from origami_milp import OrigamiMILP

import texttable as tt

"""
Solution for problem described in http://www-bcf.usc.edu/~halfond/papers/kukreja13ase.pdf

More about algorithms used:
http://teamcore.usc.edu/kiekintveld/papers/2009/kjtpot-massive-security-games.pdf
http://www.cs.utep.edu/kiekintveld/papers/2011/atosk-refinement.pdf
"""

developer_payoffs = np.array([
    # Uncovered
    [[4.0], [3.0], [5.0], [7.0], [3.0]],
    # Covered
    [[-7.0], [-1.0], [-6.0], [-3.0], [-10.0]]
])

tester_payoffs = np.array([
    # Uncovered
    [[-10.0], [-4.0], [-1.0], [-9.0], [-9.0]],
    # Covered
    [[2.0], [7.0], [6.0], [9.0], [9.0]]
])

testing_game = SecurityGame(
    num_targets=5,
    max_coverage=1,
    num_attacker_types=1,
    attacker_payoffs=developer_payoffs,
    defender_payoffs=tester_payoffs
)

def _solve_game_using_ori_MILP():
    oriMILP = OrigamiMILP(testing_game)
    oriMILP.solve()
    return oriMILP

def _solve_game_using_eraser():
    eraser = Eraser(testing_game)
    eraser.solve()
    return eraser

def _print_results(solution):
    tab = tt.Texttable()
    headings = ['Feature', 'Optimal Coverage', 'Tester\'s payoff']

    coverage_array = solution.opt_coverage
    feature_ids = range(len(coverage_array))

    expected_payoffs = []
    tester_payoffs_uncovered = [p[0] for p in tester_payoffs[0]]
    tester_payoffs_covered = [p[0] for p in tester_payoffs[1]]
    for payload in list(zip(coverage_array, tester_payoffs_uncovered, tester_payoffs_covered)):
        expected_payoff = payload[0] * payload[2] + (1 - payload[0]) * payload[1]
        expected_payoffs.append(expected_payoff)
    tab.header(headings)

    for row in zip(feature_ids, coverage_array, expected_payoffs):
        tab.add_row(row)
    s = tab.draw()
    print(s)

if __name__ == '__main__':
    origami_solution = _solve_game_using_ori_MILP()
    eraser_solution = _solve_game_using_eraser()
    print('### ORIGAMI MILP ###')
    _print_results(origami_solution)
    print('\n')
    print('### ERASER ###')
    _print_results(eraser_solution)