#!/usr/bin/env python3
# Created By: Logan Sweeney
# Date: Dec. 4, 2021
# This program asks the user for the diameter
# of a pizza and calculates and displays the
# total with HST.
import constants
import time


def main():
    # get the diameter
    diameter = int(input("Enter the diameter: "))

    print("")
    print("Calculating...")
    time.sleep(2.25)

    # calculate the subtotal, tax & total
    subtotal = constants.LABOUR_COST + constants.RENTAL_COST + constants.INGRED_COST * diameter
    tax = subtotal * constants.TAX_RATE
    total = subtotal + tax

    # display the total
    print("")
    print("The total with HST is ${:.2f}".format(total))


if __name__ == "__main__":
    main()
