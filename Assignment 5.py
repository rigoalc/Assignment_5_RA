#ASSIGNMENT 5

# Rodrigo 
# 9/10/2021
# CIS-216-12292 
# Python Programming
 

#Write up a program that asks the user for their name, and the current day. 
#It should then display the special of the day at a restaurant.

#Specials
#Day	Special
#Monday	Spaghetti
#Tuesday	Lasagna
#Wednesday	Minestrone soup
#Thursday	Pot pie
#Friday	Tacos

#Also, note that for Tuesday and Thursday, the special changes to the following, 
# when the user's name is less than five characters.

#Day	Special
#Tuesday	Impossible Burger
#Thursday	Beyond Burger

#Example of Expectations

#You don't have to match the following output exactly 
#as long as you fulfill all of the requirements. This is just an example.

#I will run the program like so:

#$ python main.py
#Please enter your name:
#I will then type my name in, and hit Enter.

#Please enter your name: Steven
#Please enter the day of the week (Mon, Tue, Wed, Thu, Fri): 
#I will then enter the day of the week, and hit Enter. The special should then be printed out.

#Please enter the day of the week (Mon, Tue, Wed, Thu, Fri): Tue
#The special for Tuesday is Lasagna.

#No code has been copied from elsewhere
#(Do not copy the first result for Python Restaurant Menu in Google)

#Every file has a header with your name, date, CRN, and class name

#Explain how designed:

#The program was first designed in pseudocode following a flowchart and then practicing in the editor. 
# I was able to think in the versatility of having variables easy to change in case or need future modifications.


# 7 hs was the total development time for this programself.


#At least 1 of the following:

#Flowchart of main part of program; or

#Paragraph of at least 1 sentence each, explaining what you did for each part of the Development Cycle:

#Analyze: What is the problem?

#Design: How will you solve the problem?

#Develop: What did you actually do to solve the problem?

#Document: Explain your code for your future self and others.

#Functions, if used, must be documented with docstrings

#Your code style should match PEP 8, in general:

#snake_case for variables

#Indentation is with 4 spaces


#3-5 sentence paragraph for end-user on how to use program

#First This program will ask for the Name of the User and the day of the week.
#The function of this program is to print the name of the food special for that day. 
#The program also compare the length of the name and so define the meal for that name. 
#First: The program ask to the user "Please enter your name:" and the user should input his Name.
#Second: The program ask to The user "Please enter the day of the week (Mon, Tue, Wed, Thu, Fri):" and the user should input the day of the week as asked "(Mon, Tue, Wed, Thu, Fri):"
#Third: The program will print select and print the Day and name as follow: "The special for", day, "is", meal"



#create main function


#create variables and prompt the user for the input
def get_specials():
    name = input("Please enter your name:")
    day = input("Please enter the day of the week (Mon, Tue, Wed, Thu, Fri):")
    meal = "meat"
    if day == "Mon":
        meal = "Spaghetti"
    if day == "Tue":
        meal = "Lasagna"
        if len(name)<5:
            meal = "Impossible Burger"
    if day == "Wed":
        meal = "Minestrone soup"
    if day == "Thu":
        meal = "Pot pie"
        if len(name)<5:
            meal = "Beyond Burger"
    if day == "Fri":
        meal = "Tacos"
    
    print ("The special for", day, "is", meal) 

get_specials()

            


