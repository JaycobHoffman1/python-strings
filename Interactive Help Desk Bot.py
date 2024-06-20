# Task 1: Command Parser

print('Task 1: Command Parser')

commands = ['help', 'trouble', 'issue', 'assistance', 'problem', 'support']
replies = [
'If you need help, feel free to visit our online Help Center. There, you can search for what you need help with. \
If you cannot find what you are looking for at the Help Center, please contact support.',
'If you are having trouble, please visit our online Help Center and search for what you are having trouble with. \
If that doesn\'t solve your problem, feel free to contact support.',
'What kind of issue are you having?',
'If you need assistance, first try going to our online Help Center and searching for what you need assistance with. \
If you still need help, feel free to contact support.',
'I\'m sorry to hear you are having a problem. I would recommend searching for your problem at our online Help Center. \
Alternatively, you may contact support.',
'You may call support at (123) 456-7890 or email at support@email.com.'
]

commands2 = ['login', 'performance', 'error', 'password', 'email', 'subscription']
replies2 = [
'Ok! I will let the support team know that you are experiencing a login issue.',
'Alright! I will tell the support team that you are having a performance issue.',
'Thanks for letting me know! I will tell the support team that you are experiencing an error.',
'I\'m sorry to hear that. I will get in touch with the support team and let them you you are having an issue with your password.',
'Ok. I will let the support team know about your issue with your email.',
'Got it! I will tell the support team about your subscription issue.'
]

error_message = 'I\'m sorry, but I don\'t understand. Please try again.'

print('Hello! How might I be of assistance?')

while True:
    user_message = input('Enter message here (when you\'re ready to end the chat, type "done"): ')

    if user_message == 'done' or user_message == 'done'.upper() or user_message == 'done'.capitalize():
        break

    commands.append(user_message)
    replies.append(error_message)

    for i in range(len(commands)):
        command_detected = commands[i] in user_message or commands[i].capitalize() in user_message
        
        if command_detected and commands[i] == commands[2]:
            print(replies[i])
            commands, replies = commands2, replies2
            break
        elif command_detected:
            print(replies[i])
            break

print('Thank you! Glad I could help!')


print('Task 2: Issue Categorizer (see comment on line 58)')

'''
Task 2: Issue Categorizer

On line 45, I have included an if statement that checks whether the user's message contains the word "issue".
If it does, then on the while loop's next iteration, the chatbot searches for one of the commands specifically
related to the word "issue" and replies accordingly.
'''