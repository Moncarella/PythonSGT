# # Task 1
def sum(a,b):
    return a + b

a = 12
b = 19
print(sum(a,b))

# # Task 2
def count_vowels(text):
    count = 0
    for char in text:
        if char in "aeiouAEIOU":
            count += 1
    return count

textInp = input("Enter the text\n")
print("There are " + str(count_vowels(textInp)) + " vowels in the text")

# Task 3
def reverse(text:str):
    revStr = ""
    for char in text:
        revStr = char + revStr
    return revStr

def is_palindrome(text:str):
    text = text.lower()
    if reverse(text) == text:
        return True
    else:
        return False

textInput = input("Enter the text:\n")
print(is_palindrome(textInput))


# Task 4
def even_int_from_list(listInput:list):
    evenList = []
    for element in listInput:
        if element % 2 == 0:
            evenList.append(element)
    return evenList

listInp = [5,2,3,8,7,1,0,9,6]
print(even_int_from_list(listInp))


# Task 5
def find_pair(integers,target_sum):
    seen = set()
    for number in integers:
        diff = target_sum - number
        if diff in seen:
            return [diff, number]
        # else:
        seen.add(number)
    return []

numbers = [4,8,19,5,3]
target_sum = 13
print(find_pair(numbers, target_sum))


# Task 6
def product_of_list(numbers:list):
    product = 1
    for number in numbers:
        product *= number
    return product

numbers = [6,3,7,2,9,2]
print(product_of_list(numbers))


# Task 7 - does not exist

# Task 8
def key_of_even(dict_input:dict):
    keys = []
    for key,value in dict_input.items():
        if value % 2 == 0:
            keys.append(key)
    return keys

input_dict = {"1":6, "2":10, "3":9, "4":8}
print(key_of_even(input_dict))


# Task 9
def get_sums(list_of_dict:list):
    sums_dict = dict()
    for values_dict in list_of_dict:
        for key,value in values_dict.items():
            if key in sums_dict:
                sum = sums_dict.get(key)
                sum += value
                sums_dict[key] = sum
            else:
                sums_dict[key] = value
    return sums_dict

listInput = [{1:19, 2:7, 3:6}, {1:19, 2:7, 3:6}, {1:7, 2:5, 3:3}]
print(get_sums(listInput))


# Task 10
def rev_tuple_first_last(tup:tuple):
    tup_list = list(tup)
    tup_list[0], tup_list[len(tup_list)-1] = tup_list[len(tup_list)-1], tup_list[0]
    return tuple(tup_list)

input_tup = (45,32,21,94,32,11)
print(rev_tuple_first_last(input_tup))


# Task 11
def non_div_3(input_set:set):
    non_div_3_set = set()
    for element in input_set:
        if element % 3 != 0:
            non_div_3_set.add(element)
    return non_div_3_set

inp_set = {3,9,15,21,4,7}
print(non_div_3(inp_set))
