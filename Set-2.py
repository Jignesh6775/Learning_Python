# Problem 1: Print the following pattern
rows = 5  

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# Problem 2: Display numbers from a list using loop

numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num % 5 == 0:
        if num > 500:
            break
        elif num > 150:
            continue
        print(num)


# Problem 3: Append new string in the middle of a given string
s1 = "Ault"
s2 = "Kelly"

mid_index = len(s1) // 2  # floor value(//)
s3 = s1[:mid_index] + s2 + s1[mid_index:]

print(s3) 


# Problem 4: Arrange string characters such that lowercase letters should come first

def arrange_lowercase_first(input_str):
    lowercase_chars = ""
    uppercase_chars = ""

    for char in input_str:
        if char.islower():
            lowercase_chars += char
        else:
            uppercase_chars += char

    arranged_str = lowercase_chars + uppercase_chars
    return arranged_str


str1 = "PyNaTive"
result = arrange_lowercase_first(str1)
print(result)


# Problem 5: Concatenate two lists index-wise


list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

result = []

lenght=len(list1)

for i in range(lenght):
    result.append(list1[i] + list2[i])


print(result)



# Problem 6: Concatenate two lists in the following order

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

concatenated_list = []

for word1 in list1:
    for word2 in list2:
        concatenated_list.append(word1 + word2)

print(concatenated_list)

# Problem 7: Iterate both lists simultaneously

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
length=len(list1)
for i in range(length):
    print(list1[i], list2[length - i - 1])


# Problem 8: Initialize dictionary with default values

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

result = {}

for employee in employees:
    result[employee] = defaults

print(result)    


# Problem 9: Create a dictionary by extracting the keys from a given dictionary

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}

keys = ["name", "salary"]

output = {}

for key in keys:
    output[key] = sample_dict[key]

print(output)


# Problem 10: Modify the tuple

tuple1 = (11, [22, 33], 44, 55)

# => making list here 
tuple_list = list(tuple1)

# => accesing element here 
tuple_list[1][0] = 222

# => making touple here
tuple1_modified = tuple(tuple_list)

print("tuple1:", tuple1_modified)