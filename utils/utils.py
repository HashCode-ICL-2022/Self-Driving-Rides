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


def distance_to_ride(location, ride):
    x, y = location
    ride_x, ride_y = ride.start
    return abs(x - ride_x) + (y - ride_y)


def nearest_ride(car, rides):
    closest_ride = None
    closest_dist = float("inf")
    for ride in rides:
        dist = distance_to_ride(car.location, ride)
        if dist < closest_dist:
            closest_ride = ride
            closest_dist = dist
    return closest_ride



if __name__ == "__main__":
    pass