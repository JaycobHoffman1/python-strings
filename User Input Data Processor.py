user_inputs = []

# Task 1: Input Length Validator

print('Task 1: Input Length Validator')

while True:
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')

    if len(first_name) < 2 and len(last_name) < 2:
        print('Invalid first and last name. Please try again.')
    elif len(first_name) < 2:
        print('Invalid first name. Please try again.')
    elif len(last_name) < 2:
        print('Invalid last name. Please try again.')
    else:
        print('Your first and last name are valid!')
        user_inputs.append(first_name)
        user_inputs.append(last_name)
        break
    
        
# Task 2: Password Complexity Checker

print('Task 2: Password Complexity Checker')

def check_password_complexity(strng):
    alphabet_lowercase = 'qwertyuiopasdfghjklzxcvbnm'
    alphabet_uppercase = alphabet_lowercase.upper()
    nums = ''.join([str(i) for i in range(10)])

    def check_for_chars(char_strng):
        counter = 0

        for j in range(len(char_strng)):
            if char_strng[j] in strng:
                counter += 1

        return counter > 0
    
    return len(strng) >= 8 and check_for_chars(alphabet_lowercase)\
    and check_for_chars(alphabet_uppercase) and check_for_chars(nums)

while True:
    password = input('Enter a password: ')

    if check_password_complexity(password):
        print('Your password is valid!')
        user_inputs.append(password)
        break
    else:
        print(f'"{password}" is not a valid password. Your password must contain at least 8 characters, \
at least one uppercase letter, at least one lowercase letter, and at least one number.')


# Task 3: Email Formatter

print('Task 3: Email Formatter')

while True:
    email = input('Enter your personal email: ')

    if '@' in email and '@' != email[-5]\
    and '@' != email[0] and email[-4:] == '.com'\
    and ' ' not in email and email[email.index('@') + 1:-4] == email[email.index('@') + 1:-4].lower():
        print('Your email address is valid!')
        user_inputs.append(email)
        break
    else:
        print(f'"{email}" is not a valid email address. Please try again.')


# The following print statement prints all valid user inputs in a formatted manner.

print(f'User Inputs:\nFirst Name: {user_inputs[0]}\nLast Name: {user_inputs[1]}\n\
Password: {user_inputs[2]}\nEmail: {user_inputs[3]}')