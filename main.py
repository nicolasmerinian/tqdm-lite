import sys
import time

def tqdm_lite(iterable):
    total = len(iterable)
    bar_length = 20
    
    for i, item in enumerate(iterable):
        percent = i / total
        progress = int(percent * bar_length)
        str = "#" * progress + '-' * (bar_length - progress)
        sys.stdout.write(f"\r{str}")
        sys.stdout.flush()

        yield item
    
    str = "#" * bar_length
    sys.stdout.write(f"\r{str}")
    sys.stdout.flush()
    

def main():
    array = [x ** 2 for x in range(10)]
    
    for _ in tqdm_lite(array):
        time.sleep(0.2)



if __name__ == "__main__":
    main()