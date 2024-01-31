import arcade
import random
#définir la grandeur de l'écran
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

#les couleurs inclue dans la list qu'ont choisi randomly
COLORS = [arcade.color.RED, arcade.color.BLUE, arcade.color.GREEN, arcade.color.YELLOW, arcade.color.ORANGE, arcade.color.PURPLE, arcade.color.PINK]



#la classe Ball
class Ball:
    # définit le rayon position , la direction où le cercle va aller et son couleur
    def __init__(self, x, y, rayon, color):
        self.rayon = rayon
        self.x = x
        self.y = y
        self.change_x = 100
        self.change_y = 100
        self.color = color


    #fonciton pour prévenir le cercle de sortir de l'écran
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
    #fonction pour dessiner le cercle sur l'écran
    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.rayon, self.color)

#La classe rectangle
class Rectangle:
    #commencer la class rectangle en définisant son grandeur, angle, position et direction et vitesse qu'il va aller et son couleur.
    def __init__(self, x, y, width, height, angle, color):
        self.width = width
        self.height = height
        self.angle = angle
        self.x = x
        self.y = y
        self.change_x = 100
        self.change_y = 100
        self.color = color

    #prévenir le rectangle de sortir de l'écran
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
    #dessiner le rectangle sur l'écran
    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color, self.angle)


#main class de pygame
class MyGame(arcade.Window):
    #commencer le fonction MyGame et définir les listes qui contiennent les listes balls et les listes rectangles
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")

        self.Balls = []
        self.Rectangles = []

    #définir le couleur en arrière plan
    def setup(self):
        arcade.set_background_color(arcade.color.BLACK)
    #fonction pour appeller les fonctions pour dessiner les balls et les rectangles.
    def on_draw(self):
        arcade.start_render()
        for ball in self.Balls:
            ball.draw()
        for rectangle in self.Rectangles:
            rectangle.draw()
    #update le position des ballons afin de les dessiners au bon endroit.
    def on_update(self, delta_time):
        for ball in self.Balls:
            ball.update()
        for rectangle in self.Rectangles:
            rectangle.update()

    #fonction pour ajouter une ball ou un rectamge à l'écran quand il y a une click du souris
    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            ball = Ball(x, y, 30, random.choice(COLORS))
            self.Balls.append(ball)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            rectangle = Rectangle(x, y, 40, 80, 0, random.choice(COLORS))
            self.Rectangles.append(rectangle)

#le fonction qui commence le programme complet
def main():
    my_game = MyGame()
    my_game.setup()

    arcade.run()


main()
