from import_data import import_data
from utils.utils import score

def main(fname):

    R, C, F, N, B, T, rides, cars = import_data(fname)

    t = 0
    total_score = 0
    while t < T:
        for car in cars:
            finished, ride = car.check_ride_finished(t)
            if car.is_free:
                if finished:
                    total_score += score([ride], B)
                if len(rides) > 0:
                    car.add_ride(rides.pop())
        t += 1

    print(total_score)


if __name__ == "__main__":
    main("data/b_should_be_easy.in")



