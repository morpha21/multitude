from math import sqrt

def divisors_sum(num):
	return 1 + sum([i+num/i for i in range(2,1+int(sqrt(num))) if num%i == 0])

def is_perfect(num):
	return num == divisors_sum(num)

def perfect_finder(numbers):
	for i in numbers:
		if is_perfect(i):
			print(i)

if __name__ == "__main__":
	for i in range(2, 34000000):
		if is_perfect(i):
			print(i)
