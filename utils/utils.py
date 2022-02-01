def score(rides, B):
    score = 0
    for ride in rides:
        if ride.finished:
            score += ride.distance
            if ride.on_time:
                score += B

    return score


def can_finish(T, ride):
    return T <= ride.latest_time


def distance_to_ride(location, ride):
    x, y = location
    ride_x, ride_y = ride.start
    return abs(x - ride_x) + (y - ride_y)


def nearest_ride(car, rides, T):
    closest_ride = None
    closest_dist = float("inf")
    for ride in rides:
        if car.can_finish(ride, T):
            dist = distance_to_ride(car.location, ride)
            if dist < closest_dist:
                closest_ride = ride
                closest_dist = dist
    return closest_ride


def ride_sort(rides):
    """ Sort lowest to highest: ride.latest_finish + ride.end[0] + ride.end[1]
    """
    rides.sort(reverse=True|False, key=myFunc)



if __name__ == "__main__":
    pass
