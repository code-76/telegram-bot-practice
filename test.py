from threading import Timer
import time

class TestTime(object):

    def __init__(self, run=True) -> None:
        super().__init__()
        self.run = run

    def hello():
        print('hello world!')

    def stop(self):
        self.run = False

    def infinite(self):
        while self.run:
            print("Running.")
            time.sleep(1)

tt = TestTime()
t = Timer(10.0, tt.stop)
t.start()

tt.infinite()