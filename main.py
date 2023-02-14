import secrets
import sys
import time
import math
import numpy as np


def run(n):
    """
    n: number of different coupons (stamps)
    return: days it took to achieve such goal
    """

    days = 0
    collected = set()
    while len(collected) < n:
        stamp_id = secrets.choice(range(0, n))
        days += 1
        collected.add(stamp_id)

    return days


if __name__ == '__main__':
    lowest_days_to_collect_all = sys.maxsize
    highest_days_to_collect_all = -sys.maxsize - 1

    totaldays = 0

    simulation_runs = 1_000_000

    unique_coupons = 295

    expected_days = \
        1 + unique_coupons * sum([1 / i for i in range(1, unique_coupons)])

    start_time = time.time()
    for i in range(1, simulation_runs):
        days = run(unique_coupons)
        totaldays += days
        if i % 1000 == 0:
            avg_so_far = totaldays / i
            delta_ev = abs(expected_days - avg_so_far)
            print(
                str(i).rjust(1 + int(math.log(simulation_runs + 1, 10))),
                "{:.22f}".format(avg_so_far),
                "{:.22f}".format(delta_ev)
            )

        if days < lowest_days_to_collect_all:
            lowest_days_to_collect_all = days
        
        if days > highest_days_to_collect_all:
            highest_days_to_collect_all = days

    print("\ntime", time.time() - start_time)
    print(simulation_runs, totaldays / simulation_runs)
    print("lowest_days_to_collect_all", lowest_days_to_collect_all)
    print("highest_days_to_collect_all", highest_days_to_collect_all)
    print("expected_days", expected_days)
