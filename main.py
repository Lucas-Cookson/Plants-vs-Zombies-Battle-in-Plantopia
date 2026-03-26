import tkinter as tk
import random
from model import GameModel
from view import GameView
from controller import GameController

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Plants vs Zombies - Phase 1")
    model = GameModel()
    view = GameView(root, model)
    controller = GameController(model)
    view.canvas.bind("<Button-1>", controller.place_plant)
    
    for _ in range(3):
        lane = random.randint(0, model.lanes - 1)
        model.add_zombie(750, lane)
    
    def game_loop():
        model.update()
        view.draw()
        root.after(50, game_loop)
    
    game_loop()
    root.mainloop()
