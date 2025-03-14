import sqlite3

class DatabaseHandler:
    def __init__(self, db_path):
        self.__db_path = db_path
        self.conn = sqlite3.connect(self.__db_path)
        self.cursor = self.conn.cursor()
        self.__create_table()

    def __create_table(self):
        """
        Создает таблицу cipher_data, если она еще не существует.
        """
        query = '''
        CREATE TABLE IF NOT EXISTS cipher_data (
            original_text TEXT,
            cipher_key TEXT,
            encrypted_text TEXT
        )
        '''
        self.conn.execute(query)
        self.conn.commit()

    def save_to_db(self, original_text, cipher_key, encrypted_text):
        """
        Сохраняет данные в таблицу cipher_data.
        :param original_text: Исходный текст.
        :param cipher_key: Ключ шифрования.
        :param encrypted_text: Зашифрованный текст.
        """
        if not original_text or not cipher_key or not encrypted_text:
            raise ValueError("Все поля должны быть заполнены!")
        query = "INSERT INTO cipher_data (original_text, cipher_key, encrypted_text) VALUES (?, ?, ?)"
        self.conn.execute(query, (original_text, cipher_key, encrypted_text))
        self.conn.commit()

    def load_data(self):
        """
        Загружает все данные из таблицы cipher_data.
        :return: Список кортежей с данными из базы.
        """
        query = "SELECT original_text, cipher_key, encrypted_text FROM cipher_data"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def delete_entry(self, encrypted_text):
        """
        Удаляет запись из таблицы cipher_data по зашифрованному тексту.
        :param encrypted_text: Зашифрованный текст для удаления.
        """
        if not encrypted_text:
            raise ValueError("Не указан текст для удаления.")
        query = "DELETE FROM cipher_data WHERE encrypted_text = ?"
        self.cursor.execute(query, (encrypted_text,))
        self.conn.commit()

    def close(self):
        """
        Закрывает соединение с базой данных.
        """
        if self.conn:
            self.conn.close()
