import gui
from tkinter import *
if __name__ == '__main__':
    root = Tk()
    root.geometry("400x100+500+200")

    app = gui.Application(root)
    # 设置窗口标题:
    app.master.title('简陋dy直播录制gui v0.1.1')
    # 主消息循环:
    app.mainloop()
