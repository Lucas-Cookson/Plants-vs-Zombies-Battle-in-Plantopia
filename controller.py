import tkinter as tk
import random
from model import GameModel
from view import GameView

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
