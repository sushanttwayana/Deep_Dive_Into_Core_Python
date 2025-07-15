#### Example 1  ;
from typing import Generator

def fibonacci_generator() -> Generator[int, None, None]:

    """
        Generates fibonaacci series upto 'n' numbers specified in each click.

        This method uses generator to generate and also is more memoery efficient than creating a list.

        In Gnerator[int, None, None] :

        >>>> first value spevifies the type that we are going to yeild
        >>>> second value specidies what value will be passed to the Generator 
        >>>> third value spcifies what value will be returned by the generator 
        
    """

    a, b = 0, 1

    while True:
        yield a

        a, b = b, (a + b)


def main() -> None :
    
    fib_gen : Generator[int, None, None] = fibonacci_generator()

    n: int = 10
    line_break: str = '-' * 25

    while True:
        input(f"Tap 'ENTER' for the next {n} number of fibonacci")

        for i in range(n):
            print(f'{next(fib_gen)}') 

        print(line_break)


if __name__ == '__main__':
    main()
