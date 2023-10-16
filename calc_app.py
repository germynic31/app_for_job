import tkinter as tk
import pyperclip


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("caclulate2000")
        self.master.geometry("400x200")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.number_label = tk.Label(self, text="Введите число:",
                                     font=('Arial', 14))
        self.number_label.grid(row=0, column=0, padx=10, pady=10)

        self.number_entry = tk.Entry(self, font=('Arial', 20))
        self.number_entry.grid(row=1, column=0, padx=10, pady=10)

        self.submit_button = tk.Button(self, text="Добавить 250 и скопировать",
                                       font=('Arial', 14),
                                       command=lambda: self.add_and_copy(None))
        self.submit_button.grid(row=2, column=0, padx=10, pady=10)

        self.number_entry.unbind("<Control-v>")

        self.number_entry.bind("<Return>", self.add_and_copy)

    def add_and_copy(self, event):
        try:
            input_number = str(self.number_entry.get()).replace(' ', '').replace('	', '')
            result = int(input_number) + 250
            while result % 50 != 0:
                result += 1
            pyperclip.copy(result)
            self.submit_button.config(text="Скопировано!")
            self.number_entry.delete(0, tk.END)
        except ValueError:
            self.submit_button.config(text="Ошибка, введите число!")

    def paste_from_clipboard(self, event):
        clipboard_text = self.master.clipboard_get()
        self.number_entry.insert(tk.END, clipboard_text)


root = tk.Tk()
app = Application(master=root)
app.mainloop()
