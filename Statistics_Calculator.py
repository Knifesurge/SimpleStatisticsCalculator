# Statistics Calculator
from math import sqrt, floor

def round_num(n, decimals=0):
    mult = 10 ** decimals
    return floor(n*mult + 0.5) / mult

precision_measure = float(input("Enter the precision measure (p.m.): "))
n = int(input("Enter number of data points (N): "))
data = [None for _ in range(n)]

for i in range(n):
    data_point = float(input(f'Enter the {i+1}-th data point: '))
    data[i] = data_point

print(f'You entered: {data}')

# Calculate the mean
avg = 0
for num in data:
    avg += num
avg = avg / n
mean = 0
for num in data:
    mean += (num - avg) ** 2

# Calculate the std dev.
std_dev = sqrt(mean/(n-1))

# Calculate the std dev. of the mean
std_dev_mean = std_dev / (sqrt(n))

# Calculate the optimal N
n_optimal = round_num((std_dev / precision_measure) ** 2)

# Get uncertainty
uncertainty = max([std_dev_mean, precision_measure])

print(f'Average: {avg}')
print(f'Mean: {mean}')
print(f'Std. Deviation: {std_dev}')
print(f'Std. Dev. of the Mean: {std_dev_mean}')
print(f'Optimal Trials: {n_optimal}')
print(f'Uncertainty: {uncertainty}')

input("\n\nPress ENTER to quit")