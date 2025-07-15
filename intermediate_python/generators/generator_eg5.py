import csv
from typing import Generator
import sys

def csv_row_reader(file_path : str) -> Generator[list[str], None, None]:

    """
        This will recieve the csv_file_path and then retrive/yeild the rows from the csv file for the time user continue to press Enter 
    """

    with open(file_path, 'r') as csv_file:
        for row in csv.reader(csv_file):
            yield row


def main() -> None:
    reader: Generator[list[str], None, None] = csv_row_reader('cv-valid-train.csv')

    while True:

        try:
            for i in range(5):
                print(next(reader))

            input("Continue retriving more row?? press ENTER")
        except StopIteration:
            print("No more rows remaining in the csv")
            sys.exit()


if __name__ == '__main__':
    main()