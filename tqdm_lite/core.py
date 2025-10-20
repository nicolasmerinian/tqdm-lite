import sys
import time

class TqdmLite:
    def __init__(self, iterable, bar_length=25, prefix=""):
        self.iterable = iterable
        self.bar_length = bar_length
        self.prefix = prefix
        try:
            self.total = len(self.iterable)
        except TypeError:
            self.total = None
        self.timer = None
    
    def _print_bar(self, progress_ratio, index):
        filled = int(progress_ratio * self.bar_length)
        cursor = "ᗧ" if index % 2 == 0 else "ᱝ"
        bar = " " * filled + cursor + "•" * (self.bar_length - filled)
        elapsed = time.time() - self.timer
        eta = elapsed / index * (self.total - index)
        sys.stdout.write(f"\r{self.prefix.strip()} [{bar}ᗣ] | {progress_ratio * 100:.1f}% | Remaining: {eta:.1f}s")
        sys.stdout.flush()
    
    def __iter__(self):
        self.timer = time.time()
        
        if self.total is not None:
            for i, item in enumerate(self.iterable, start=1):
                yield item
                self._print_bar(i / self.total, i)
        else:
            for i, item in enumerate(self.iterable, start=1):
                yield item
        print()