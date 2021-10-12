#create main function
def get_specials(prompt):
#user input as string value
    value = input(prompt)
    value = str(value)
    #return the value input
    return value 
#create variables and prompt the user for the input
name = get_specials("Please enter your name:")
day = get_specials("Please enter the day of the week (Mon, Tue, Wed, Thu, Fri):")

#Nested condition for the menu of the day given the selected day and length of the user name.
if day == "Mon":
    meal = "Spaghetti"
print ("The special for", day, "is", meal)   
    #if day == "Tue" and name.length < 5:
        #meal = "Impossible Burger"
# else: 
    # meal = "Lasagna"
    # if day == "Wed":
        # meal = "Minestrone soup"
            #if day == "Thu" and name.length < 5:
            # meal = "Pot pie"
            #else:
                #meal = "Beyond Burger"
                #if day == "Fri":
# meal = "Tacos"           
#Print the result to the user.         
