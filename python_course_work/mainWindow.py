import sys
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import AboutAuthor
import Info
import ViewAndSend
from ProcessingText import Text
from DataHandler import DatabaseHandler


class MainWindow(tk.Tk):
    def __init__(self):
        # Параметры окна
        super().__init__()
        self.title("Шифратор")
        self.geometry("900x470")
        self.resizable(height=False, width=False)
        self.configure(bg="gray60")

        # Работа с изображениями на кнопках
        self.image_author = Image.open("Photos/AboutAuthor.png")
        self.image_resized_author = self.image_author.resize((35, 35))
        self.photo_author = ImageTk.PhotoImage(self.image_resized_author)

        self.image_program = Image.open("photos/AboutProgram.png")
        self.image_resized_program = self.image_program.resize((35, 35))
        self.photo_program = ImageTk.PhotoImage(self.image_resized_program)

        self.image_exit = Image.open("Photos/Exit.png")
        self.image_resized_exit = self.image_exit.resize((35, 35))
        self.photo_exit = ImageTk.PhotoImage(self.image_resized_exit)

        self.image_load = Image.open("Photos/Load.png")
        self.image_resized_load = self.image_load.resize((35, 35))
        self.photo_load = ImageTk.PhotoImage(self.image_resized_load)

        self.image_save = Image.open("Photos/Save.png")
        self.image_resized_save = self.image_save.resize((35, 35))
        self.photo_save = ImageTk.PhotoImage(self.image_resized_save)

        self.image_db_save = Image.open("Photos/DatabaseSave.png")
        self.image_resized_db_save = (self.image_db_save.resize ((35, 35)))
        self.photo_db_save = (ImageTk.PhotoImage(self.image_resized_db_save))

        self.image_send_email = Image.open("Photos/SendEmail.png")
        self.image_resized_send_email = self.image_send_email.resize((35, 35))
        self.photo_send_email = ImageTk.PhotoImage(self.image_resized_send_email)

        self.image_encrypt = Image.open("Photos/encrypt.png")
        self.image_resized_encrypt = self.image_encrypt.resize((35, 35))
        self.photo_encrypt = ImageTk.PhotoImage(self.image_resized_encrypt)

        self.image_decrypt = Image.open("Photos/decrypt.png")
        self.image_resized_decrypt = self.image_decrypt.resize((35, 35))
        self.photo_decrypt = ImageTk.PhotoImage(self.image_resized_decrypt)

        self.image_help = Image.open("Photos/Help.png")
        self.image_resized_help = self.image_help.resize((35, 35))
        self.photo_help = ImageTk.PhotoImage(self.image_resized_help)

        # Frame исходного текста
        self.frame_ET = tk.Frame(self, borderwidth=3, relief="sunken", height=295, width=315)
        self.frame_ET.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.frame_ET.grid_propagate(False)

        self.label_ET = tk.Label(self.frame_ET, text="Введите текст:", font=("Arial", 12))
        self.label_ET.grid(row=0, column=0, padx=10, pady=10)

        self.text_ET = tk.Text(self.frame_ET, height=19, width=40)
        self.text_ET.grid(row=1, column=0, padx=10)

        # Frame обработанного текста
        self.frame_RT = tk.Frame(self, borderwidth=3, relief="sunken", height=295, width=315)
        self.frame_RT.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.frame_RT.grid_propagate(False)

        self.label_result = tk.Label(self.frame_RT, text="Обработанный текст:", font=("Arial", 12))
        self.label_result.grid(row=0, column=0, padx=10, pady=10)

        self.result_text = tk.Text(self.frame_RT, height=19, width=40)
        self.result_text.grid(row=1, column=0, padx=10)

        # Frame поля ключа и шифрования
        self.frame_KT = tk.Frame(self, borderwidth=3, relief="sunken", height=100, width=450)
        self.frame_KT.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        self.frame_KT.grid_propagate(False)

        self.frame_KT.grid_columnconfigure(0, weight=1)
        self.frame_KT.grid_columnconfigure(1, weight=1)
        self.frame_KT.grid_columnconfigure(2, weight=1)
        self.frame_KT.grid_columnconfigure(3, weight=1)

        self.key_label = tk.Label(self.frame_KT, text="Введите ключ:")
        self.key_label.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.key_entry = tk.Entry(self.frame_KT)
        self.key_entry.grid(row=0, column=1, columnspan=2, padx=5, pady=5, sticky="ew")

        # Создание объекта класса Text
        self.text_method = Text(self.text_ET, self.result_text, self.key_entry)

        self.bt_help = tk.Button(self.frame_KT, text="Help", command=self.help_clicked,
                                 image=self.photo_help, compound="left", anchor="w", padx=10)
        self.bt_help.grid(row=0, column=3, padx=5, pady=5, sticky="ew")

        self.bt_encrypt = tk.Button(self.frame_KT, text="Зашифровать", command=self.text_method.encrypt_clicked,
                                    image=self.photo_encrypt, compound="left", anchor="w")
        self.bt_encrypt.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        self.bt_decrypt = tk.Button(self.frame_KT, text="Расшифровать", command=self.text_method.decrypt_clicked,
                                    image=self.photo_decrypt, compound="left", anchor="w")
        self.bt_decrypt.grid(row=1, column=2, columnspan=2, padx=5, pady=5, sticky="nsew")

        # Frame панели кнопок
        self.frame_BT = tk.Frame(self, borderwidth=3, relief="sunken", height=490, width=200, background="grey90")
        self.frame_BT.grid(row=0, column=2, rowspan=2, padx=10, pady=10, sticky="ns")
        self.frame_BT.grid_propagate(False)

        # Верхний Frame с четырьмя кнопками
        self.top_frame = tk.Frame(self.frame_BT, borderwidth=3, relief="sunken", height=220, width=190)
        self.top_frame.pack(side=tk.TOP, padx=10, pady=10)
        self.top_frame.grid_propagate(False)

        # Кнопки в верхнем фрейме
        self.in_text = tk.Button(self.top_frame, text="Загрузить текст", command=self.text_method.load_text,
                                 image=self.photo_load, compound="left", anchor="w", padx=10)
        self.in_text.grid(row=0, column=0, sticky="ew", pady=5)

        self.out_text = tk.Button(self.top_frame, text="Сохранить текст", command=self.text_method.save_text,
                                  image=self.photo_save, compound="left", anchor="w", padx=10)
        self.out_text.grid(row=1, column=0, sticky="ew", pady=5)

        self.out_DB = tk.Button(self.top_frame, text="Сохранить в БД", command=self.save_db,
                                image=self.photo_db_save, compound="left", anchor="w", padx=10)
        self.out_DB.grid(row=2, column=0, sticky="ew", pady=5)

        self.send_mail = tk.Button(self.top_frame, text="Отправить письмо", command=self.show_mail_window,
                                   image=self.photo_send_email, compound="left", anchor="w", padx=10)
        self.send_mail.grid(row=3, column=0, sticky="ew", pady=5)

        # Нижний Frame с тремя кнопками
        self.bottom_frame = tk.Frame(self.frame_BT, borderwidth=3, relief="sunken", height=165, width=190)
        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)
        self.bottom_frame.grid_propagate(False)

        # Кнопки в нижнем фрейме
        self.button_program = tk.Button(self.bottom_frame, text="О программе", command=self.show_info_window,
                                        image=self.photo_program, compound="left", anchor="w", padx=10)
        self.button_program.grid(row=0, column=0, sticky="ew", pady=5)

        self.button_author = tk.Button(self.bottom_frame, text="Об авторе", command=self.show_author_window,
                                       image=self.photo_author, compound="left", anchor="w", padx=10)
        self.button_author.grid(row=1, column=0, sticky="ew", pady=5)

        self.button_exit = tk.Button(self.bottom_frame, text="Выход", command=self.exit_button,
                                     image=self.photo_exit, compound="left", anchor="w", padx=10)
        self.button_exit.grid(row=2, column=0, sticky="ew", pady=5)

        # Настройка grid для кнопок
        self.top_frame.grid_columnconfigure(0, weight=1)
        self.bottom_frame.grid_columnconfigure(0, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # Создание меню
        self.create_menu()
        self.bind_shortcuts()

        self.db_handler = DatabaseHandler('cipher_data.db')

    def create_menu(self):
        # Создаем главное меню
        menu_bar = tk.Menu(self)

        # Меню "File"
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Save", command=self.text_method.save_text)
        file_menu.add_command(label="Load", command=self.text_method.load_text)
        menu_bar.add_cascade(label="Файл", menu=file_menu)

        # Меню "Edit"
        edit_menu = tk.Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Copy", command=self.menu_copy)
        edit_menu.add_command(label="Paste", command=self.menu_paste)
        edit_menu.add_command(label="Cut", command=self.menu_cut)
        edit_menu.add_separator()
        edit_menu.add_command(label="Clear all", command=self.menu_clear)
        menu_bar.add_cascade(label="Изменить", menu=edit_menu)

        # Меню "Help"
        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About Program", command=self.show_info_window)
        help_menu.add_command(label="About Author", command=self.show_author_window)
        help_menu.add_command(label="Help", command=self.help_clicked)
        help_menu.add_separator()
        help_menu.add_command(label="Exit", command=self.exit_button)
        menu_bar.add_cascade(label="Помощь", menu=help_menu)

        # Устанавливаем меню в главное окно
        self.config(menu=menu_bar)

    def menu_copy(self):
        self.focus_get().event_generate("<<Copy>>")
        return "break"

    def menu_paste(self):
        self.focus_get().event_generate("<<Paste>>")
        return "break"

    def menu_cut(self):
        self.focus_get().event_generate("<<Cut>>")
        return "break"

    def menu_clear(self):
        self.text_ET.delete(1.0, tk.END)
        self.result_text.delete(1.0, tk.END)
        self.key_entry.delete(0, tk.END)

    def bind_shortcuts(self):
        self.bind("<Control-c>", lambda event: self.menu_copy())
        self.bind("<Control-v>", lambda event: self.menu_paste())
        self.bind("<Control-x>", lambda event: self.menu_cut())


    def save_db(self):
        try:
            original_text = self.text_ET.get("1.0", tk.END).strip()  # Оригинальный текст
            cipher_key = self.key_entry.get().strip()  # Ключ шифрования
            encrypted_text = self.result_text.get("1.0", tk.END).strip()  # Зашифрованный текст
            self.db_handler.save_to_db(original_text, cipher_key, encrypted_text)
            messagebox.showinfo("Успех", "Данные успешно сохранены в базу данных!")
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))

    def exit_button(self):
        self.destroy()
        sys.exit()

    def __del__(self):
        # Закрытие базы данных при удалении объекта
        if hasattr(self, 'db_handler'):
            self.db_handler.close()

    @staticmethod
    def help_clicked():
        messagebox.showinfo("Help window", "Введите текст и ключ, затем нажмите на одну из кнопок"
                                           " для шифрования или расшифровки. Тест и ключ должны быть написаны на "
                                           "кириллице. Допускается использование знаков препинания.")

    def show_info_window(self):
        Info.AboutInfoWindow(self)

    def show_mail_window(self):
        ViewAndSend.MailWindow(self)

    def show_author_window(self):
        AboutAuthor.AboutAuthorWindow(self)
