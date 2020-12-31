#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import realurl
import record

from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self, text='填入分享链接')
        self.nameInput.pack()
        self.alertButton = Button(self, text='开始录制', command=self.record)
        self.alertButton.pack()

    def record(self):
        share_link = self.nameInput.get()
        print(share_link)
        live = realurl.DouYin(share_link)
        record.exec_ffmpeg(live.get_real_url()[0])

