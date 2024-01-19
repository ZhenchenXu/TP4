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

        arcade.draw_circle_filled(self.x, self.y, 20, (self.R, self.G, self.B))
        pass
    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.x = x
        self.y = y
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        self.R,self.G,self.B = 255,54,34
def main():
    my_game = MyGame()
    my_game.setup()

    arcade.run()


main()
