from ast import arg
from utils.utils import score
from utils.parse import import_data

from tqdm import tqdm

import argparse

def main(fname):

    R, C, F, N, B, T, rides, cars = import_data(fname)

    t = 0
    total_score = 0
    count = 0

    for t in tqdm(range(T)):
        for car in cars:
            count += 1
            finished, ride = car.check_ride_finished(t)
            if car.is_free:
                if finished and ride.finished_on_time:
                    total_score += score([ride], B)
                if len(rides) > 0:
                    car.add_ride(rides.pop(), t)

    print(f"{total_score:,}")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--fname', '-f', default='b')
    args = parser.parse_args()
    fname_dict = {
        "a" : "a_example.in",
        "b" : "b_should_be_easy.in",
        "c" : "c_no_hurry.in",
        "d" : "d_metropolis.in",
        "e" : "e_high_bonus.in",
    }
    main(fname_dict[args.fname])



