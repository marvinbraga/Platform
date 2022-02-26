from core.abstract_game_loop import AbstractGameLoop


class GameLoop(AbstractGameLoop):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    def draw(self):
        pass

    def check_keys(self, event):
        pass

    def check_events(self, event):
        pass
