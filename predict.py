#!/usr/bin/python3

import os.path
import sys
from functions import *

def main():
    while True:
        file_path = 'data.csv'  # CSV file
        mileages, prices = load_data_from_csv(file_path)
        
        mileage = input("Please enter a mileage: ")
        try:
            mileage = float(mileage)
        except ValueError:
            print("That's not a number!")
            sys.exit()

        if mileage < 0:
            print("Be realistic, mileage cannot be a negative value!")
            sys.exit()
        if mileage > 3039122:
            print("You should check for a smaller mileage, no car in the world has been on the road that much!")
            sys.exit()

        norm_mileage = (mileage - min(mileages)) / (max(mileages) - min(mileages))
        theta0, theta1 = get_thetas()
        norm_price = theta0 + (theta1 * norm_mileage)
        estimated_price = norm_price * (max(prices) - min(prices)) + min(prices)
        print("This car is worth " + str(estimated_price) + "$")

        # Pregunta si se desea procesar otro conjunto de datos
        another_process = input("Do you want to process another set of data? (y/n): ").lower()
        if another_process != 'y':
            break

if __name__ == "__main__":
    main()