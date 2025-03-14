from tkinter import *
import os


class AboutAuthorWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Об авторе")
        self.geometry("290x470")
        self.resizable(False, False)

        # Загрузка изображения
        image_path = "Photos/me.jpg"
        if os.path.exists(image_path):
            self.photo = PhotoImage(file=image_path)
            Label(self, image=self.photo).pack(pady=10)
        else:
            Label(self, text="Изображение не найдено").pack(pady=10)

        self.frame = Frame(self)
        self.frame.pack()

        self.label_first = Label(self.frame, text="Автор", font=("Arial", 13, "bold"))
        self.label_first.pack()
        self.label_student = Label(self.frame, text="студент группы 10701223", font=("Arial", 13, "bold"))
        self.label_student.pack()
        self.label_fio = Label(self.frame, text="Дешко Никита Дмитриевич", font=("Arial", 13, "bold"))
        self.label_fio.pack()
        self.label_mail = Label(self.frame, text="nikitadeshko5@gmail.com", font=("Arial", 13, "bold"))
        self.label_mail.pack()

        self.button_back = Button(self, text="Назад", width=20, height=2, command=self.destroy)
        self.button_back.config(activeforeground="red")
        self.button_back.pack(pady=10)

        self.bind("<Escape>", self.exit_app)

    def exit_app(self, event=None):
        self.destroy()
