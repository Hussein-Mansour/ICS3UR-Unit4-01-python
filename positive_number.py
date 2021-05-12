#!/usr/bin/env python3

# Created by: Hussein Mansour
# Created on: Tue/May11/2021
# This program while loop program


def main():
    # this function add all the whole numbers up to user input positive number

    # input
    positive_number = int(input("enter a positive integer:"))

    # process  & output
    sum_number = 0
    loop_counter = 1

    while loop_counter <= positive_number:
        sum_number = sum_number + loop_counter
        loop_counter = loop_counter+1    # update counter

    print("The sum of all positive numbers from 1 to {0} is".format(positive_number), sum_number)
    print("\nDone.")


if __name__ == "__main__":
    main()
