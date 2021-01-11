#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import realurl
import OpenCRS

from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.fill_share_link_label = Label(self, text='填入分享链接')
        self.fill_share_link_label.grid(row=0, column=1)
        self.fill_share_link_textbox = Entry(self, text='', width=40)
        self.fill_share_link_textbox.grid(row=0, column=0)
        self.show_real_url_Label = Entry(self, text='', width=40)
        self.show_real_url_Label.grid(row=1, column=0)
        self.get_real_url_button = Button(self, text='提取录制链接', command=self.getrealurl)
        self.get_real_url_button.grid(row=1, column=1)
        self.record_button = Button(self, text='开始录制', command=self.record)
        self.record_button.grid(row=2, column=1)

    def record(self):
        share_link = self.fill_share_link_textbox.get()
        live = realurl.Douyin(share_link)
        OpenCRS.record(live.get_real_url()[1])

    def getrealurl(self):
        share_link = self.fill_share_link_textbox.get()
        if share_link == '' or share_link == NONE:
            self.show_real_url_Label.insert(0, "填入分享链接处不可为空")
        else:
            live = realurl.Douyin(share_link)
            self.show_real_url_Label.insert(0, live.get_real_url()[1])

