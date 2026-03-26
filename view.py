import tkinter as tk

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
