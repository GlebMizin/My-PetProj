import tkinter as tk
import fnmatch
import os
from pygame import mixer


def window():
    mixer.init()
    canvas = tk.Tk()
    canvas.title("Music Player")
    canvas.geometry("600x800")
    canvas.config(bg='black')
    list_box = tk.Listbox(canvas, fg="cyan", bg="black", width=100, font=('Sunday', 14))
    list_box.pack(padx=15, pady=15)

    pattern = "*.mp3"

    prev_img = tk.PhotoImage(file='prev_img.png')
    stop_img = tk.PhotoImage(file='stop_img.png')
    play_img = tk.PhotoImage(file='play_img.png')
    pause_img = tk.PhotoImage(file='pause_img.png')
    next_img = tk.PhotoImage(file='next_img.png')

    def select():
        label.config(text=list_box.get('anchor'))
        mixer.music.load(root_path + '\\' + list_box.get('anchor'))
        mixer.music.play()

    def stop_sound():
        mixer.music.stop()
        list_box.select_clear('active')

    def next_song():
        next_s = list_box.curselection()
        next_s = next_s[0] + 1
        next_s_name = list_box.get(next_s)
        label.config(text= next_s_name)

        mixer.music.load(root_path + '\\' + next_s_name)
        mixer.music.play()

        list_box.select_clear(0, 'end')
        list_box.activate(next_s)
        list_box.select_set(next_s)

    def prev_song():
        next_s = list_box.curselection()
        next_s = next_s[0] - 1
        next_s_name = list_box.get(next_s)
        label.config(text= next_s_name)

        mixer.music.load(root_path + '\\' + next_s_name)
        mixer.music.play()

        list_box.select_clear(0, 'end')
        list_box.activate(next_s)
        list_box.select_set(next_s)

    def pause_song():
        if pause_button['text'] == 'pause':
            mixer.music.pause()
            pause_button['text'] = 'play'
        else:
            mixer.music.unpause()
            pause_button['text'] = 'pause'

    label = tk.Label(canvas, text='', bg='black', fg='yellow', font=('Sunday', 18))
    label.pack(pady=15)

    top = tk.Frame(canvas, bg='black')
    top.pack(padx=10, pady=5, anchor='center')

    prev_button = tk.Button(canvas, text="Prev", image=prev_img, bg='black', borderwidth=0, command=prev_song)
    prev_button.pack(pady=15, in_=top, side='left')

    stop_button = tk.Button(canvas, text="stop",  image=stop_img, bg='black', borderwidth=0, command=stop_sound)
    stop_button.pack(pady=15, in_=top, side='left')

    play_button = tk.Button(canvas, text="play", image=play_img, bg='black', borderwidth=0, command=select)
    play_button.pack(pady=15, in_=top, side='left')

    pause_button = tk.Button(canvas, text="pause",  image=pause_img, bg='black', borderwidth=0, command=pause_song)
    pause_button.pack(pady=15, in_=top, side='left')

    next_button = tk.Button(canvas, text="next", image=next_img, bg='black', borderwidth=0, command=next_song)
    next_button.pack(pady=15, in_=top, side='left')

    for root, dirs, files in os.walk(root_path):
        for filename in fnmatch.filter(files, pattern):
            list_box.insert('end', filename)

    canvas.mainloop()


if __name__ == '__main__':
    root_path = input("Введите путь к папке с музыкой: ")
    window()
