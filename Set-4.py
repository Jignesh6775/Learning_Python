# 1. **Anagram Check**: Write a Python function that checks whether two given words are anagrams.
#     - *Input*: "cinema", "iceman"
#     - *Output*: "True"


def anagramCheck(s1, s2):
    list1 = []
    list2 = []
    for e1, e2 in zip(s1, s2):
        if e1 != " ":
            list1.append(e1)
        if e2 != " ":
            list2.append(e2)
            
    list1 = sorted(list1)
    list2 = sorted(list2)
    
    if list1 == list2:
        return True
    else:
        return False
    

s1 = "cinema"
s2 = "iceman"

result = anagramCheck(s1, s2)

if(result):
    print(f"Both String s1: {s1} and String s2: {s2} are anagrams.")
else:
    print("Not Anagrams")
        


# 2. **Bubble Sort**: Implement the bubble sort algorithm in Python.
#     - *Input*: [64, 34, 25, 12, 22, 11, 90]
#     - *Output*: "[11, 12, 22, 25, 34, 64, 90]"


def bubbleSort(list):
    for i in range(len(list)):
        for j in range(len(list)-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                
    return list


list = [64, 34, 25, 12, 22, 11, 90]
print("Original List: {}".format(str(list)))

bubbleSort(list)
print("Sorted List {}".format(str(list)))