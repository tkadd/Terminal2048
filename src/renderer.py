from rich.align import Align
from rich.box import ROUNDED
from rich.panel import Panel
from rich.table import Table
from rich.text import Text


class GameRenderer:

    def __init__(self):
        self.tile_width = 15
        self.tile_height = 6

        self.tile_palette = self.colour_palette()

    def colour_palette(self):
        """2048 colour palette"""
        tile_palette = {
            # exponent: (fg, bg)
            0: ("#776e65", "#cdc1b4"),
            1: ("#776e65", "#eeefda"),
            2: ("#776e65", "#ede0c8"),
            3: ("#f9f6f2", "#f2b179"),
            4: ("#f9f6f2", "#f59563"),
            5: ("#f9f6f2", "#f67c5f"),
            6: ("#f9f6f2", "#f65e3b"),
            7: ("#f9f6f2", "#edcf72"),
            8: ("#f9f6f2", "#edcc61"),
            9: ("#f9f6f2", "#edc850"),
            10: ("#f9f6f2", "#edc53f"),
            11: ("#f9f6f2", "#edc22e")
        }
        return tile_palette

    def get_tile(self, exponent):
        fg, bg = self.tile_palette.get(exponent, ("#f9f6f2", "#3c3a32"))

        text = str(2**exponent) if exponent else ""

        tile = Panel(
            Align.center(Text(text, style=f"bold {fg}"), vertical="middle"),
            width=self.tile_width,
            height=self.tile_height,
            style=f"on {bg}",
            border_style=bg,
            padding=0
        )

        return tile

    def make_title(self):
        return Text(
            "2048",
            style="bold yellow",
            justify="center"
        )

    def make_score(self, game):
        return Text(
            f"Score: {game.score}",
            style="bold white",
            justify="center"
        )

    def make_board(self, game):
        board = Table.grid(padding=0)
        for _ in range(4):
            board.add_column()
        for i in range(4):
            row = game.board[4*i: 4*i + 4]
            board.add_row(
                *[
                    self.get_tile(row[j]) for j in range(4)
                ]
            )
        return board

    def make_instructions(self, game_over):
        text = "Moves: WASD / Vim keys / Arrows\nRestart: R    Quit: Q" if (
            not game_over
        ) else "GAME OVER!\nR to restart - Q to quit"
        instructions = Text(
            text,
            style="bold white",
            justify="center"
        )
        return instructions

    def render(self, game, game_over):
        # --- Main Layout ---
        layout = Table(
            show_header=False,
            show_lines=True,
            box=ROUNDED,
            expand=False,
            padding=(0, 1)
        )
        elements = [
            self.make_title(),
            self.make_score(game),
            self.make_board(game),
            self.make_instructions(game_over)
        ]
        for element in elements:
            layout.add_row(Align.center(element))

        return layout


if __name__ == "__main__":
    pass
