def binary_search_recursive(ordered_list, search_value):
	if len(ordered_list) == 0:
		return False
	else:
		middle = len(ordered_list)//2

		# checking the search value is in the list
		if search_value == ordered_list[middle]:
			return True
		elif search_value < ordered_list[middle]:
			return binary_search_recursive(ordered_list[:middle], search_value)
		else:
			return binary_search_recursive(ordered_list[middle+1:], search_value)
		