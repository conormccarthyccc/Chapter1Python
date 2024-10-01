# Title: Task 7, 8 and 9
# Author: CMC
# Date: Oct 24

# Task 7

# Sample program to build up a list of user details
userList = []
userName = input("Enter your name:")
userList.append(userName)
userAge = int (input("What age are you "+userName+"?"))
userList.append(userAge)
userCountry = input("What is your country of birth?")
userList.append(userCountry)
userYearOfBirth = int(input("What is your year of birth? "))
userList.append(userYearOfBirth)

print("My database for "+userName+"\n"+str(userList))

# Reverse the list
userList.reverse()

# Task 8

# Define the pangram
pangram = "The five boxing wizards jump quickly"

# Split the pangram into words
words = pangram.split()

# Print the resulting list of words
print(words)



# Original pangram
pangram = "The five boxing wizards jump quickly"

# Split the pangram into words
words = pangram.split()

# Rearranged order of words
new_order = [words[4], words[3], words[0], words[1], words[2], words[5]]

# Join the rearranged list into a new string
new_pangram = ' '.join(new_order)

# Print the result
print(new_pangram)

# Task 9

# Program to simulate a fruit machine!
import random

# Open the fruits file (already created)
fruitFile = open("fruits.txt","r")

# Read the entire file
fileContents = fruitFile.read()

# Close the file
fruitFile.close()

# Split the content into a list
fruits = fileContents.split()

# Spin! Display three fruits
print(random.choice(fruits))
print(random.choice(fruits))
print(random.choice(fruits))