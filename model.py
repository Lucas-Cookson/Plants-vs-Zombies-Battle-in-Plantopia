class Plant:
    def __init__(self, x, y, lane):
        self.x, self.y, self.lane, self.width, self.height = x, y, lane, 50, 50

class Zombie:
    def __init__(self, x, y, lane):
        self.x, self.y, self.lane, self.width, self.height, self.speed = x, y, lane, 50, 50, 1

    def move(self):
        self.x -= self.speed

class GameModel:
    def __init__(self):
        self.lanes, self.lane_height = 5, 120
        self.plants = [[] for _ in range(self.lanes)]
        self.zombies = [[] for _ in range(self.lanes)]

    def add_plant(self, x, lane):
        self.plants[lane].append(Plant(x, lane * self.lane_height + 35, lane))

    def add_zombie(self, x, lane):
        self.zombies[lane].append(Zombie(x, lane * self.lane_height + 35, lane))

    def update(self):
        for lane in range(self.lanes):
            for z in self.zombies[lane]:
                z.move()
