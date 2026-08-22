def print_profile(**kwargs):
	for key, value in kwargs.items():
		print(key, ":", value)
		
print_profile(name = "ali", age = 25, city =  "London")