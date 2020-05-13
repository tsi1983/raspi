import sys
import os
import numpy as np
import tkinter as tk

import tkinter.ttk as ttk
from PIL import Image, ImageTk
from tkinter import messagebox as tkMessageBox
from tkinter import filedialog as tkFileDialog

# originated from https://qiita.com/nanako_ut/items/b5393363b9e21d6342ea

# アプリケーション（GUI）クラス
class Application(tk.Frame):
    DEBUG_LOG = True
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # ペインウィンドウ
        # PanedWindow
        ##  orient : 配置（vertical or horizontal）
        ##  bg : 枠線の色
        # pack
        ##  expand ：可変（True or False(固定)
        ##  fill : スペースが空いている場合の動き（tk.BOTH　縦横に広がる）
        ##  side ：　配置する際にどの方向からつめていくか（side or top ・・・）
        pw_main = tk.PanedWindow(self.master, orient='horizontal')
        pw_main.pack(expand=True, fill = tk.BOTH, side="left")
    
        pw_left = tk.PanedWindow(pw_main, bg="cyan", orient='vertical')
        pw_main.add(pw_left)
        pw_right = tk.PanedWindow(pw_main, bg="yellow", orient='vertical')
        pw_main.add(pw_right)

# 実行
root = tk.Tk()        
myapp = Application(master=root)
myapp.master.title("My Application") # タイトル
myapp.master.geometry("1000x500") # ウィンドウの幅と高さピクセル単位で指定（width x height）

myapp.mainloop()