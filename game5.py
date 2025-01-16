import tkinter as tk
import random

class TebakAngkaGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Game Tebak Angka")
        
        # Angka acak yang dipilih komputer
        self.random_number = random.randint(1, 100)
        self.guess_count = 0
        
        # Judul
        self.title_label = tk.Label(root, text="Selamat datang di Game Tebak Angka!", font=("Arial", 14))
        self.title_label.pack(pady=10)
        
        # Petunjuk
        self.instructions_label = tk.Label(root, text="Tebak angka antara 1 dan 100:", font=("Arial", 12))
        self.instructions_label.pack()
        
        # Input untuk tebakan pemain
        self.entry = tk.Entry(root, font=("Arial", 12))
        self.entry.pack(pady=5)
        
        # Tombol Tebak
        self.guess_button = tk.Button(root, text="Tebak", command=self.check_guess, font=("Arial", 12))
        self.guess_button.pack(pady=5)
        
        # Label hasil tebakan
        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=5)
        
        # Skor
        self.score_label = tk.Label(root, text="Tebakan: 0", font=("Arial", 12))
        self.score_label.pack()

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.guess_count += 1
            self.entry.delete(0, tk.END)
            
            if guess < self.random_number:
                self.result_label.config(text="Terlalu Rendah!")
            elif guess > self.random_number:
                self.result_label.config(text="Terlalu Tinggi!")
            else:
                self.result_label.config(text="Selamat! Anda menebak dengan benar.")
                self.guess_button.config(state=tk.DISABLED)
            
            self.score_label.config(text=f"Tebakan: {self.guess_count}")
        
        except ValueError:
            self.result_label.config(text="Masukkan angka yang valid!")

# Jalankan game
root = tk.Tk()
game = TebakAngkaGame(root)
root.mainloop()
