# -*- coding = utf-8 -*-
# @Time : 2022/4/9
# @Author :小吴
# @File :Private_signer.py
# @Software :PyCharm
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk
import requests
import re
# http://www.uustv.com/
window = Tk()

window.geometry('535x345')
window.resizable(0, 0)
window.title('私人签名器')
window.iconbitmap('D:\pics\icon.ico')

Label(window, text='姓名：', font=('华文行楷', 20)).place(x=20, y=20)
name_entry = Entry(window, font=('华文行楷', 20))
name_entry.place(x=120, y=20)
Label(window, text='字体：', font=('华文行楷', 20)).place(x=20, y=80)
font_box = ttk.Combobox(window, width=10, height=1, font=('华文行楷', 20))
font_box.place(x=120, y=80)
font_box['value'] = ('个性签', '连笔签', '潇洒签', '草体签', '合文签', '商务签', '可爱签')
font_box.current(0)
font = {
    '个性签': 'jfcs.ttf',
    '连笔签': 'qmt.ttf',
    '潇洒签': 'bzcs.ttf',
    '草体签': 'lfc.ttf',
    '合文签': 'haku.ttf',
    '商务签': 'zql.ttf',
    '可爱签': 'yqk.ttf'
}


def pc_image():
    name = name_entry.get()
    name = name.strip()
    if name == '':
        messagebox.showwarning('警告', message='请输入你的姓名')
    else:
        fonts = font[font_box.get()]

        data = {
            "word": name,
            "sizes": "60",
            "fonts": fonts,
            "fontcolor": "#000000"
        }

        url = 'http://www.uustv.com/'
        result = requests.post(url, data)
        result.encoding = 'utf-8'
        html = result.text

        reg = f'<div class="tu">﻿<img src="(.*?)"/></div>'
        img_path = re.findall(reg, html)
        img_adress = url + img_path[0]
        image = requests.get(img_adress).content

        with open('{}.gif'.format(name), 'wb') as f:
            f.write(image)

        bm = ImageTk.PhotoImage(file='{}.gif'.format(name))
        label_image = Label(window, image=bm)
        label_image.bm = bm
        label_image.place(x=0, y=140)


Button(window, width=10, height=3, text='生成签名', font=('华文行楷', 20), command=pc_image).place(x=380, y=20)

bm = ImageTk.PhotoImage(file='./image/空白.gif')
label_image = Label(window, image=bm)
label_image.bm = bm
label_image.place(x=0, y=140)

window.mainloop()