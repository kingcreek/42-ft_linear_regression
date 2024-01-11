#!/usr/bin/python3

import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.tri import Triangulation
from functions import *

def update_thetas(theta0, theta1, learning_rate, normalized_mileage, normalized_prices):
	m = len(normalized_mileage)
	
	# Calculate predictions
	predictions = [theta0 + theta1 * x for x in normalized_mileage]
	
	# Calculate errors
	errors = [predictions[i] - normalized_prices[i] for i in range(m)]

	tmp_theta0 = sum(errors) / m
	tmp_theta1 = sum(errors[i] * normalized_mileage[i] for i in range(m)) / m

	theta0 -= learning_rate * tmp_theta0
	theta1 -= learning_rate * tmp_theta1

	return theta0, theta1

def draw_plot(mileage, prices, theta0, theta1, mileage_min, mileage_max, prices_min, prices_max, iteration, normalized_prices):
	plt.clf()

	# Plot 2D graph
	plt.subplot(121)
	plt.scatter(mileage, prices, color='blue', label='Data points')
	plt.plot(mileage, [estimate_price(x, theta0, theta1, mileage_min, mileage_max, prices_min, prices_max) for x in mileage], color='red', label='Regression line')
	plt.xlabel('Mileage')
	plt.ylabel('Price')
	plt.title(f'Linear Regression - Iteration {iteration + 1}')
	plt.legend()

	# Plot 3D graph
	ax = plt.subplot(122, projection='3d')
	ax.scatter(mileage, normalized_prices, prices, color='blue')
	mileage_line = np.linspace(min(mileage), max(mileage), 100)
	prices_line = np.array([estimate_price(x, theta0, theta1, mileage_min, mileage_max, prices_min, prices_max) for x in mileage_line])
	normalized_prices_line = (prices_line - prices_min) / (prices_max - prices_min)
	ax.plot(mileage_line, normalized_prices_line, prices_line, color='red', label='Regression line')

	ax.set_xlabel('Mileage')
	ax.set_ylabel('')
	ax.set_yticks([])
	ax.set_zlabel('Price')
	ax.set_title(f'Linear Regression - Iteration {iteration + 1}')

	plt.draw()
	plt.pause(0.01)


def train_and_plot(mileage, prices, learning_rate, iterations):

	update_interval = 30

	# Normalize data
	normalized_mileage, mileage_min, mileage_max = normalize_data(mileage)
	normalized_prices, prices_min, prices_max = normalize_data(prices)

	theta0 = 0
	theta1 = 0

	for iteration in range(iterations):
		theta0, theta1 = update_thetas(theta0, theta1, learning_rate, normalized_mileage, normalized_prices)

		# Plot updated regression line every update_interval iterations
		if iteration % update_interval == 0 or iteration == iterations - 1 or iteration == 0:
			draw_plot(mileage, prices, theta0, theta1, mileage_min, mileage_max, prices_min, prices_max, iteration, normalized_prices)

	plt.ioff()  # Disable interactive mode

	# Save theta0 and theta1 in thetas.txt file
	with open("thetas.txt", "w") as file:
		file.write(f"{theta0}\n{theta1}")

	plt.show()

def main():
	file_path = 'data.csv'  # CSV file
	mileage, prices = load_data_from_csv(file_path)

	learning_rate = 0.2
	iterations = 1000

	# Train model and plot
	train_and_plot(mileage, prices, learning_rate, iterations)

if __name__ == "__main__":
	main()
