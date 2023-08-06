# 1.Hello, World!: Write a Python program that prints "Hello, World!" to the console.

print("Hello World")


# 2.Data Type Play: Create variables of each data type (integer, float, string, boolean, list, tuple, dictionary, set) and print their types and values.

num=12
print(f"Type of variable1:{type(num)}, value: {num}")

float=3.12
print(f"Type of variable1:{type(float)}, value: {float}")

str="name"
print(f"Type of variable1:{type(str)}, value: {str}")

bool=True
print(f"Type of variable1:{type(bool)}, value: {bool}")

list=[1,2,3,4]
print(f"Type of variable1:{type(list)}, value: {list}")

tuple=(1,2,3,4)
print(f"Type of variable1:{type(tuple)}, value: {tuple}")

set = {
    "name":"react",
    "age":20,
    "method":False
    }
print(f"Type of variable1:{type(set)}, value: {set}")

set2 = {1,2,3,4}
print(f"Type of variable1:{type(set2)}, value: {set2}")


# 3.List Operations: Write a Python program to create a list of numbers from 1 to 10, and then add a number, remove a number, and sort the list.

li = [1,6,7,8,9,10,2,3,4,5]
li.append(20)
li.remove(6)
li.sort()
print(li)


# 4.Sum and Average: Write a Python program that calculates and prints the sum and average of a list of numbers.
list2 = [1,2,3,4,5]
sum=0
count=0
for i in range(len(list2)):
    sum+=list2[i]
    count+=1
    
print("avg is:-",sum/count)


# 5.String Reversal: Write a Python function that takes a string and returns the string in reverse order.

def reverse_string(input_string):
    reversed_str = ""
    for i in input_string:
        reversed_str = i + reversed_str
  
    return reversed_str

# Test the function
input_string = "python"
reversed_string = reverse_string(input_string)
print(reversed_string)


# 6. Count Vowels: Write a Python program that counts the number of vowels in a given string.

str="Hello"
count =0
for i in str:
    if (i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
        count += 1
        
print( "Number of vowels:", count )


# 7. Prime Number: Write a Python function that checks whether a given number is a prime 
   
def is_prime(number):
    if (number<=1):
        return False
    for i in range(2,number):
        if(number%i==0):
            return False
            
        
    return True


input_number = 13
if is_prime(input_number):
    print(f"{input_number} is a prime number.")
else:
    print(f"{input_number} is not a prime number.")



#  8. Factorial Calculation: Write a Python function that calculates the factorial of a number.

def factorial(n):


    if (n==0 or n==1):
        return 1
    else:
        result=1
        
        for i in range(2,n+1):
            result*=i
            
        return result
        

Input=5

output=factorial(Input)
print(output)   


# 9. Fibonacci Sequence: Write a Python function that generates the first n numbers in the Fibonacci sequence.

def fibonacci(n):
    fib_seq = [0, 1]
    for i in range(2, n):
        next_num = fib_seq[i - 1] + fib_seq[i - 2]
        fib_seq.append(next_num)
    return fib_seq

# Test the function
input_n = 5
fib_num = fibonacci(input_n)
print(fib_num)


# 10. List Comprehension: Use list comprehension to create a list of the squares of the numbers from 1 to 10.

square = [x ** 2 for x in range(1, 11)]
print(square)