# from sys import float_repr_style
from typing import Generator

def cumulative_sum() -> Generator[float, float, None]:

    """
        This total += yeild total is going to grab the total value  and it
        is going to loop and then going to send that value back. 

        >>> Here yeild is going to act as a retrive though there is no retriver keyword in python still
        IT retives the value yeilds and then loop again to calcualte the final cumulative sum
    """

    total: float =  0
    
    while True:

        # new_value: float = yield total

        total += yield total

    
def main() -> None:

    cumulative_generator : Generator[float, float, None] = cumulative_sum()
    
    # initialize generator 
    next(cumulative_generator)

    while True:

        value: float = float(input("Enter a number:"))
        current_sum: float = cumulative_generator.send(value)
        print(f"Cumulative Sum is: {current_sum}")

if __name__ == '__main__' :
    main()   


    