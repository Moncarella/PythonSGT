elements = {1,2,3,42,1,4,52}
print(elements) # It removes duplicated elements
# Sets are not ordered
elements.remove(42)
print(elements)
elements.add(34)
print(elements)

elements = {1,2,3,42,1,4,52}
elements2 = {4,2,6,3,10,0,34}
elementsU = elements | elements2  # combines two sets into one
print(elementsU)

elementsI = elements & elements2  # Intersection will return only elements that exist in both sets
print(elementsI)

elementsD = elements - elements2
print(elementsD) 

# Sets are useful for removing duplicates
# You convert list to the set and it removes duplicates:

my_list = [1,2,2,3,3,3,4,4,4,4,4,4,5,5,5,5,5,5,5]
unique_set = set(my_list)
print(unique_set)  # output: {1,2,3,4,5}
print(sorted(unique_set))  # converts set to list and sorts it

