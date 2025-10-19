import sys
import time

def tqdm_lite(iterable):
    def print_bar(progress):
        filled = int(progress * bar_length)
        bar = "#" * filled + "-" * (bar_length - filled)
        sys.stdout.write(f"\r{bar} | {progress * 100:.1f}%")
        sys.stdout.flush()
    
    try:
        total = len(iterable)
    except TypeError:
        total = None

    bar_length = 25
    
    if total is not None:
        for i, item in enumerate(iterable, start=1):
            yield item
            print_bar(i / total)
    else:
        for i, item in enumerate(iterable, start=1):
            yield item
    print()
    

def main():
    array = [x ** 2 for x in range(15)]
    
    for _ in tqdm_lite(array):
        time.sleep(0.2)


if __name__ == "__main__":
    main()