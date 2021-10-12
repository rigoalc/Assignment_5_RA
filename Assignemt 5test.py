def get_integer(prompt):
    """Prompt the user and return an integer"""
    # First get a string, using the provided prompt
    value = input(prompt)
    # Convert the string to an Integer
    value = int(value)
    # Give the Integer back to the caller
    return value

get_integer("enter integer")