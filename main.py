import sys
import time

class TqdmLite:
    def __init__(self, iterable, bar_length=25):
        self.iterable = iterable
        self.bar_length = bar_length
        try:
            self.total = len(self.iterable)
        except TypeError:
            self.total = None
    
    def _print_bar(self, progress_ratio):
        filled = int(progress_ratio * self.bar_length)
        bar = "#" * filled + "-" * (self.bar_length - filled)
        sys.stdout.write(f"\r{bar} | {progress_ratio * 100:.1f}%")
        sys.stdout.flush()
    
    def __iter__(self):
        if self.total is not None:
            for i, item in enumerate(self.iterable, start=1):
                yield item
                self._print_bar(i / self.total)
        else:
            for i, item in enumerate(self.iterable, start=1):
                yield item
        print()
        

def main():
    array = [x ** 2 for x in range(15)]

    for _ in TqdmLite(array):
        time.sleep(0.2)


if __name__ == "__main__":
    main()