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
        self.fillShareLinkLabel = Label(self, text='填入分享链接')
        self.fillShareLinkLabel.grid(row=0, column=1)
        self.fillShareLink = Entry(self, text='', width=40)
        self.fillShareLink.grid(row=0,column=0)
        self.showrealurlLabel = Entry(self, text='', width=40)
        self.showrealurlLabel.grid(row=1,column=0)
        self.getrealurlButton = Button(self, text='提取录制链接', command=self.getrealurl)
        self.getrealurlButton.grid(row=1,column=1)
        self.recordButton = Button(self, text='开始录制', command=self.record)
        self.recordButton.grid(row=2, column=1)

    def record(self):
        share_link = self.fillShareLink.get()
        live = realurl.DouYin(share_link)
        ctx = record.Resource()
        record.record(live.get_real_url()[1],ctx)

    def getrealurl(self):
        share_link = self.fillShareLink.get()
        if share_link == '' or share_link == NONE:
            self.showrealurlLabel.insert(0, "填入分享链接处不可为空")
        else:
            live = realurl.DouYin(share_link)
            self.showrealurlLabel.insert(0, live.get_real_url()[0])

