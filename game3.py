import tkinter as tk
import random

# Inisialisasi jendela Tkinter
window = tk.Tk()
window.title("Baseball Swing Game")
window.geometry("600x400")

# Inisialisasi kanvas
canvas = tk.Canvas(window, width=600, height=400, bg="lightblue")
canvas.pack()

# Variabel untuk bola, pemukul, dan skor
ball = canvas.create_oval(290, 10, 310, 30, fill="red")
bat = canvas.create_rectangle(270, 350, 330, 360, fill="brown")
score = 0
score_text = canvas.create_text(50, 30, text="Score: 0", font=("Arial", 16))

# Kecepatan bola
ball_speed_x = random.choice([-4, 4])
ball_speed_y = 4

# Fungsi untuk menggerakkan pemukul (bat)
def move_bat_left(event):
    x1, _, x2, _ = canvas.coords(bat)
    if x1 > 0:
        canvas.move(bat, -20, 0)

def move_bat_right(event):
    _, _, x2, _ = canvas.coords(bat)
    if x2 < 600:
        canvas.move(bat, 20, 0)

# Fungsi utama untuk menggerakkan bola dan memeriksa tabrakan
def move_ball():
    global score, ball_speed_x, ball_speed_y
    canvas.move(ball, ball_speed_x, ball_speed_y)
    ball_pos = canvas.coords(ball)
    bat_pos = canvas.coords(bat)

    # Cek tabrakan bola dengan dinding
    if ball_pos[0] <= 0 or ball_pos[2] >= 600:
        ball_speed_x = -ball_speed_x
    if ball_pos[1] <= 0:
        ball_speed_y = -ball_speed_y

    # Cek tabrakan bola dengan pemukul
    if (bat_pos[0] < ball_pos[2] and bat_pos[2] > ball_pos[0] and
        bat_pos[1] < ball_pos[3] and bat_pos[3] > ball_pos[1]):
        ball_speed_y = -ball_speed_y
        score += 1
        canvas.itemconfig(score_text, text="Score: " + str(score))

    # Reset bola jika jatuh ke dasar
    if ball_pos[3] >= 400:
        reset_ball()

    # Panggil fungsi ini lagi setelah 50ms
    window.after(50, move_ball)

# Fungsi untuk me-reset posisi bola ke atas dengan arah acak
def reset_ball():
    global ball_speed_x, ball_speed_y
    x_position = random.randint(20, 580)
    canvas.coords(ball, x_position, 10, x_position + 20, 30)
    ball_speed_x = random.choice([-4, 4])
    ball_speed_y = 4

# Bind tombol kiri dan kanan untuk menggerakkan pemukul
window.bind("<Left>", move_bat_left)
window.bind("<Right>", move_bat_right)

# Mulai gerakan bola
move_ball()
window.mainloop()
