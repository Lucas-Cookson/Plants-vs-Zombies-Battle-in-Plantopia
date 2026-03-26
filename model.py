class Plant:
    def __init__(self, x, y, lane):
        self.x = x
        self.y = y
        self.lane = lane
        self.width = 50
        self.height = 50

class Zombie:
    def __init__(self, x, y, lane):
        self.x = x
        self.y = y
        self.lane = lane
        self.width = 50
        self.height = 50
        self.speed = 1

    def move(self):
        self.x -= self.speed

class GameModel:
    def __init__(self):
        self.lanes = 5
        self.lane_height = 120  # 600 / 5
        self.plants = []  # list of lists, one per lane
        self.zombies = []  # list of lists, one per lane
        for _ in range(self.lanes):
            self.plants.append([])
            self.zombies.append([])

    def add_plant(self, x, lane):
        plant = Plant(x, lane * self.lane_height + 35, lane)  # center in lane
        self.plants[lane].append(plant)

    def add_zombie(self, x, lane):
        zombie = Zombie(x, lane * self.lane_height + 35, lane)
        self.zombies[lane].append(zombie)

    def update(self):
        for lane in range(self.lanes):
            for zombie in self.zombies[lane]:
                zombie.move()
