#Right here I imported the string
import string
#Here I define a function
def check_password_strength(password):
    #Here I just set the categories up instead of just ilterating through  a list I found this way easier instead of going line by line
    categories = [string.ascii_uppercase, string.ascii_lowercase, string.punctuation, string.digits]
    #Checking if password got spefic charcters
    characters = [any(c in category for c in password) for category in categories]
    #Checking the length of the password
    length = len(password)

    """Here I didn't really change anything I just linked it to my Common.txt file Note that I got the Common password list from year 2019 to 2021 
        Also this opens up the file and goes through the passwords in common.txt
    """
    with open('common.txt', 'r') as f:
        common_passwords = f.read().splitlines()
    #Checks if the password is common
    if password in common_passwords:
        return "Password is too weak, as it is in the common password list."
#This line calculates the score based on its length, the longer the password the bigger the score.
    score = sum(1 for threshold in [8, 12, 17, 20] if length > threshold)
#This line dectates if the password is valid or invalid
    if all(characters) and score >= 1:
        return f"Password is strong, with a score of {score}."
    else:
        return "Password is weak. Please use a combination of uppercase, lowercase, special characters, and digits."
#And this is asking the user for them to put in their password, this also prints the results.
user_password = input("Enter your password: ")
result = check_password_strength(user_password)
print(result)
