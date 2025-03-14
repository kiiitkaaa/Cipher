from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
import mainWindow


class SplashScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Splash Screen")
        self.geometry("550x450")
        # Убираем заголовок окна
        self.title_bar_visible = False
        self.overrideredirect(True)

        self.header_label = ttk.Label(self, text="Белорусский национальный технический университет",
                                      font=("Arial", 14, "bold"))
        self.header_label.pack(pady=10)

        self.faculty_label = ttk.Label(self, text="Факультет информационных технологий и робототехники",
                                       font=("Arial", 12))
        self.faculty_label.pack()
        self.department_label = ttk.Label(self,
                                          text="Кафедра программного обеспечения информационных систем и технологий",
                                          font=("Arial", 12))
        self.department_label.pack()

        self.title_label = ttk.Label(self, text="Курсовой проект", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=20)

        self.discipline_label = ttk.Label(self, text="по дисциплине Языки программирования", font=("Arial", 14))
        self.discipline_label.pack()
        self.project_label = ttk.Label(self, text="Шифр Виженера кодирования данных (кириллица)",
                                       font=("Arial", 20, "bold"))
        self.project_label.pack(pady=10)

        self.image = Image.open("Photos/Safe.png")
        new_width = int(self.image.width * 1.2)
        new_height = int(self.image.height * 1.2)
        self.resized_image = self.image.resize((new_width, new_height))
        self.photo = ImageTk.PhotoImage(self.resized_image)

        self.frame1 = ttk.Frame(self)
        self.frame1.pack()

        self.image_label = ttk.Label(self.frame1, image=self.photo)
        self.image_label.image = self.photo
        self.image_label.pack(side=LEFT, padx=20)

        self.author_label = ttk.Label(self.frame1, text="  Выполнил: студент группы 10701223\n  "
                                                        "Дешко Никита Дмитриевич", font=("Arial", 12))
        self.author_label.pack(pady=20)

        self.teacher_label = ttk.Label(self.frame1, text="Преподаватель: к.ф.-м.н., доц.\nСидорик Валерий Владимирович",
                                       font=("Arial", 12, "bold"))
        self.teacher_label.pack(pady=20)

        self.place_label = ttk.Label(self, text="Минск, 2024", font=("Arial", 12, "bold"))
        self.place_label.pack(pady=20)

        self.button_frame = ttk.Frame(self)
        self.button_frame.pack()

        self.button_frame.columnconfigure(0, weight=1)
        self.button_frame.columnconfigure(1, weight=1)

        self.next_button = ttk.Button(self.button_frame, text="Далее", width=25, command=self.next_button_clicked)
        self.next_button.grid(column=0, row=0, sticky="ew", padx=1)

        self.exit_button = ttk.Button(self.button_frame, text="Выход", width=25, command=self.destroy)
        self.exit_button.grid(column=1, row=0, sticky="ew", padx=1)

        self.image_icon = Image.open("Photos/IconCipher.png")
        self.photo_icon = ImageTk.PhotoImage(self.image_icon)
        self.iconphoto(False, self.photo_icon)

        # Запуск таймера для автоматического закрытия
        self.after(60000, self.destroy)

        # Привязываем событие клика для переключения заголовочной панели
        self.bind("<Button-1>", self.toggle_title_bar)

    def toggle_title_bar(self, event=None):
        """Переключение заголовочной панели окна."""
        # Проверяем, что клик произошел не на кнопках
        if event.widget != self.next_button and  event.widget != self.exit_button:
            self.title_bar_visible = not self.title_bar_visible
            self.overrideredirect(not self.title_bar_visible)
            self.resizable(False, False)

    def next_button_clicked(self):
        self.destroy()  # Закрываем SplashScreen
        root = mainWindow.MainWindow()
        root.mainloop()



if __name__ == "__main__":
    splash_screen = SplashScreen()
    splash_screen.mainloop()
