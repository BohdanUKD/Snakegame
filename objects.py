import random
from variables import *


# Створення змії
class Snake:
    def __init__(self, canvas, direction):
        self.snake_body = game_variables.BODY_PARTS
        self.coordinates = []
        self.squares = []
        self.direction = direction
        for i in range(game_variables.BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + game_variables.SPACE_SIZE, y + game_variables.SPACE_SIZE,
                                             fill=game_variables.SNAKE_COLOR, tag="snake")
            self.squares.append(square)

    # Зміна руху змії
    def change_direction(self, new_direction):

        if new_direction == "left" and self.direction != "right":
            self.direction = new_direction
        elif new_direction == "right" and self.direction != "left":
            self.direction = new_direction
        elif new_direction == "up" and self.direction != "down":
            self.direction = new_direction
        elif new_direction == "down" and self.direction != "up":
            self.direction = new_direction


# Створення фрукту з додатковою перевіркою щоб фрукт не появлявся в тих місцях які зайняті тілом змії
class Food:
    def __init__(self, canvas, snake):
        while True:
            x = (random.randint(0, (game_variables.GAME_WIDTH // game_variables.SPACE_SIZE) - 1)
                 * game_variables.SPACE_SIZE)
            y = (random.randint(0, (game_variables.GAME_HEIGHT // game_variables.SPACE_SIZE) - 1)
                 * game_variables.SPACE_SIZE)

            self.coordinates = [x, y]

            # Перевірка, чи координати не зайняті тілом змії
            if self.coordinates not in snake.coordinates:
                break

        canvas.create_oval(x, y, x + game_variables.SPACE_SIZE, y + game_variables.SPACE_SIZE,
                           fill=game_variables.FOOD_COLOR, tag="food")