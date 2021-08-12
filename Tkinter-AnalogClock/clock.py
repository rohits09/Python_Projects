import tkinter as tk
import time, math


win = tk.Tk()
win.title("Analog Clock")
win.geometry("400x400")

def update():
    hr = int(time.strftime("%H"))
    min = int(time.strftime("%M"))
    sec = int(time.strftime("%S"))
    
    hour_x = center_x + hour_hand_len * math.sin(math.radians(hr * 30))
    hour_y = -1 * hour_hand_len * math.cos(math.radians(hr * 30)) + center_y 
    canvas.coords(hour_hand, center_x, center_y, hour_x, hour_y)

    minute_x = center_x + min_hand_len * math.sin(math.radians(min * 6))
    minute_y = -1 * min_hand_len * math.cos(math.radians(min * 6)) + center_y  
    canvas.coords(minute_hand, center_x, center_y, minute_x, minute_y)

    second_x = center_x + sec_hand_len * math.sin(math.radians(sec * 6))
    second_y = -1 * sec_hand_len * math.cos(math.radians(sec * 6)) + center_y 
    canvas.coords(second_hand, center_x, center_y, second_x, second_y)

    win.after(1000, update)

canvas = tk.Canvas(win, width=400, height=400, bg="black")
canvas.pack(expand=True, fill="both")

clock = tk.PhotoImage(file="clock.png")
canvas.create_image(200, 200, image=clock)

center_x = 200
center_y = 200
hour_hand_len = 60
min_hand_len = 80
sec_hand_len = 95

second_hand = canvas.create_line(200, 200, 200 + sec_hand_len, 200 + sec_hand_len, width=1.3, fill="red")
minute_hand = canvas.create_line(200, 200, 200 + min_hand_len, 200 + min_hand_len, width=1.5, fill="green")
hour_hand = canvas.create_line(200, 200, 200 + hour_hand_len, 200 + hour_hand_len, width=1.5, fill="blue")

update()

win.mainloop()