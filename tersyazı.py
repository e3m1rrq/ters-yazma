import tkinter as tk

def create_black_window(yazı):
    window = tk.Tk()
    window.title("Ters Yazıcı")
    window.geometry("400x300")
    window.configure(bg="black")

    label = tk.Label(window, text=yazı, font=("Helvetica", 30), bg="black", fg="white")
    label.pack(expand=True)

    label_reversed = tk.Label(window, text=yazı[::-1], font=("Helvetica", 30), bg="black", fg="white")
    label_reversed.pack(expand=True)

    window.mainloop()

if __name__ == "__main__":
    yazı = input("Bir yazı girin: ")
    create_black_window(yazı)
    create_black_window(yazı[::-1])
