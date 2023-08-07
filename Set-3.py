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