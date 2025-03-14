import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import io
import CipherFile

class Text:
    def __init__(self, text_widget, result_widget, key_entry):
        self.text_ET = text_widget
        self.result_text = result_widget
        self.key_entry = key_entry

        self.cipher_instance = CipherFile.Cipher()

    def save_text(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"),
                                                            ("PDF files", "*.pdf"),
                                                            ("All files", "*.*")])
        if file_path:
            text_to_save = self.result_text.get("1.0", tk.END)
            if file_path.endswith(".pdf"):
                text_to_save = text_to_save.strip()

                packet = io.BytesIO()
                can = canvas.Canvas(packet, pagesize=letter)

                pdfmetrics.registerFont(TTFont('Font', 'RussianFont.ttf'))
                can.setFont("Font", 12)

                lines = text_to_save.split('\n')
                y_position = 750

                for line in lines:
                    can.drawString(40, y_position, line)
                    y_position -= 14
                    if y_position < 50:
                        can.showPage()
                        can.setFont("Arial", 12)
                        y_position = 750

                can.save()
                with open(file_path, "wb") as file:
                    file.write(packet.getvalue())
            else:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(text_to_save)

    def load_text(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"),
                                                          ("PDF files", "*.pdf"),
                                                          ("All files", "*.*")])
        if file_path:
            if file_path.endswith(".pdf"):
                with open(file_path, "rb") as file:
                    pdf_reader = PdfReader(file)
                    loaded_text = ""
                    for page in pdf_reader.pages:
                        loaded_text += page.extract_text() or ""

                    self.text_ET.delete("1.0", tk.END)
                    self.text_ET.insert(tk.END, loaded_text)
                    self.key_entry.delete(0, tk.END)
                    self.result_text.delete("1.0", tk.END)
            else:
                with open(file_path, 'r', encoding='utf-8') as file:
                    loaded_text = file.read()
                    self.text_ET.delete("1.0", tk.END)
                    self.text_ET.insert(tk.END, loaded_text)
                    self.key_entry.delete(0, tk.END)
                    self.result_text.delete("1.0", tk.END)

    def __process_text(self):
        text = self.text_ET.get("1.0", tk.END).strip()  # Оставляем текст в исходном регистре
        key = self.key_entry.get().strip()  # Оставляем ключ в исходном регистре

        # Проверка на заполненность полей текста и ключа
        if not text or not key:
            messagebox.showerror("Ошибка", "Поля текста и ключа должны быть заполнены!")
            return None

        # Игнорируем пробелы и переносы строк при валидации
        if not self.cipher_instance.validate_input(text.replace("\n", "").replace(" ", ""), key):
            messagebox.showerror("Ошибка", "Текст и ключ должны содержать только буквы кириллицы!")
            return None

        return text, key

    def encrypt_clicked(self):
        result = self.__process_text()
        if result is None:
            return

        text, key = result
        encrypted_text = self.cipher_instance.vigenere_encrypt(text, key)
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, encrypted_text)

    def decrypt_clicked(self):
        result = self.__process_text()
        if result is None:
            return

        text, key = result
        decrypted_text = self.cipher_instance.vigenere_decrypt(text, key)
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, decrypted_text)
