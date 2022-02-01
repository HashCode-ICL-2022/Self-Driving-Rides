
class Car:
    def __init__(self, id):
        self.id = id
        self.location = (0, 0)

        self.ride = None
        self.is_riding = False

        self.expected_start = None
        self.expected_finish = None

        self.prev_rides = list()

    @property
    def is_free(self):
        return self.ride is None

    def add_ride(self, ride):
        self.ride = ride

        self.expected_start = self.distance_to_start(ride)
        self.expected_finish = self.total_ride_distance(ride)

        self.location = self.ride.start

    def start_ride(self):
        self.is_riding = True
        self.location = self.ride.end

    def finish_ride(self):
        self.prev_rides.append(self.ride.id)

        self.ride = None
        self.is_riding = False

        self.expected_start = None
        self.expected_finish = None

    def check_ride_finished(self, step):
        if not self.ride:
            return

        if not self.is_riding and self.expected_start <= step:
            self.start_ride()
        elif self.is_riding and self.expected_finish <= step:
            self.finish_ride()

    def manhatten(self, start, end):
        (x0, y0), (x1, y1) = start, end
        return abs(x1 - x0) + abs(y1 - y0)

    def distance_to_start(self, ride):
        return self.manhatten(self.location, ride.start)

    def total_ride_distance(self, ride):
        distance_to_start = self.distance_to_start(ride)
        return distance_to_start + ride.distance

    def can_finish(self, ride, step):
        total_distance = self.total_ride_distance(ride)
        return step + total_distance <= ride.latest_finish
