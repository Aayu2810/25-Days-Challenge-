# 1. Create a way to store the data
db: dict[str, int] = dict()


# 2. Create an easy way to write system messages
def announcement(msg: str) -> None:
    print(f'System: {msg}')


# 3. Create the core functionality
def add_item() -> None:
    name: str = input('Enter an item: ').lower().strip()

    try:
        quantity: int = int(input('Enter a quantity: '))
        db[name] = quantity
        announcement(f'Added "{name}" x {quantity}')
    except ValueError:
        announcement('Error, please enter a valid number.')


def remove_item() -> None:
    name: str = input('Enter an item: ').lower().strip()
    try:
        db.pop(name)
        announcement(f'Successfully removed "{name}"')
    except KeyError:
        announcement(f'"{name}" not found in groceries.')


def read_list() -> None:
    if db:
        print('-' * 20)
        for k, v in db.items():
            print(f'{k.capitalize()}: {v}')

        print('-' * 20)
    else:
        announcement('There are no groceries to display.')


# 4. Create a menu for the user
def display_options() -> None:
    print('Options:')
    print('0 - Display options')
    print('1 - Read list')
    print('2 - Add to list')
    print('3 - Remove from list')
    print('_')


# 5. Get user input
def get_option(option: str) -> None:
    try:
        converted: int = int(option)
    except ValueError:
        announcement('Error, please enter a valid option.')
        return

    if converted == 0:
        display_options()
    elif converted == 1:
        read_list()
    elif converted == 2:
        add_item()
    elif converted == 3:
        remove_item()


# 6. Start and loop the program
def main() -> None:
    display_options()
    while True:
        user_input: str = input('You: ')
        get_option(user_input)


if __name__ == '__main__':
    main()

# Homework:
# 1. Make it so that if the user adds a wrong value for quantity, it allows them to try again
# immediately instead of asking them to enter the name and quantity again.
# 2. Add an option that allows the user to modify the quantity of any item.
