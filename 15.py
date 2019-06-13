#!/usr/bin/python2
# coding: utf-8

from Tkinter import *
from random import shuffle
from functools import partial

class Game15:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("15")
        self.digit = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        self.victory = False
        #Кнопки
        self.btns = []
        for r in range(4):
            for c in range(4):
                btn = Button(self.tk, text='*', width=7, height=4,
                                font="16", 
                                 command=partial(self.btn_game, r, c))
                btn.grid(column = c, row = r)
                self.btns.append(btn)
        mn = Menu(self.tk)
        self.tk.config(menu=mn)
        mn.add_command(label="Перемешать", command=self.shuffle)
        mn.add_command(label="Закрыть", command=self.close)
        
    def mainloop(self):
        self.tk.mainloop()
    
    def close(self):
        self.tk.destroy()
    
    def shuffle(self):
        shuffle(self.digit)
        self.victory = False
        self.tk.title("15")
        for i in range(len(self.digit)):
            btn = self.btns[i]
            if self.digit[i] > 0:
                btn["text"] = self.digit[i]
                btn["relief"] = "groove"
            else:
                btn["text"] = ""
                btn["relief"] = "sunken"
    
    def btn_game(self, row, col):
        if self.victory:
            return
        pos = row * 4 + col
        btn = self.btns[pos]
        if btn["relief"] == "sunken":
            return
        if row > 0:
            sosed = (row - 1) * 4 + col
            sbtn = self.btns[sosed]
            if sbtn["relief"] == "sunken":
                sbtn["relief"] = "groove"
                sbtn["text"] = btn["text"]
                btn["relief"] = "sunken"
                btn["text"] = ""
        if row < 3:
            sosed = (row + 1) * 4 + col
            sbtn = self.btns[sosed]
            if sbtn["relief"] == "sunken":
                sbtn["relief"] = "groove"
                sbtn["text"] = btn["text"]
                btn["relief"] = "sunken"
                btn["text"] = ""
        if col > 0:
            sosed = row * 4 + col - 1
            sbtn = self.btns[sosed]
            if sbtn["relief"] == "sunken":
                sbtn["relief"] = "groove"
                sbtn["text"] = btn["text"]
                btn["relief"] = "sunken"
                btn["text"] = ""
        if col < 3:
            sosed = row * 4 + col + 1
            sbtn = self.btns[sosed]
            if sbtn["relief"] == "sunken":
                sbtn["relief"] = "groove"
                sbtn["text"] = btn["text"]
                btn["relief"] = "sunken"
                btn["text"] = ""
        if self.check_game():
            print "Victory"
            self.victory = True
            self.tk.title("Победа !!!")
    
    def check_game(self):
        if self.btns[15]["relief"] != "sunken":
            return False
        for r in range(4):
            for c in range(4):
                num = r * 4 + c
                if num == 0 or num == 15:
                    continue
                btn1 = self.btns[num-1]["text"]
                btn2 = self.btns[num]["text"]
                if int(btn2) - int(btn1) != 1:
                    return False
        return True

if __name__ == "__main__":
    g = Game15()
    g.mainloop()
