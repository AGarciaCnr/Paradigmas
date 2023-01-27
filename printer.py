from rx.core import observer

class Printer(observer.Observer):
    def on_next(self, value):
        print("("+ value[0] + ") - " + value[1] + ": " + value[2] + " (" + value[3] + ")")

    def on_error(self, error):
        print("Error: {0}".format(error))

    def on_completed(self):
        print("Done!")