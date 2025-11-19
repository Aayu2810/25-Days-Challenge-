import json


# 1. Load the data
def load_exchange_rates() -> dict[str, float]:
    with open('currencies.json', 'r') as file:
        return json.load(file)


# 2. Create instructions
def instructions() -> None:
    print('1. Type <amount><CURRENCY>, e.g. 10USD, to convert a currency.')
    print('2. Type LIST to list available currencies.')
    print('3. Type QUIT to exit.')


def convert(user_input: str, rates: dict[str, float]) -> None:
    # Prepare data
    currency_codes: list[str] = list(rates.keys())
    input_currency_code: str = user_input[-3:]  # Gets the last three characters of a string

    # Check whether the user specifies a valid currency
    if input_currency_code not in currency_codes:
        print(f'Currency code: "{input_currency_code}" is invalid.')
        return

    # Check whether the specifies a valid amount
    try:
        input_amount: float = float(user_input[:-3])  # Gets everything besides the last three characters
    except ValueError:
        print(f'"{user_input}" is invalid. Try something like: "10 AUD"')
        return

    # Base conversion - USD is the base currency in the file so any currency we specify
    # will be converted to that first.
    base_conversion: float = input_amount / rates[input_currency_code]

    # Display the conversion
    print(f'{round(input_amount, 2):>16} {input_currency_code}')
    print('-' * 20)
    for currency_code in currency_codes:
        converted_amount: float = base_conversion * rates[currency_code]
        print(f'= {round(converted_amount, 2):>14} {currency_code}')
    print('-' * 20)


def main() -> None:
    # 1. Display instructions
    instructions()

    # 2. Load exchange rate data
    exchange_rates: dict[str, float] = load_exchange_rates()

    # 3. Run
    while True:
        user_input: str = input('Convert: ').upper().strip()

        if user_input == 'LIST':
            print(f'Available currencies: {', '.join(exchange_rates.keys())}')
            continue
        elif user_input == 'QUIT':
            print('Exiting.')
            break

        convert(user_input, exchange_rates)


if __name__ == '__main__':
    main()

# Homework:
# 1. Split "convert()" into two functions:
# - One that returns all the conversions as a dictionary.
# - One that displays the converted data.
