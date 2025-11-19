from datetime import datetime


# Helper function that makes it easier to check whether there's
# a term in a sentence
def contains(terms: list[str], content: str) -> bool:
    matches: list[bool] = []
    for term in terms:
        matches.append(term in content.lower())

    return any(matches)


# Check for the appropriate response
def response(text: str) -> str:
    text = text.lower()

    if contains(['hello', 'hi'], text):
        return 'Hello there!'
    elif contains(['goodbye', 'bye'], text):
        return 'Talk to you later!'
    elif contains(['what time is it', 'current time'], text):
        return f'The time is: {datetime.now()}'
    else:
        return 'Sorry... I can\'t answer that right now.'


# Infinite loop
while True:
    user_input: str = input('You: ')
    print(f'Bot: {response(user_input)}')

# Homework:
# 1. Add your own custom responses to the bot!
