import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from SetGmailApi import send_user_mail
from DataHandler import DatabaseHandler

class MailWindow(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Отправить письмо")
        self.geometry("750x300")
        self.resizable(False, False)
        self.configure(bg="gray60")

        # Загрузка картинок
        self.image_gmail = Image.open("Photos/Gmail.png")
        self.image_resized_gmail = self.image_gmail.resize((35, 35))
        self.photo_gmail = ImageTk.PhotoImage(self.image_resized_gmail)

        self.image_back = Image.open("Photos/Back.png")
        self.image_resized_back = self.image_back.resize((35, 35))
        self.photo_back = ImageTk.PhotoImage(self.image_resized_back)

        self.image_delete = Image.open("Photos/Trash.png")
        self.image_resized_delete = self.image_delete.resize((35, 35))
        self.photo_delete = ImageTk.PhotoImage(self.image_resized_delete)

        # Основной Frame для размещения таблицы и панели с вводом почты
        main_frame = tk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Frame для таблицы
        table_frame = tk.Frame(main_frame, borderwidth=3, relief="sunken")
        table_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Добавление прокрутки для таблицы
        scrollbar_y = tk.Scrollbar(table_frame, orient=tk.VERTICAL)

        # Создание виджета Treeview для отображения данных
        self.tree = ttk.Treeview(
            table_frame,
            columns=("original_text", "cipher_key", "encrypted_text"),
            show='headings',
            yscrollcommand=scrollbar_y.set,
        )

        # Настройка заголовков столбцов
        self.tree.heading("original_text", text="Исходный текст")
        self.tree.heading("cipher_key", text="Ключ")
        self.tree.heading("encrypted_text", text="Зашифрованный текст")

        self.tree.column("original_text", width=150)
        self.tree.column("cipher_key", width=100)
        self.tree.column("encrypted_text", width=150)

        # Привязка прокрутки
        scrollbar_y.config(command=self.tree.yview)
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Frame для ввода почты и статуса отправки
        input_frame = tk.Frame(main_frame, borderwidth=3, relief="sunken")
        input_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)

        # Поле для ввода почты
        email_label = tk.Label(input_frame, text="Введите свою почту Gmail")
        email_label.pack(anchor=tk.W, pady=(0, 5))
        self.email_entry = tk.Entry(input_frame, width=30)
        self.email_entry.pack(anchor=tk.W, pady=(0, 10))

        # Frame для кнопок "Удалить" и "Отправить"
        button_frame = tk.Frame(input_frame, borderwidth=1)
        button_frame.pack(anchor=tk.W, pady=(0, 10), fill=tk.X)

        # Кнопка "Удалить"
        delete_button = tk.Button(button_frame, text="Удалить", command=self.delete_entry,
                                  image=self.photo_delete, compound="left", anchor="w", padx=10)
        delete_button.grid(row=0, column=0)

        # Кнопка "Отправить"
        send_button = tk.Button(button_frame, text="Отправить", command=self.send_encrypted_text,
                                image=self.photo_gmail, compound="left", anchor="w", padx=9)
        send_button.grid(row=0, column=1)

        # Поле для отображения статуса отправки
        self.status_label = tk.Label(input_frame, text="Статус отправки:")
        self.status_label.pack(anchor=tk.W)
        self.status_text = tk.Text(input_frame, width=30, height=5, state=tk.DISABLED)
        self.status_text.pack(anchor=tk.W, pady=(5, 0), fill=tk.X)

        self.back_button = tk.Button(input_frame, text="Назад", command=self.destroy,
                                     image=self.photo_back, compound="left", anchor="w", padx=10)
        self.back_button.pack(anchor=tk.W, pady=(0, 10), fill=tk.X)

        # Подключение к базе данных через DatabaseHandler
        self.db_handler = DatabaseHandler('cipher_data.db')

        # Загрузка данных из базы данных
        self.load_data()

        # Событие для выбора строки в таблице
        self.tree.bind("<<TreeviewSelect>>", self.on_row_selected)
        self.selected_encrypted_text = None  # Переменная для хранения выбранного encrypted_text

        self.bind("<Escape>", self.exit_app)

    def exit_app(self, event=None):
        self.destroy()

    def load_data(self):
        # Загружаем данные из базы данных через DatabaseHandler
        data = self.db_handler.load_data()

        # Очищаем текущие данные в Treeview
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Добавляем данные в Treeview
        for row in data:
            self.tree.insert("", tk.END, values=row)

    def on_row_selected(self, event):
        # Получаем выбранную строку
        selected_item = self.tree.selection()
        if selected_item:
            values = self.tree.item(selected_item, "values")
            self.selected_encrypted_text = values[2]  # Получаем значение encrypted_text
            # Обновляем статус отправки
            self.status_text.config(state=tk.NORMAL)
            self.status_text.delete(1.0, tk.END)
            self.status_text.insert(tk.END, f"Выбранный текст: {self.selected_encrypted_text}")
            self.status_text.config(state=tk.DISABLED)

    def send_encrypted_text(self):
        # Получение email из поля ввода и проверка на выбор encrypted_text
        email = self.email_entry.get().strip()
        if not email:
            messagebox.showwarning("Внимание", "Введите свою почту Gmail.")
            return

        if self.selected_encrypted_text is None:
            messagebox.showwarning("Внимание", "Выберите строку в таблице.")
            return

        if send_user_mail(email, self.selected_encrypted_text):
            # Обновление статуса отправки
            self.status_text.config(state=tk.NORMAL)
            self.status_text.insert(tk.END, f"\nТекст '{self.selected_encrypted_text}' \nотправлен на {email}")
            self.status_text.config(state=tk.DISABLED)
        else:
            self.status_text.config(state=tk.NORMAL)
            self.status_text.insert(tk.END, f"Ошибка оправки")
            self.status_text.config(state=tk.DISABLED)

    def delete_entry(self):
        # Удаляет запись из базы данных через DatabaseHandler
        if not self.selected_encrypted_text:
            messagebox.showwarning("Внимание", "Выберите строку для удаления.")
            return

        try:
            self.db_handler.delete_entry(self.selected_encrypted_text)
            messagebox.showinfo("Успех", "Запись удалена.")
            self.load_data()
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось удалить запись: {e}")

        self.status_text.config(state=tk.NORMAL)
        self.status_text.delete(1.0, tk.END)

    def __del__(self):
        # Закрытие соединения с базой данных через DatabaseHandler
        self.db_handler.close()
