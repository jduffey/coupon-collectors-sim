import secrets
import sys
import time
import math

'''
Spin a roulette wheel until all numbers have been hit.
An implementation of the Coupon Collector's Problem.
'''


def play_until_all_numbers_hit(n):
    spins = 0
    collected = set()
    while len(collected) < n:
        stamp_id = secrets.choice(range(0, n))
        spins += 1
        collected.add(stamp_id)

    return spins


if __name__ == '__main__':
    fewest_runs_to_collect_all = sys.maxsize
    most_runs_to_collect_all = -sys.maxsize - 1

    total_runs = 0

    games_to_play = 10_000

    unique_elements = 38

    expected_runs = \
        1 + unique_elements * sum([1 / i for i in range(1, unique_elements)])

    start_time = time.time()
    for i in range(1, games_to_play):
        internal_runs = play_until_all_numbers_hit(unique_elements)
        total_runs += internal_runs
        if i % 1000 == 0:
            avg_so_far = total_runs / i
            delta_ev = abs(expected_runs - avg_so_far)
            print(
                str(i).rjust(1 + int(math.log(games_to_play + 1, 10))),
                "",
                "{:.22f}".format(avg_so_far),
                "{:.22f}".format(delta_ev).rjust(26),
                f'({fewest_runs_to_collect_all}, {most_runs_to_collect_all})',
                total_runs
            )

        if internal_runs < fewest_runs_to_collect_all:
            fewest_runs_to_collect_all = internal_runs
        
        if internal_runs > most_runs_to_collect_all:
            most_runs_to_collect_all = internal_runs

    print("\ntime", time.time() - start_time)
    print("     Games played:", games_to_play)
    print("       Total runs:", total_runs)
    print("  Avg (mean) runs:", total_runs / games_to_play)
    print("EV spins per game:", expected_runs, f'({unique_elements} unique elements)')
    print("To collect all")
    print("  -fewest runs:   ", fewest_runs_to_collect_all)
    print("  -most runs:     ", most_runs_to_collect_all)

    bet_amount_per_spin = 1
    print("  Total $ wagered:", total_runs * bet_amount_per_spin)

    house_edge = 0.0526
    print("       House edge:", house_edge * 100, "%")
    house_profit = total_runs * bet_amount_per_spin * house_edge
    print("     House profit:", house_profit)

    retroactive_rewards_per_game = house_profit / games_to_play
    print("Retroactive rewards per game:", retroactive_rewards_per_game)
