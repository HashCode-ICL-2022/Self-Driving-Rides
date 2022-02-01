
class Ride:
    def __init__(self, start, end, earliest_start, latest_finish, id):
        self.start = start
        self.end = end

        self.earliest_start = earliest_start
        self.latest_finish = latest_finish

        self.id = id

        self.distance = self.manhatten(start, end)
        self.reward = self.distance

        self.done = False
        self.on_time = False

    def manhatten(self, start, end):
        (x0, y0), (x1, y1) = start, end
        return abs(x1 - x0) + abs(y1 - y0)

    def mark_as_done(self, step):
        self.done = True

        if step <= self.latest_finish:
            self.on_time = True