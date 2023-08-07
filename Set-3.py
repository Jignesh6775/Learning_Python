# 1. **Tuple Unpacking**: Create a list of tuples, each containing a name and an age. Then, use tuple unpacking to iterate through the list and print each name and age.
#     - *Input*: [("John", 25), ("Jane", 30)]
#     - *Output*: "John is 25 years old. Jane is 30 years old."

list = [
    ("John", 25), 
    ("Jane", 30), 
    ("Shanaya", 23)
]

for name, age in list:
    print(f"{name} is {age} years old.")


# 2. **Dictionary Manipulation**: Create a dictionary with keys as names and values as ages. 
# Write functions to add a new name-age pair, update the age of a name, and delete a name from the dictionary.
#     - *Input*: Add "John": 25, Update "John": 26, Delete "John"
#     - *Output*: "{}, {'John': 26}, {}"


def add(pair, Dict):
    if pair[0] in Dict:
        return f"Name: {pair[0]} is already present in Dictionary."
    
    Dict[pair[0]] = pair[1]
    return f"Name: {pair[0]} is added along with Age: {pair[1]}."

def update(pair, Dict):
    if pair[0] in Dict:
        Dict[pair[0]] = pair[1]
        return f"Name: {pair[0]} is updated along with Age: {pair[1]}."
    
    return f"Name: {pair[0]} is not Present in the Dictionary."

def delete(name, Dict):
    if name in Dict:
        del Dict[name]
        return f"Name: {name} is Deleted from Dictionary."
    
    return f"Name: {name} is not present in Dictionary."


# Add Operation
Dict = dict()
print(add(("Sima", 25), Dict))
print(add(("Sima", 26), Dict))
print(Dict)

# Update Operation
print(update(("Sima", 27), Dict))
print(update(("Asha", 54), Dict))
print(Dict)

# Delete Operation
print(delete("Asha", Dict))
print(delete("Sima", Dict))
print(Dict)



# 3. Two Sum Problem**: Given an array of integers and a target integer, find the two integers in the array that sum to the target.
#     - *Input*: [2, 7, 11, 15], target = 9
#     - *Output*: "[0, 1]"


def twoSum(arr, t):
    s = 0
    e = len(arr)-1
    arr.sort()
    
    while(s < e):
        sum = arr[s] + arr[e]
        
        if sum == t:
            return [s, e]
        elif sum < t:
            s += 1
        else:
            e -= 1
            
    return "not found"


arr = [2, 7, 11, 15]
target = 9
print(twoSum(arr, target))


# 4. Palindrome Check: Write a Python function that checks whether a given word or phrase is a palindrome.
# - *Input*: "madam"
# - *Output*: "The word madam is a palindrome."

def checkPalindrome(s):
    list = [*s]   #By using *s we can convert string to list => ['m','a','d','a','m']

    i=0
    j=len(list)-1
  
    for e in range(int(len(list)//2)):
        if list[i] != list[j]:
            return False
        else:
            i += 1
            j -= 1

    return True

str = "madam"
print(checkPalindrome(str))


# 5. **Selection Sort**: Implement the selection sort algorithm in Python.
#     - *Input*: [64, 25, 12, 22, 11]
#     - *Output*: "[11, 12, 22, 25, 64]"



def selectionSort(list):
    
    for i in range(len(list)):
        
        minIndex = i
        for j in range(i+1, len(list)):
            if list[minIndex] > list[j]:
                minIndex = j
                
        list[i], list[minIndex] = list[minIndex], list[i]
        

list = [64, 25, 12, 22, 11]
print(list)
selectionSort(list)
print(list)


# 6. **Implement Stack using Queue**: Use Python's queue data structure to implement a stack.
#     - *Input*: push(1), push(2), pop(), push(3), pop(), pop()
#     - *Output*: "1, None, 3, None, None"
from queue import *

st = LifoQueue()

def push(n):
    st.put(n)
    
push(2)
push(3)

while not st.empty():
    print(st.get())
    
q = PriorityQueue()

q.put(20)
q.put(303)
q.put(40)

while not q.empty():
    print (q.get())



# 7. **FizzBuzz**: Write a Python program that prints the numbers from 1 to 100, but for multiples of three, print "Fizz" instead of the number, for multiples of five, print "Buzz", and for multiples of both three and five, print "FizzBuzz".
#     - *Input*: None
#     - *Output*: "1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16,..."


for i in range(101):
    if i%5==0 and i%3==0:
        print("FizzBuzz")
    elif i%5 == 0:
        print("Buzz")
    elif i%3 == 0:
        print("Fizz")
    else:
        print(i)



# 8. **File I/O**: Write a Python program that reads a file, counts the number of words,
# and writes the count to a new file.
#     - *Input*: A text file named "input.txt" with the content "Hello world"
#     - *Output*: A text file named "output.txt" with the content "Number of words: 2"


def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            words = text.split()
            word_count = len(words)
            return word_count
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return 0


def write_word_count(file_path, count):
    try:
        with open(file_path, 'w') as file:
            file.write(str(f"Number of words: {count}"))
            print(f"Word count ({count}) written to file '{file_path}' successfully.")
    except IOError:
        print(f"Error: Could not write to file '{file_path}'.")


if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"

    word_count = count_words(input_file)
    write_word_count(output_file, word_count)


# 9. **Exception Handling**: Write a Python function that takes two numbers as inputs and returns their division, 
# handling any potential exceptions (like division by zero).
#     - *Input*: 5, 0
#     - *Output*: "Cannot divide by zero."


def divide(dividant, divisor):
    try:
        return dividant/divisor
    except ArithmeticError as e:
        return "Error: ", e
    
    
print(divide(5, 0))