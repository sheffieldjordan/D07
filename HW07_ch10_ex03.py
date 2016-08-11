# I want to be able to call cumulative_sum from main w/ various lists and
# get returned a list of the cumulative sums.
# You are safe to expect only integers in a flat list.
# Ex. the cumulative sum of [1, 2, 3] is [1, 3, 6]
#  - in the above example I want returned the list [1, 3, 6]
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()
def cumulative_sum(int_list):
	count = 0
	while count <= len(int_list)-2:
		int_list[count+1] = int_list[count] + int_list[count+1]
		count += 1
	return int_list
	# add the first number to the 2nd number and the 2nd number to the 3rd, etc. 
	# append these numbers to a new list, or replace the numbers in the old list
	# return the new list 

def main():
	# print(cumulative_sum([1,2,33,83]))
	# print(cumulative_sum([1,2,3]))
	# print(cumulative_sum([99, 0, 4, 1]))
	pass
if __name__ == '__main__':
    main()