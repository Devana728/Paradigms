def sort_list_declarative(n_list):  
  
# Sort the list using lambda and sorted function
  sorted_list = sorted(n_list, key=lambda x: int(x[0:]))
  return sorted_list
# Print the sorted list
print("The list of the sorted values are:")

n_list = ['11', '50', '5', '1', '37', '19']

print(sort_list_declarative(n_list))