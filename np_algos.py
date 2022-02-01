import numpy as np
from tqdm import tqdm


def read(fname):
    with open(fname, 'r') as file:
        meta = file.readline().rstrip()
        [R, C, F, N, B, T] = [int(i) for i in meta.split(' ')]
        rides = []
        for i in range(N):
            tmp = file.readline().rstrip()
            rides += [[int(i) for i in tmp.split(' ')]]
    print(fname)
    print(
        f"Rows: {R}, Cols: {C}, Vehicles: {F}, Rides: {N}, Bonus: {B}, Timesteps: {T}"
    )

    rides = np.array(rides)
    return [R, C, F, N, B, T], rides


def get_dist_array(X, Y):
    return np.sum(np.abs(X - Y), axis=1)


def build_close_map(fname, rides=None, N=None):
    # Ride: a, b, x, y, s, f
    if fname:
        [R, C, F, N, B, T], rides = read(fname)

    # Selectors for the start and end coordinates
    si = [0, 1]
    ei = [2, 3]
    dists = get_dist_array(rides[:, si], rides[:, ei])

    # For each ride (index), find closest N start points and store in closemap
    closemap = {i: [] for i in range(N)}

    # Closest rides from the start node
    dist_to_start = get_dist_array(rides[:, si], np.array([0, 0]))
    # Gives ride ids of closest rides to start node
    closest = np.argsort(dist_to_start)

    # Stores ride ids of sorted rides (from start point) in key [-1]
    closemap[-1] = closest
    

    # Stores ride ids of sorted rides from ride (id i) in key[i]
    pbar = tqdm(enumerate(rides))
    pbar.set_description("Building Closemap")
    for i, ride in pbar:

        dist_to_ends = get_dist_array(rides[:, si], ride[ei])
        closest = np.argsort(dist_to_ends)
        closemap[i] = closest

    return closemap


def dist(a, b):
    return np.sum(np.abs(a - b))


def car_by_car(fname, verbose=True):
    # Selectors for the start and end coordinates
    si = [0, 1]
    ei = [2, 3]

    # Run simulation car by car
    [R, C, F, N, B, T], rides = read(fname)

    # Calc ride lengths
    ride_lengths = get_dist_array(rides[:, si], rides[:, ei])

    # Get closemap
    closemap = build_close_map(False, rides=rides, N=N)

    # Init array storing done rides
    done_rides = np.full(len(rides), False)
    intmap = np.arange(len(rides))

    # track (useful dist, between dist) for each car
    car_stats = np.zeros((F, 2))

    # Run each car
    if verbose:
        crange = range(F)
    else:
        crange = tqdm(range(F))

    total_score = 0

    for car_id in crange:
        if not verbose:
            crange.set_description(f"Car {car_id}, Score {total_score}")

        if verbose: print(f"Doing Car {car_id}")

        current_loc_id = -1  # Car starts at start node
        total_dist = 0  # Total dist travelled by car
        ran_out = False
        while total_dist < T and not ran_out:
            # Find the ordered list of Non-done rides closest to current loc
            close = closemap[current_loc_id]

            # print(f"Close: {close}")
            # print(f"Done rides: {done_rides}")
            # print(f"Intmap: {intmap}")

            # Mask out the done rides for this car
            mask_out_done = np.isin(close, done_rides * intmap, invert=True)
            undone_close = close[mask_out_done]

            # Pick the closest ride that can be completed
            found_doable_ride = False
            pick_next = 0
            while not found_doable_ride:
                next_considered_id = undone_close[pick_next]
                r_len = ride_lengths[next_considered_id]
                goto_len = dist(rides[current_loc_id][ei],
                                rides[next_considered_id][si])

                # If we have time to get to the considered ride, and also do it
                if r_len + goto_len <= T - total_dist:
                    found_doable_ride = True

                    # Add to done rides
                    done_rides[current_loc_id] = True

                    # Log the move
                    current_loc_id = next_considered_id
                    total_dist += r_len + goto_len
                    car_stats[car_id] += [r_len, goto_len]
                    total_score += r_len

                else:
                    pick_next += 1

                    # If we've run out of doable rides from this point, quit
                    if pick_next >= len(undone_close):
                        if verbose:
                            print(
                                f"  [Car {car_id}] stopping, can't do more rides from {current_loc_id}"
                            )
                        ran_out = True
                        break

        if verbose: print(f"Done (useful, goto) = {car_stats[car_id]}")

    print(f"All carstats (usefuls, gotos) {np.sum(car_stats, axis=0)}")
    


if __name__ == "__main__":
    fname = "data/c_no_hurry.in"
    # fname = "data/a_example.in"
    # fname = "data/b_should_be_easy.in"

    car_by_car(fname, verbose=False)
