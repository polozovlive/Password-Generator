import random
import tkinter as tk
from tkinter import messagebox

# ===== загрузка словаря =====
def load_words(file_path="words_ru.txt"):
    with open(file_path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

# ===== раскладка RU -> EN =====
ru_to_en = {
    'й': 'q','ц': 'w','у': 'e','к': 'r','е': 't','н': 'y','г': 'u','ш': 'i','щ': 'o','з': 'p',
    'х': '[','ъ': ']',
    'ф': 'a','ы': 's','в': 'd','а': 'f','п': 'g','р': 'h','о': 'j','л': 'k','д': 'l',
    'ж': ';','э': "'",
    'я': 'z','ч': 'x','с': 'c','м': 'v','и': 'b','т': 'n','ь': 'm','б': ',','ю': '.','ё': '`'
}

def convert(text):
    return "".join(ru_to_en.get(c, c) for c in text.lower())

# ===== генерация =====
def generate_password(words):
    chosen_words = random.sample(words, 3)

    parts = []
    for w in chosen_words:
        short = convert(w[:3]).capitalize()
        parts.append(short)

    number = str(random.randint(10, 99))
    symbol = random.choice("!@#$%^&*")

    # 🔀 случайный порядок числа и символа
    tail = [number, symbol]
    random.shuffle(tail)

    password = "".join(parts) + "".join(tail)

    return password, chosen_words


# ===== GUI =====
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("420x250")

        self.words = load_words()

        tk.Label(root, text="Генератор паролей", font=("Arial", 14)).pack(pady=5)

        self.base_label = tk.Label(root, text="Основа: -", fg="blue")
        self.base_label.pack(pady=5)

        self.result = tk.Entry(root, width=40, font=("Arial", 12))
        self.result.pack(pady=10)

        tk.Button(root, text="Сгенерировать", command=self.create_password).pack(pady=5)
        tk.Button(root, text="Скопировать", command=self.copy).pack(pady=5)

    def create_password(self):
        if len(self.words) < 3:
            messagebox.showerror("Ошибка", "Слишком мало слов")
            return

        pwd, base_words = generate_password(self.words)

        self.result.delete(0, tk.END)
        self.result.insert(0, pwd)

        # 🧾 показываем базовые слова
        #self.base_label.config(text="Основа: " + ", ".join(base_words))
        capitalized_words = [w.capitalize() for w in base_words]
        self.base_label.config(text="Основа: " + ", ".join(capitalized_words))

    def copy(self):
        pwd = self.result.get()
        self.root.clipboard_clear()
        self.root.clipboard_append(pwd)
        messagebox.showinfo("OK", "Скопировано")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()