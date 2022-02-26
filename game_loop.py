from core.abstract_game_loop import AbstractGameLoop
from game import Game


class GameLoop(AbstractGameLoop):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.game = Game()
        self.add_valid_key(*self.game.valid_keys)

    def draw(self):
        self.game.draw(self.window)
        self.game.update()

    def check_keys(self, event):
        self.game.check_keys(event)

    def check_events(self, event):
        self.game.check_events(event)
