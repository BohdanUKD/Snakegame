from tkinter import ALL

from objects import Food
from variables import *
import webbrowser


# Реакція гри на всі дії
def next_turn(snake, food, canvas, label, window, score, menu_frame):
    x, y = snake.coordinates[0]

    # Поворот змії
    if snake.direction == "up":
        y -= game_variables.SPACE_SIZE
    elif snake.direction == "down":
        y += game_variables.SPACE_SIZE
    elif snake.direction == "left":
        x -= game_variables.SPACE_SIZE
    elif snake.direction == "right":
        x += game_variables.SPACE_SIZE

    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + game_variables.SPACE_SIZE, y + game_variables.SPACE_SIZE,
                                     fill=game_variables.SNAKE_COLOR)
    snake.squares.insert(0, square)

    # Якщо змія з'їла фрукт +1 до загального значення, створення нового фрукта
    if x == food.coordinates[0] and y == food.coordinates[1]:

        score += 1
        label.config(text=f"Score: {score}")
        canvas.delete("food")
        food = Food(canvas, snake)
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over(canvas, label, menu_frame)
    else:
        window.after(game_variables.SPEED, next_turn, snake, food,
                     canvas, label, window, score, menu_frame)


# Перевірка на те чи змія не вдарилася
def check_collisions(snake):
    x, y = snake.coordinates[0]

    # Перевірка чи не відбувся удар в поля карти
    if x < 0 or x >= game_variables.GAME_WIDTH or y < 0 or y >= game_variables.GAME_HEIGHT:
        return True

    # Перевірка чи не відбувся удар в своє тіло
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False


# Реакція програми при програші
def game_over(canvas, label, menu_frame):
    webbrowser.open_new("https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley")
    canvas.pack_forget()
    label.pack_forget()
    menu_frame.pack()