nums = list(range(1,101))

for i in nums:
	if i%3 == 0:
		print(f'Buzz - {i}')
	elif i%5 == 0:
		print(f'Fizz - {i}')
	else:
		pass

	if (i%3 == 0) and (i%5 == 0):
		print(f'FizzBuzz - {i}')