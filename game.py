import tkinter as tk
import random

# Inisialisasi jendela Tkinter
window = tk.Tk()
window.title("Catch the Ball Game")
window.geometry("400x600")

# Inisialisasi kanvas
canvas = tk.Canvas(window, width=400, height=600, bg="lightblue")
canvas.pack()

# Variabel untuk pemain, bola, dan skor
player = canvas.create_rectangle(180, 550, 220, 570, fill="blue")
ball = canvas.create_oval(180, 0, 220, 20, fill="red")
score = 0
score_text = canvas.create_text(50, 30, text="Score: 0", font=("Arial", 16))

# Kecepatan bola
ball_speed = 5

# Fungsi untuk menggerakkan pemain ke kiri
def move_left(event):
    x1, _, x2, _ = canvas.coords(player)
    if x1 > 0:
        canvas.move(player, -20, 0)

# Fungsi untuk menggerakkan pemain ke kanan
def move_right(event):
    _, _, x2, _ = canvas.coords(player)
    if x2 < 400:
        canvas.move(player, 20, 0)

# Fungsi utama untuk menurunkan bola dan memeriksa tabrakan
def drop_ball():
    global score, ball_speed
    canvas.move(ball, 0, ball_speed)
    ball_pos = canvas.coords(ball)
    player_pos = canvas.coords(player)

    # Cek tabrakan bola dengan pemain
    if (player_pos[0] < ball_pos[2] and player_pos[2] > ball_pos[0] and
        player_pos[1] < ball_pos[3] and player_pos[3] > ball_pos[1]):
        score += 1
        canvas.itemconfig(score_text, text="Score: " + str(score))
        reset_ball()

    # Jika bola jatuh ke dasar layar, reset posisi bola
    elif ball_pos[3] >= 600:
        reset_ball()

    # Panggil fungsi ini lagi setelah 50ms
    window.after(50, drop_ball)

# Fungsi untuk me-reset posisi bola ke atas dengan posisi acak
def reset_ball():
    x_position = random.randint(20, 380)
    canvas.coords(ball, x_position, 0, x_position + 40, 20)

# Bind tombol kiri dan kanan untuk menggerakkan pemain
window.bind("<Left>", move_left)
window.bind("<Right>", move_right)

# Mulai game
drop_ball()
window.mainloop()
