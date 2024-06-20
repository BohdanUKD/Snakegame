from tkinter import *
from variables import *
from menu import *

def main():
    # Створення початкового екрану
    window = Tk()
    window.title("Snake game")
    window.configure(bg=game_variables.BACKGROUND_COLOR)

    menu_frame = Frame(window, bg="black")
    menu_frame.pack()

    logs(window, menu_frame)

    # Створення початкових кнопок
    title_label = Label(menu_frame, text="Pysnake", font=('consolas', 50), fg="white", bg="black")
    title_label.pack(pady=80)

    start_button = Button(menu_frame, text="Старт", font=('consolas', 20), fg="white", bg="black", command=show_game)
    start_button.pack(pady=10)

    settings_button = Button(menu_frame, text="Налаштування", font=('consolas', 20), fg="white", bg="black",
                             command=show_settings)
    settings_button.pack(pady=10)

    exit_button = Button(menu_frame, text="Вийти", font=('consolas', 20), fg="white", bg="black", command=window.quit)
    exit_button.pack(pady=10)

    # Створення розмірів екрану
    window_width = 800
    window_height = 800
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    window.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))

    window.mainloop()


if __name__ == "__main__":
    main()
