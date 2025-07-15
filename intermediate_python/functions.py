from datetime import datetime
from typing import Iterator

# 1. keep the function name short and concise
# 2. Specify a return type
# 3, Make as simple and reuseable as possible
# 4. Document all your functions
# 5. handle errors appropriately


# example 1
def get_time() -> str: # 2. specify a return type

    """
    A function that gets the current time in the users locale

    Example:

    >>> get_time() -----> "16:10:11"
    """

    now: datetime = datetime.now()

    return f'{now:%X}'

# print(get_time())


# example 2

from collections.abc import Iterable

def get_total_discount(prices: Iterable[float], percent: float) -> float:

    """ 
        Calculate the total price after applying a discount.

        This function calculates the total sum of prices in the provided list and then applies a discount based on the given discount rate. If the discount rate is invalid (e.g., negative or greater than 1), the function raises a ValueError.

        :param prices: A list of item prices.
        :type prices: List[float]
        :param percent: The discount rate to apply. Default is 0.1 (10%).
        :type percent: float, optional
        :return: The total price after applying the discount.
        :rtype: float
        :raises ValueError: If the discount_rate is not between 0 and 1 inclusive, or if prices contain non-numeric values.

        :Example:
        >>> get_total_discount([100.0, 50.0, 25.0], 0.2)
        140.0
    """

    #Validate Input
    if not(0 <= percent <= 1):
        raise ValueError(f'Invalid discount rate : {percent}. Must be between 0 and 1 inclusive...')

    if not all(isinstance(price, (int,float)) and price >= 0  for price in prices):
        raise ValueError("All prices must be non-negative numbers")


    total : float = sum(prices)
    return total * (1 - percent)

def main() -> None:
    print(get_total_discount(prices=[1000, 500, 3500], percent= 0.13))


if __name__ == '__main__':
    main()