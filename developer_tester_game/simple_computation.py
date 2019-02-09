import texttable as tt
tab = tt.Texttable()

# Each tuple in array represents payoffs for given feature
tester_payoffs = [
    (2, -10),
    (7, -4)
]
developer_payoffs = [
    (7, -4),
    (-1, 3)
]

weights_array = [
    [0, 1],
    [0.1, 0.9],
    [0.3, 0.7],
    [0.5, 0.5],
    [0.7, 0.3],
    [0.9, 0.1],
    [1, 0]
]


def _compute_payoff(payoff_matrix, weights):
    payoff = 0
    for p, w in zip(payoff_matrix, weights):
        partial_payoff = p[0] * w + p[1] * (1 - w)
        payoff += partial_payoff
    return payoff


if __name__ == '__main__':
    for w in weights_array:
        tester_payoff = _compute_payoff(tester_payoffs, w)
        developer_payoff = _compute_payoff(developer_payoffs, w)
        tab.add_row([w[0],w[1],tester_payoff,developer_payoff])
    s = tab.draw()
    print(s)