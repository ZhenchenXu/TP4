import arcade
import random

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

COLORS = [arcade.color.RED, arcade.color.BLUE, arcade.color.GREEN, arcade.color.YELLOW, arcade.color.ORANGE, arcade.color.PURPLE, arcade.color.PINK]




class Ball:
    def __init__(self, x, y, rayon, color):
        self.rayon = rayon
        self.x = x
        self.y = y
        self.change_x = 10
        self.change_y = 10
        self.color = color


    def update(self):
        self.y += self.change_y
        self.x += self.change_x

        if self.x > SCREEN_WIDTH - self.rayon:
            self.x = SCREEN_WIDTH - self.rayon
            self.change_x *= -1
        elif self.x < self.rayon:
            self.x = self.rayon
            self.change_x *= -1
        if self.y > SCREEN_HEIGHT - self.rayon:
            self.y = SCREEN_HEIGHT - self.rayon
            self.change_y *= -1
        elif self.y < self.rayon:
            self.y = self.rayon
            self.change_y *= -1

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.rayon, self.color)

class Rectangle:
    def __init__(self, x, y, width, height, angle, color):
        self.width = width
        self.height = height
        self.angle = angle
        self.x = x
        self.y = y
        self.change_x = 10
        self.change_y = 10
        self.color = color


    def update(self):
        self.y += self.change_y
        self.x += self.change_x

        if self.x > SCREEN_WIDTH - self.width:
            self.x = SCREEN_WIDTH - self.width
            self.change_x *= -1
        elif self.x < 0:
            self.x = 0
            self.change_x *= -1
        if self.y > SCREEN_HEIGHT - self.height:
            self.y = SCREEN_HEIGHT - self.height
            self.change_y *= -1
        elif self.y < 0:
            self.y = 0
            self.change_y *= -1

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, random.choice(COLORS), self.angle)


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")

        self.Balls = []
        self.Rectangles = []

    def setup(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        for ball in self.Balls:
            ball.draw()
        for rectangle in self.Rectangles:
            rectangle.draw()

    def on_update(self, delta_time):
        for ball in self.Balls:
            ball.update()
        for rectangle in self.Rectangles:
            rectangle.update()
    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            ball = Ball(x, y, 30, random.choice(COLORS))
            self.Balls.append(ball)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            rectangle = Rectangle(x, y, 30, 30, random.choice(COLORS))
            self.Rectangles.append(rectangle)

def main():
    my_game = MyGame()
    my_game.setup()

    arcade.run()


main()
