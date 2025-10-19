import sys
import time

def tqdm_lite(iterable):
    total = len(iterable)
    bar_length = 25
    
    for i, item in enumerate(iterable):
        percent = i / total
        progress = int(percent * bar_length)
        bar = "#" * progress + '-' * (bar_length - progress)
        sys.stdout.write(f"\r{bar} | {percent*100:.1f}%")
        sys.stdout.flush()

        yield item
    
    bar = "#" * bar_length
    sys.stdout.write(f"\r{bar} | 100.0%")
    sys.stdout.flush()
    

def main():
    array = [x ** 2 for x in range(15)]
    
    for _ in tqdm_lite(array):
        time.sleep(0.2)



if __name__ == "__main__":
    main()