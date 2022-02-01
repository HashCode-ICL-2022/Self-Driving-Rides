def score(rides, B):

    score = 0
    for ride in rides:
        if ride.finished:
            score += ride.distance
            if ride.on_time:
                score += B

    return score


def ride_can_finish(T, ride):
    return T <= ride.latest_time


if __name__ == "__main__":
    pass