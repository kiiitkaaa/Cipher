class Cipher:
    def __init__(self):
        self.__upper_alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        self.__lower_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"


    def vigenere_decrypt(self, text, key):
        decrypted_text = ""
        key_repeated = (key * (len(text) // len(key))) + key[:len(text) % len(key)]
        key_index = 0  # Индекс для ключа, чтобы пропускать неалфавитные символы

        for char in text:
            if char in self.__upper_alphabet:
                char_index = self.__upper_alphabet.index(char)
                key_char = key_repeated[key_index % len(key)]
                key_char_index = self.__upper_alphabet.index(key_char.upper())
                decrypted_text += self.__upper_alphabet[(char_index - key_char_index) % len(self.__upper_alphabet)]
                key_index += 1
            elif char in self.__lower_alphabet:
                char_index = self.__lower_alphabet.index(char)
                key_char = key_repeated[key_index % len(key)]
                key_char_index = self.__lower_alphabet.index(key_char.lower())
                decrypted_text += self.__lower_alphabet[(char_index - key_char_index) % len(self.__lower_alphabet)]
                key_index += 1
            else:
                decrypted_text += char  # Сохраняем пробелы и знаки препинания

        return decrypted_text

    def vigenere_encrypt(self, text, key):
        encrypted_text = ""
        key_repeated = (key * (len(text) // len(key))) + key[:len(text) % len(key)]
        key_index = 0  # Индекс для ключа, чтобы пропускать неалфавитные символы

        for char in text:
            if char in self.__upper_alphabet:
                char_index = self.__upper_alphabet.index(char)
                key_char = key_repeated[key_index % len(key)]
                key_char_index = self.__upper_alphabet.index(key_char.upper())
                encrypted_text += self.__upper_alphabet[(char_index + key_char_index) % len(self.__upper_alphabet)]
                key_index += 1
            elif char in self.__lower_alphabet:
                char_index = self.__lower_alphabet.index(char)
                key_char = key_repeated[key_index % len(key)]
                key_char_index = self.__lower_alphabet.index(key_char.lower())
                encrypted_text += self.__lower_alphabet[(char_index + key_char_index) % len(self.__lower_alphabet)]
                key_index += 1
            else:
                encrypted_text += char  # Сохраняем пробелы и знаки препинания

        return encrypted_text

    def validate_input(self, text, key):
        valid_chars = self.__upper_alphabet + self.__lower_alphabet + " \n.,!?"
        return (all(char in valid_chars for char in text) and
                all(char in self.__upper_alphabet + self.__lower_alphabet for char in key))
