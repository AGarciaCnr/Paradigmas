from tkinter import *
from tkinter.ttk import Combobox
from functools import partial


class App:
    def __init__(self):
        self.__text = ""
        self.window = Tk()
        self.window.title = 'Aplicación Gráfica!'
        # window.maxsize(width=300, height=200)
        # window.minsize(width=100, height=120)
        # window.geometry('800x400')

        self.display = Label(text='0', font=('Arial Bold', 36))
        self.display.grid(column=0, row=0)

        self.button7 = Button(text='7', command=partial(self.pressedButton, 7), pady=15, padx=20)
        self.button7.grid(column=0, row=1)
        self.button8 = Button(text='8', command=partial(self.pressedButton, 8), pady=15, padx=20)
        self.button8.grid(column=1, row=1)
        self.button9 = Button(text='9', command=partial(self.pressedButton, 9), pady=15, padx=20)
        self.button9.grid(column=2, row=1)
        self.buttonPlus = Button(text='+', command=partial(self.pressedButton, '+'), pady=15, padx=20)
        self.buttonPlus.grid(column=3, row=1)

        self.button4 = Button(text='4', command=partial(self.pressedButton, 4), pady=15, padx=20)
        self.button4.grid(column=0, row=2)
        self.button5 = Button(text='5', command=partial(self.pressedButton, 5), pady=15, padx=20)
        self.button5.grid(column=1, row=2)
        self.button6 = Button(text='6', command=partial(self.pressedButton, 6), pady=15, padx=20)
        self.button6.grid(column=2, row=2)
        self.buttonSubstract = Button(text='-', command=partial(self.pressedButton, '-'), pady=15, padx=20)
        self.buttonSubstract.grid(column=3, row=2)

        self.button1 = Button(text='1', command=partial(self.pressedButton, 1), pady=15, padx=20)
        self.button1.grid(column=0, row=3)
        self.button2 = Button(text='2', command=partial(self.pressedButton, 2), pady=15, padx=20)
        self.button2.grid(column=1, row=3)
        self.button3 = Button(text='3', command=partial(self.pressedButton, 3), pady=15, padx=20)
        self.button3.grid(column=2, row=3)
        self.buttonTimes = Button(text='*', command=partial(self.pressedButton, '*'), pady=15, padx=20)
        self.buttonTimes.grid(column=3, row=3)

        self.button0 = Button(text='0', command=partial(self.pressedButton, 0), pady=15, padx=20)
        self.button0.grid(column=0, row=4)
        self.buttonDivide = Button(text='/', command=partial(self.pressedButton, '/'), pady=15, padx=20)
        self.buttonDivide.grid(column=1, row=4)
        self.buttonExec = Button(text='=', command=partial(self.pressedButton, '='), pady=15, padx=46)
        self.buttonExec.grid(column=2, row=4, columnspan=2)

        self.window.mainloop()

    def pressedButton(self, val):
        if val == '=':
            self.display.configure(text=eval(self.__text))
            self.__text = ""
        else:
            self.__text += str(val)
            self.display.configure(text=self.__text)

if __name__ == '__main__':
    App()
