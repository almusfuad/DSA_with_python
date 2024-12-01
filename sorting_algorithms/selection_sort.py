# Determine the lowest value
# Swap the lowest value with the first value

def selection_sort(my_list):
	list_length = len(my_list)
	for i in range(list_length - 1):
		lowest = my_list[i]
		index = i
		for j in range(i+1, list_length):
			if my_list[i] < lowest:
				index = j
				lowest = my_list[j]
		my_list[i], my_list[index] = my_list[index], my_list[i]
	return my_list
	