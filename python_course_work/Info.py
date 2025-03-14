from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class AboutInfoWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("О программе")
        self.geometry('800x400')
        self.resizable(False, False)

        self.frame_title = Frame(self)
        self.frame_title.pack(side=TOP, pady=15)
        # Заголовок
        self.label_title = Label(self.frame_title, text="Шифр Виженера кодировка данных (Кириллица)",
                                 font=("Arial", 16, "bold"))
        self.label_title.pack()

        self.frame_side = Frame(self, borderwidth=3, relief="sunken")
        self.frame_side.pack(fill=X)

        # Рисунок
        self.image = Image.open("Photos/table.jpg")
        new_width = int(self.image.width / 2)
        new_height = int(self.image.height / 2)
        self.resized_image = self.image.resize((new_width, new_height))
        self.photo = ImageTk.PhotoImage(self.resized_image)

        # Рамка для изображения и информации
        self.frame1 = ttk.Frame(self.frame_side, width=330, height=280)
        self.frame1.pack(side=LEFT, padx=5)

        # Изображение
        self.image_label = ttk.Label(self.frame1, image=self.photo)
        self.image_label.image = self.photo  # Keep a reference to the image
        self.image_label.pack()  # Add padding to the image

        self.frame_text = Frame(self.frame_side, width=500, height=280)
        self.frame_text.pack(side=LEFT, padx=5, fill=X)
        # Описание программы
        self.label_desc = Label(self.frame_text, text=(
            "Программа позволяет:\n"
            "1. Вводить с клавиатуры текст и ключ для шифрования \n"
            "    и расшифровки.\n"
            "2. Использовать шифр Виженера для работы с текстами \n"
            "    на кириллице.\n"
            "3. Получить зашифрованный и расшифрованный текст.\n"
            "4. Сохранить обработанный текст в файл.\n"
            "5. Загрузит из файла исходный текст.\n"
            "6. Сохранить результаты в базу данных.\n"
            "7. Отправить письмо с зашифрованным тестом\n"
            "    из базы данных через gmail."
        ), font=("Arial", 14), justify="left")
        self.label_desc.pack()

        self.frame2 = Frame(self)
        self.frame2.pack(side=BOTTOM, anchor=S, pady=10)

        # Версия программы
        self.label_version = Label(self.frame2, text="Версия программы: release 1.0", font=("Arial", 10), fg="gray")
        self.label_version.pack(side=LEFT, padx=15)

        # Кнопка выхода
        self.exit_button = Button(self.frame2, text="Назад",font=("Arial", 14),
                                  command=self.destroy, width=20, height=2)
        self.exit_button.config(activeforeground="red")
        self.exit_button.pack(side=RIGHT, padx=15)

        self.bind("<Escape>", self.exit_app)

    def exit_app(self, event=None):
        self.destroy()
