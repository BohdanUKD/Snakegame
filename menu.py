from tkinter import *
from objects import *
from movement import *
from variables import *


# Витягання із main параметрів window, menu_frames
def logs(windows, menu_frames):
    global window, menu_frame
    window = windows
    menu_frame = menu_frames


# Запуск гри
def show_game():
    direction = 'right'
    score = 0

    menu_frame.pack_forget()

    # Cтворення Score
    label = Label(window, text="Score: {}".format(score), font=('consolas', 40))
    label.pack()
    # Створення ігрового вікна
    canvas = Canvas(window, bg=game_variables.BACKGROUND_COLOR, height=game_variables.GAME_HEIGHT,
                    width=game_variables.GAME_WIDTH)
    canvas.pack()

    window.update()
    snake = Snake(canvas, direction)
    food = Food(canvas, snake)

    #Захоплення кнопок
    window.bind('<Left>', lambda event: snake.change_direction("left"))
    window.bind('<Right>', lambda event: snake.change_direction("right"))
    window.bind('<Up>', lambda event: snake.change_direction("up"))
    window.bind('<Down>', lambda event: snake.change_direction("down"))

    next_turn(snake, food, canvas, label, window, score, menu_frame)


# Реакція коду на вибір значень в налаштуваннях
def apply_settings():
    global SPEED, SNAKE_COLOR, GAME_WIDTH, GAME_HEIGHT

    # Швидкість змії
    speed = speed_var.get()
    if speed == "Низька":
        game_variables.SPEED = 150
    elif speed == "Середня":
        game_variables.SPEED = 100
    elif speed == "Висока":
        game_variables.SPEED = 50

    # Колір змії
    color = color_var.get()
    if color == "Зелений":
        game_variables.SNAKE_COLOR = "green"
    elif color == "Жовтий":
        game_variables.SNAKE_COLOR = "yellow"
    elif color == "Синій":
        game_variables.SNAKE_COLOR = "blue"

    # Розмір ігрового поля
    size = size_var.get()
    if size == "Маленька":
        game_variables.GAME_WIDTH = 300
        game_variables.GAME_HEIGHT = 300
    elif size == "Середня":
        game_variables.GAME_WIDTH = 700
        game_variables.GAME_HEIGHT = 700
    elif size == "Велика":
        game_variables.GAME_WIDTH = 1000
        game_variables.GAME_HEIGHT = 1000

    settings_frame.pack_forget()
    show_game()


# Налаштування
def show_settings():
    global settings_frame, speed_var, color_var, size_var

    menu_frame.pack_forget()
    settings_frame = Frame(window, bg="black")
    settings_frame.pack()

    # Шрифт для текстових елементів
    font_style_label = ('consolas', 20)
    font_style_option = ('consolas', 15)
    label_color = 'white'

    # Налаштування розміру карти
    Label(settings_frame, text="Розмір карти", font=font_style_label, fg=label_color, bg="black").pack()
    size_var = StringVar(window)
    size_var.set("Середня")
    size_choices = ["Маленька", "Середня", "Велика"]
    option_menu = OptionMenu(settings_frame, size_var, *size_choices)
    option_menu.config(font=font_style_option, fg=label_color, bg="black")
    option_menu.pack()

    # Налаштування швидкості змії
    Label(settings_frame, text="Швидкість гри", font=font_style_label, fg=label_color, bg="black").pack(pady=10)
    speed_var = StringVar(window)
    speed_var.set("Середня")
    speed_choices = ["Низька", "Середня", "Висока"]
    option_menu = OptionMenu(settings_frame, speed_var, *speed_choices)
    option_menu.config(font=font_style_option, fg=label_color, bg="black")
    option_menu.pack()

    # Налаштування кольору змії
    Label(settings_frame, text="Колір змії", font=font_style_label, fg=label_color, bg="black").pack(pady=10)
    color_var = StringVar(window)
    color_var.set("Зелений")
    color_choices = ["Зелений", "Жовтий", "Синій"]
    option_menu = OptionMenu(settings_frame, color_var, *color_choices)
    option_menu.config(font=font_style_option, fg=label_color, bg="black")
    option_menu.pack()

    save_button = Button(settings_frame, text="Зберегти", font=font_style_label, fg=label_color, bg="black",
                         command=apply_settings)
    save_button.pack(pady=20)
