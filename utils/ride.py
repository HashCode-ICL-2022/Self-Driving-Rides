
class Ride:
    def __init__(self, start, end, earliest_start, latest_finish, bonus=0):
        self.start = start
        self.end = end

        self.earliest_start = earliest_start
        self.latest_finish = latest_finish

        self.bonus = bonus
        self.distance = self.manhatten(start, end)

        self.reward = self.distance + bonus

    def manhatten(self, start, end):
        (x0, y0), (x1, y1) = start, end
        return abs(x1 - x0) + abs(y1 - y0)
