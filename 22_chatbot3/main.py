from dataclasses import dataclass
import json
import re


# 1. Create the model
@dataclass
class Response:
    response: str
    words: list[str]
    required_words: list[str]


# 2. Load the data
def load_responses() -> list[Response]:
    responses: list[Response] = []
    with open('responses.json') as file:
        for response in json.load(file):
            responses.append(
                Response(
                    response['response'], response['words'], response['required_words']
                )
            )

    return responses


# 3. Helper function that processes text by splitting
# words into a list and lowering them
def split_text(text: str) -> list[str]:
    return re.split(r'\s+|[,;?!.-]\s*', text.lower())


# 4. Check how accurate the bot recognises the user's response
def match_rating(text: str, response: Response) -> float:
    text = text.lower()
    score: int = 0
    has_required_words: bool = True

    # Counts how many words match in the user's message vs the Response
    for word in split_text(text):
        if word in response.words:
            score += 1

    # Calculate the amount of words matched
    percent_matched: float = score / len(response.words)

    # Check whether the user's message includes all the words required to trigger a message
    if response.required_words:
        for word in response.required_words:
            if word not in text:
                has_required_words = False
                break

    # Return the score as a percent
    return percent_matched if has_required_words else 0


# 5. Get the response from the bot
def get_response(text: str, responses: list[Response]) -> str:
    matches: dict[str, float] = {}

    for response in responses:
        # Updates the dictionary to contain the score of each bot response in relation to our input
        matches[response.response] = match_rating(text, response)

    # Debugging
    # print(matches)

    # Checks all the keys and returns the one with the highest value
    best_match: str = max(matches, key=matches.get)  # type: ignore
    
    if matches[best_match] == 0:
        return 'I don\'t understand... [0%]'
    else:
        return f'{best_match} [{matches[best_match]:.0%}]'


# 6. Run the script and enjoy
def main() -> None:
    responses: list[Response] = load_responses()

    while True:
        user_input: str = input('You: ')
        print(f'Bot: {get_response(user_input, responses)}')


if __name__ == '__main__':
    main()

# Homework:
# 1. Add more responses to the chatbot.
# 2. Convert this code to use an OOP approach.
