# I want to be able to call is_sorted from main w/ various lists and get
# returned True or False.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()
def is_sorted(mystery_list):
	#if it's sorted, return True
	#else if it's not sorted, return False
	for item in mystery_list:
		if isinstance(item, int):
			if str in mystery_list:
				return False
			if sorted(mystery_list, key=int) == mystery_list:
				return True
			else: 
				return False	 
		else:
			if sorted(mystery_list) == mystery_list:
				return True
			else:
				return False


def main():
	# print(is_sorted(['a','b','c', 'd']))
	# print(is_sorted(['Sacramento', 'Alameda', 'Tahoe', 'Los Angeles']))
	# print(is_sorted([1, 2, 3]))
	# print(is_sorted([1, 2, 3, ['a','b','c', 'd']]))   # can't figure out how to get this to pass 
	pass

if __name__ == '__main__':
	main()