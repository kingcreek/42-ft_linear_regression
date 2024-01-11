#!/usr/bin/python3

import csv
import sys
import os.path

def get_max_min(data):
	data_min = min(data)
	data_max = max(data)
	return data_min, data_max

def normalize_data(data):
	data_min, data_max = get_max_min(data)
	normalized_data = [(x - data_min) / (data_max - data_min) for x in data]
	return normalized_data, data_min, data_max

def estimate_price(mileage, theta0, theta1, mileage_min, mileage_max, prices_min, prices_max):
	norm_mileage = (mileage - mileage_min)/(mileage_max-mileage_min)
	norm_price = theta1 * norm_mileage + theta0
	return norm_price * (prices_max-prices_min) + prices_min

def load_data_from_csv(file_path):
	mileage = []
	prices = []
	
	if not os.path.exists(file_path):
		print("There is no data.csv file. Please add one to the same directory as " + sys.argv[0])
		sys.exit()

	with open(file_path, 'r') as file:
		reader = csv.DictReader(file)
		for row in reader:
			try:
				mileage.append(float(row['km']))
				prices.append(float(row['price']))
			except ValueError:
				pass

	return mileage, prices

def get_tethas():
	if os.path.exists('thetas.txt'):
		with open('thetas.txt') as f:
			theta0 = float(f.readline())
			theta1 = float(f.readline())
	else:
		theta0 = 0
		theta1 = 0
	return theta0, theta1