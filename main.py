import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = []


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")

        pass

    def setup(self):
        pass

    def on_draw(self):
        arcade.start_render()

        arcade.draw_circle_filled(self.x, self.y, 20, (255, 35, 34))
        pass
    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.x = x
        self.y = y

def main():
    my_game = MyGame()
    my_game.setup()

    arcade.run()


main()
