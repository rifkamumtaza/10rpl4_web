import tkinter as tk
import random

# Inisialisasi jendela Tkinter
window = tk.Tk()
window.title("Adventure Game")
window.geometry("500x500")

# Inisialisasi kanvas
canvas = tk.Canvas(window, width=500, height=500, bg="lightgreen")
canvas.pack()

# Variabel untuk karakter utama, objek untuk dikumpulkan, dan skor
character = canvas.create_rectangle(230, 230, 270, 270, fill="blue")
items = []
score = 0
score_text = canvas.create_text(50, 30, text="Score: 0", font=("Arial", 16))

# Fungsi untuk membuat item di lokasi acak
def spawn_item():
    x = random.randint(20, 480)
    y = random.randint(20, 480)
    item = canvas.create_oval(x, y, x + 20, y + 20, fill="gold")
    items.append(item)

# Fungsi untuk menggerakkan karakter
def move_character(dx, dy):
    global score
    canvas.move(character, dx, dy)
    char_pos = canvas.coords(character)

    # Cek apakah karakter menyentuh item
    for item in items:
        item_pos = canvas.coords(item)
        if (char_pos[0] < item_pos[2] and char_pos[2] > item_pos[0] and
            char_pos[1] < item_pos[3] and char_pos[3] > item_pos[1]):
            # Hapus item jika tersentuh
            canvas.delete(item)
            items.remove(item)
            score += 1
            canvas.itemconfig(score_text, text="Score: " + str(score))

# Fungsi untuk bind tombol panah untuk gerakan
def move_left(event): move_character(-10, 0)
def move_right(event): move_character(10, 0)
def move_up(event): move_character(0, -10)
def move_down(event): move_character(0, 10)

# Spawn beberapa item di lokasi acak
for _ in range(5):
    spawn_item()

# Bind tombol gerakan
window.bind("<Left>", move_left)
window.bind("<Right>", move_right)
window.bind("<Up>", move_up)
window.bind("<Down>", move_down)

# Jalankan game
window.mainloop()
