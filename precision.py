#!/usr/bin/python3

import os.path
import numpy as np
import csv
from functions import *

def mean_squared_error(predictions, actual_values):
	n = len(predictions)
	mse = sum((predictions[i] - actual_values[i]) ** 2 for i in range(n)) / n
	return mse

def calculate_precision(theta0, theta1, mileage, mileage_min, mileage_max, prices, prices_min, prices_max):
	predictions = [theta1 * ((x - mileage_min) / (mileage_max - mileage_min)) + theta0 for x in mileage]
	normalized_predictions = [estimate_price(x, theta0, theta1, mileage_min, mileage_max, prices_min, prices_max) for x in mileage]

	mse = mean_squared_error(predictions, prices)
	normalized_mse = mean_squared_error(normalized_predictions, prices)

	return mse, normalized_mse

def main():
	file_path = 'data.csv'  # CSV file
	mileage, prices = load_data_from_csv(file_path)

	learning_rate = 0.2
	iterations = 1000

	theta0, theta1 = get_tethas()
	
	mileage_min, mileage_max = get_max_min(mileage)
	prices_min, prices_max = get_max_min(prices)

	# Calculate precision using the trained model
	mse, normalized_mse = calculate_precision(theta0, theta1, mileage, mileage_min, mileage_max, prices, prices_min, prices_max)

	print(f"Mean Squared Error: {mse}")
	print(f"Normalized Mean Squared Error: {normalized_mse}")

if __name__ == "__main__":
	main()