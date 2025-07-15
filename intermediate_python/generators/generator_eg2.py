import sys 
from typing import Generator


def read(path: str) -> Generator[str, None, str]:

    with open(path, 'r') as file:

        for line in file:
            yield line.strip()

    return 'This is the end of the file!!!!'


def main() -> None:

    reader: Generator[str, None, str] = read("sample3.txt")
    input("Press ENTER to get a new line of the file.....")


    while True:

        try:
            print(next(reader))
        
        except StopIteration as e:
            print('StopIteration:', e.value)
            sys.exit()

        input()


if __name__  == '__main__':
    main()