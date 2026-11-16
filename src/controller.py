from rich.live import Live
from src.game import TwentyFortyEight
from src.renderer import GameRenderer
import readchar


class GameController:

    def __init__(self):
        self.game = TwentyFortyEight()
        self.renderer = GameRenderer()

        self.keymap = self.init_keymap()

    def init_keymap(self):
        keymap = {}
        for inputs, direction in (
            ((readchar.key.LEFT, "a", "h"), "L"),
            ((readchar.key.DOWN, "s", "j"), "D"),
            ((readchar.key.UP, "w", "k"), "U"),
            ((readchar.key.RIGHT, "d", "l"), "R")
        ):
            for input in inputs:
                keymap[input] = direction

        return keymap

    def reset(self):
        self.game = TwentyFortyEight()

    def run(self):
        with Live(self.renderer.render(self.game, game_over=False), screen=False, auto_refresh=True) as live:
            while True:
                if not self.game.game_over_detection():
                    live.update(
                        self.renderer.render(
                            self.game,
                            game_over=False
                        ),
                        refresh=True
                    )

                    key = readchar.readkey()

                    if key == "q":
                        return
                    if key == "r":
                        self.reset()

                    direction = self.keymap.get(key)
                    if direction is None:
                        continue
                    else:
                        if self.game.move(direction):
                            self.game.add_new_tile()

                else:
                    live.update(
                        self.renderer.render(
                            self.game,
                            game_over=True
                        ),
                        refresh=True
                    )
                    while True:
                        key = readchar.readkey()

                        if key == "q":
                            return
                        if key == "r":
                            self.reset()
                            break
