#!/usr/bin/env python3

# Created by: Sydney Kuhn
# Created on: Oct 2020
# This program prints the odd numbers in a list of 10 random numbers

import random


def find_odd_numbers(list_of_numbers):
    # this function prints the odd numbers

    odd_numbers = []
    loop_counter = 1

    for i in list_of_numbers:
        if loop_counter % 2 != 0:
            odd_numbers.append(i)
        loop_counter += 1

    return odd_numbers


def main():
    # this function creates 10 random numbers in a list

    list_of_numbers = []

    # input
    for loop_counter in range(0, 10):
        random_number = random.randint(1, 100)  # a number between 1-100
        list_of_numbers.append(random_number)
        print("The random number {0} is : {1}".format(loop_counter + 1, random_number))
        loop_counter += 1

    odd_numbers = find_odd_numbers(list_of_numbers)

    print("\nThe numbers in odd positions in the list are {0}".format(odd_numbers))
    print("\nDone.")


if __name__ == "__main__":
    main()
