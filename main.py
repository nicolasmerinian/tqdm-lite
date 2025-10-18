import sys
import time

def tqdm_lite(iterable):
    total = len(iterable)
    
    for i, item in enumerate(iterable):
        percent = i / total * 100
        progress = "#" * int(percent)
        
        sys.stdout.write(f"\r{progress}")
        sys.stdout.flush()

        yield item
    
    
def main():
    array = [x ** 2 for x in range(10)]
    
    for _ in tqdm_lite(array):
        time.sleep(0.15)



if __name__ == "__main__":
    main()