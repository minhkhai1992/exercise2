# By Using logic understanding to solve start, stop  and quit the program
# Demo problem by use python and practice to code exercise.

# user_input = input("enter command: ")
# started = False
# print("start - to start the car")
# print("stop - to stop the car")
# print("quit - to exit")
# while user_input.upper() != "QUIT":
#     car_input = input("> ")
#     if car_input.upper() == "START":
#         if started:
#             print("Car already started...")
#         else:
#             print("Car started...Ready to go!")
#             started = True
#     elif car_input.upper() == "STOP":
#         if not started:
#             print("Car already Stopped...")
#         else:
#             print("Car Stopped!")
#             started = False
#     elif car_input.upper() =="QUIT":
#         break
#     else:
#         print("I don't understand your command.")

# prices = [10, 20, 30]
# total = 0
#
# for num in prices:
#     total+= num
# print(f"Total will be: {total}")

# for x in range(4):
#     for y in range(4):
#         print(f"{x}, {y}")

# numbers = [5, 2, 5, 2, 2]
#
# for x in numbers:
#     print(x * "x")

# numbers = [5, 2, 5, 2, 2]

# for x in numbers:
#     output = ''
#     for count in range(x):
#         output+= 'x'
#     print(output)

# names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
#
# #print(names[2:]) #return all items from index to the end
# #print(names[:]) #return all items in the list or 'names'
# print(name)


# find the largest number in the list
# number = [10, 11, 12, 9, 100, 200, 13, 0]
# max = number[0]
# for x in number:
#     if x > max:
#         max = x
#
# print(max)

# number = [10, 11, 12, 9, 10, 200, 13]

# number.insert(len(number), 26) # index position, add "number"
# print(number)

# number.remove(100) # remove a number you want to remove out of the list
# print(number)

# number.clear() # make a list is empty
# print(number)

# number.pop(2) #index position
# print(number)

# print(number.count(10)) # check how many time number duplicate in list

# number.sort() #run to sort the list first
# print(number)

# number2 = number.copy()
# number.append(8)
# print (number)

# Write a program to remove the duplicates in a list
number = [10, 11, 12, 9, 10, 200, 11, 15]
table = []

for x in number:
    if x not in table:
        table.append(x)
print(table)
