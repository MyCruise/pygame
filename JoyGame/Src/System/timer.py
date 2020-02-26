from time import time


class Timer:
    def __init__(self):
        self.start = time()

    def set_timer(self):
        self.start = time()

    def elapse(self):
        return time() - self.start

    def num2time(self, num):
        num = int(num)
        second = num % 60
        num //= 60
        minute = num % 60
        num //= 60
        hour = num % 24
        if hour > 24:
            hour = 0
        return "%02d: %02d: %02d" % (hour, minute, second)


if __name__ == '__main__':
    timer = Timer()
    print(timer.elapse())
