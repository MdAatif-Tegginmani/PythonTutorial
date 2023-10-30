# nums = list(range(3, 15, 3))
# nums = list(range(5, 10, 2))
# print(nums)


# a = int(input())
# b = int(input())

# nums = list(range(a,b))
# print(nums)


# sqs=[0,1,4,9,16,25,36,49,64,81]

# print(sqs[7:5:-1])

# nums = [7,6,5,4,3,2,1]
# res = nums[::-1]  #to reverse a list 

# print(res)

#list splices


# a = input()
# res = a[0:3]  #to input first 3 items of list
# print(res)


# names[1:-1]


# Sum of input numbers between a range 

# N = int(input())
# total = 0 
# for i in range(1, N + 1):
#      total += i
# print(total)



# N = int(input("Enter a number (N): "))
# sum_of_numbers = 0
# for i in range(1, N + 1):
#     sum_of_numbers += i
# print(sum_of_numbers)

# temp = float(input())

# if(temp > 100) :
#     print("Boiling")

# a = 10
# b = 20

# a = a+ b
# a = 30
# b = a-b 
# b = -10

# a = a-b
# a = 30- (-10)
# a = 40


# a = int(input())
# b = int(input())

# def get(a,b)
    
    
# def welcome():
#         user =input()
#         print("Welcome",user)

# welcome()



# def search(text, word):
#     if word in text:
#         return "Word found"
#     else:
#         return "Word not found"

# # Get user input for the "text" variable
# text = input("Enter the text: ")

# # Get user input for the "word" variable
# word = input("Enter the word to search for: ")

# # Calling the function and printing the result
# print(search(text, word))



def star(steps):
    for i in range(1, steps + 1):
        for j in range(i):
            print("*",end =" ")
        print()


star(5)

























def hastags(step):
    for i in range(1 , step -1):
        for j in range(i):
            print("#",end ="  ")
        print()


hastags(6)
        




