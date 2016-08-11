# I want to be able to call capitalize_nested from main w/ various lists
# and get returned a new nested list with all strings capitalized.
# Ex. ['apple', ['bear'], 'cat']
# Verify you've tested w/ various nestings.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()
capitalize_list = []
def capitalize_nested(input_list):
	
	for each_list_item in input_list:
	
		if isinstance(each_list_item, int):
			break #go to the next item in the list
		elif isinstance(each_list_item, list):
			capitalize_nested(each_list_item)	 			 
		else: 
			capitalize_list.append(each_list_item.capitalize()) #puts all the strings back into a list where they're all broken down
	
	return capitalize_list




def main():
	# print(capitalize_nested(['shredder','splinter',['casey jones', ['raphael', 14],'rocksteady'], 'joe']))
	# print(capitalize_nested(['sacramento', 'san jose', 'sanfrancisco', 'berkeley', ['north Berkeley', 'south Berkeley', 'berkeley Hills']]))
	pass

if __name__ == '__main__':
    main()
