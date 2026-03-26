class GameController:
    def __init__(self, model):
        self.model = model

    def place_plant(self, event):
        lane = event.y // self.model.lane_height
        if 0 <= lane < self.model.lanes:
            self.model.add_plant(event.x - 25, lane)
