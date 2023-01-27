from rx import create
from rx.core import Observer

class Printer(Observer):
    def on_next(self, v):
        print(v)

def Observer_teclado(observer, scheduler):
    while 1:
        msg = input('introduce un mensaje: ')
        if msg:
            observer.on_next(msg)
        else:
            observer.on_completed()
            return

observable = create(Observer_teclado)
observable.subscribe(Printer())