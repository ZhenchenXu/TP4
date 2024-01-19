import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = []


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")

        self.list_Circle = []
        self.list_Rectangle = []

    def setup(self):
        pass

    def on_draw(self):
        arcade.start_render()



class Ball:
    def __init__(self):
        self.rayon = random.randint(10,30)
    def on_mouse_motion(self):
        self.x = x
        self.y = y

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            Mygame.list_Circle.append[self.x, self.y]
def main():
    my_game = MyGame()
    my_game.setup()

    arcade.run()


main()
