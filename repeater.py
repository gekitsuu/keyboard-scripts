from threading import Timer

class Repeater():
    def __init__(self, function, args, interval):
        def repeating_function():
            Timer(interval, function, args=args)
        self.timer =


if __name__ == "__main__":
    def foo(message):
        print(message)
    timers = []
    timers.append(Repeater(foo, ['foo'], 3).timer.start())
