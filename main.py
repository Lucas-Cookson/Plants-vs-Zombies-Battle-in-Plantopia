import tkinter as tk
import random

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

class GameView:
    def __init__(self, root, model):
        self.model = model
        self.canvas = tk.Canvas(root, width=800, height=600, bg="lightblue")
        self.canvas.pack()
        for i in range(1, self.model.lanes):
            y = i * self.model.lane_height
            self.canvas.create_line(0, y, 800, y, fill="black", width=2)

    def draw(self):
        self.canvas.delete("plant", "zombie")
        for lane in range(self.model.lanes):
            for p in self.model.plants[lane]:
                self.canvas.create_rectangle(p.x, p.y, p.x + p.width, p.y + p.height, fill="green", tags="plant")
            for z in self.model.zombies[lane]:
                self.canvas.create_rectangle(z.x, z.y, z.x + z.width, z.y + z.height, fill="red", tags="zombie")

class GameController:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Plants vs Zombies - Phase 1")
        self.model = GameModel()
        self.view = GameView(self.root, self.model)
        self.view.canvas.bind("<Button-1>", self.place_plant)
        for _ in range(3):
            lane = random.randint(0, self.model.lanes - 1)
            self.model.add_zombie(750, lane)
        self.game_loop()

    def place_plant(self, event):
        lane = event.y // self.model.lane_height
        if 0 <= lane < self.model.lanes:
            self.model.add_plant(event.x - 25, lane)

    def game_loop(self):
        self.model.update()
        self.view.draw()
        self.root.after(50, self.game_loop)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    GameController().run()
