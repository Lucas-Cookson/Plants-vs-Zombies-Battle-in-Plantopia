import tkinter as tk

class GameView:
    def __init__(self, root, model):
        self.model = model
        self.canvas = tk.Canvas(root, width=800, height=600, bg="lightblue")
        self.canvas.pack()
        # Draw lane lines
        for i in range(1, self.model.lanes):
            y = i * self.model.lane_height
            self.canvas.create_line(0, y, 800, y, fill="black", width=2)

    def draw(self):
        self.canvas.delete("plant", "zombie")  # keep lane lines
        for lane in range(self.model.lanes):
            for plant in self.model.plants[lane]:
                self.canvas.create_rectangle(plant.x, plant.y, plant.x + plant.width, plant.y + plant.height, fill="green", tags="plant")
            for zombie in self.model.zombies[lane]:
                self.canvas.create_rectangle(zombie.x, zombie.y, zombie.x + zombie.width, zombie.y + zombie.height, fill="red", tags="zombie")
