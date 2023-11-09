import tkinter as tk
import pyautogui



#def get_pixel_color(x, y):
 #   color = pyautogui.pixel(x, y)
  #  return color


def update_values():
    red_value = red_slider.get()
    green_value = green_slider.get()
    blue_value = blue_slider.get()
    color_label.config(bg=f'#{red_value:02X}{green_value:02X}{blue_value:02X}')
    color_label_rgbval.config(text=f'#{red_value:02X}{green_value:02X}{blue_value:02X}')

root = tk.Tk()
root.title("RGB Schieberegler")

red_slider = tk.Scale(root, from_=0, to=255, orient="horizontal", label="Rot")
red_slider.pack()

green_slider = tk.Scale(root, from_=0, to=255, orient="horizontal", label="Grün")
green_slider.pack()

blue_slider = tk.Scale(root, from_=0, to=255, orient="horizontal", label="Blau")
blue_slider.pack()

red_slider.set(0)
green_slider.set(0)
blue_slider.set(0)

color_label = tk.Label(root, text="Farbvorschau", bg="#000000", fg="white", width=20)
color_label.pack()
color_label_rgbval = tk.Label(root, bg="#FFF", fg="black", width=20)
color_label_rgbval.pack()

red_slider.bind("<Motion>", lambda event: update_values())
green_slider.bind("<Motion>", lambda event: update_values())
blue_slider.bind("<Motion>", lambda event: update_values())


root.mainloop()