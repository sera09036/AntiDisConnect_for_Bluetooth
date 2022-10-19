import tkinter as tki
from tkinter import messagebox
import threading
import time
import winsound
import sys
import os

class Application(tki.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.pack_propagate(0)
        self.create_menu()
        self.widgets()

    def create_menu(self):
        menuber = tki.Menu(self.master)
        root.config(menu=menuber)
        menu_file = tki.Menu(menuber, tearoff=False)
        menu_file.add_command(label='終了', command=self.master.destroy)
        menuber.add_cascade(label='File', menu=menu_file)

    def widgets(self):
        #frame = tki.Frame(self.master)
        frame = tki.LabelFrame(self.master,text='Welcome', foreground='LightGreen', bg='grey25')
        f0 = tki.Frame(frame)
        f1 = tki.Frame(frame)
        frame.configure(bg='grey25')

        f0.configure(bg='grey25')
        f1.configure(bg='grey25')

        self.test_btn = tki.Button(f1)
        self.test_btn['text'] = '開始'
        self.test_btn['foreground'] = 'green'
        self.test_btn['width'] = 35
        self.test_btn['height'] = 3
        self.test_btn['command'] = self.run_th
        self.test_btn.pack(fill = 'x', padx=10, pady= 20, side = 'left')

        self.stop_btn = tki.Button(f0)
        self.stop_btn['text'] = 'STOP'
        self.stop_btn['foreground'] = 'green'
        self.stop_btn['state'] = tki.DISABLED
        self.stop_btn['width'] = 35
        self.stop_btn['height'] = 3
        self.stop_btn['command'] = self.out_func
        self.stop_btn.pack(fill = 'x', padx=10, pady= 20, side = 'left')

        f1.pack()
        f0.pack()
        frame.pack()

    def dis(self):
        self.test_btn['text'] = '実行中...'
        self.test_btn['state'] = tki.DISABLED
        self.stop_btn['state'] = tki.NORMAL
        while True:
            if self.test_btn['state'] == 'disabled':
                winsound.Beep(20000, 1000)
                time.sleep(150)
            else:
                break

    def run_th(self):
        thread = threading.Thread(target=self.dis)
        thread.setDaemon(True)
        thread.start()

    def out_func(self):
        if self.test_btn['state'] == 'disabled':
            self.test_btn['text'] = '開始'
            self.test_btn['state'] = tki.NORMAL
            self.stop_btn['state'] = tki.DISABLED
        else:
            messagebox.showwarning('警告！', '開始されていません。')


if __name__ == '__main__':
    root = tki.Tk()
    root.title('AntiDisConnect')
    root.geometry('364x237')
    root.configure(bg='grey25')
    #pythonで実行する場合以下をアンコメント！
    #root.iconbitmap(default='favicon.ico')

    #ビルドする場合以下をアンコメント！
    root.iconbitmap(default=os.path.join(sys._MEIPASS,'favicon.ico'))
    app = Application(master=root)
    app.mainloop()