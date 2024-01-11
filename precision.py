#!/usr/bin/python3

from functions import *

def getAccuracy(theta0, theta1, mileages, prices):

	normalized_mileage, mileage_min, mileage_max = normalize_data(mileages)
	normalized_prices, prices_min, prices_max = normalize_data(prices)

	price_average = sum(prices) / len(prices)

	ssr = sum(map(lambda mileage, price: pow(
		price - estimate_price(mileage, theta0, theta1, mileage_min, mileage_max, prices_min, prices_max), 2
	), mileages, prices))

	sst = sum(map(lambda price: pow(price - price_average, 2), prices))

	return ((1 - (ssr / sst)) * 100)

def main():
	file_path = 'data.csv'  # CSV file
	theta0, theta1 = get_thetas()
	mileages, prices = load_data_from_csv(file_path)
	accuracy = getAccuracy(theta0, theta1, mileages, prices)
	print("ft-linear-regression accuracy is: {:.2f}%".format(accuracy))

if __name__ == "__main__":
	main()
