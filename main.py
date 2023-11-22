import tkinter as tk
import pyautogui as pyautogui
import time


def getColorOnMouse():
    time.sleep(3)
    positionx = pyautogui.position()[0]
    positiony = pyautogui.position()[1]
    red = pyautogui.pixel(positionx, positiony)[0]
    green = pyautogui.pixel(positionx, positiony)[1]
    blue = pyautogui.pixel(positionx, positiony)[2]

    #debug
    print(red, green, blue)

    red_slider.set(red)
    green_slider.set(green)
    blue_slider.set(blue)
    color_label.config(bg=f'#{red:02X}{green:02X}{blue:02X}')
    color_label_rgbval.config(text=f'#{red:02X}{green:02X}{blue:02X}')


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

button = tk.Button(root, text="get Pixel Color", command=getColorOnMouse)
button.pack(padx=20, pady=20)

red_slider.bind("<Motion>", lambda event: update_values())
green_slider.bind("<Motion>", lambda event: update_values())
blue_slider.bind("<Motion>", lambda event: update_values())

root.mainloop()
