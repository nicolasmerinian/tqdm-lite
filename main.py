def tqdm_lite(iterable):    
    for i, item in enumerate(iterable):
        yield item


def main():
    array = [x ** 2 for x in range(10)]
    
    for i in tqdm_lite(array):
        print(i)


if __name__ == "__main__":
    main()