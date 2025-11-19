# 1. Display the options
def display_menu() -> None:
    print('Note-Taking Application')
    print('1. Add a Note')
    print('2. View Notes')
    print('3. Delete a Note')
    print('4. Exit')


# 2. Add new notes
def add_note() -> None:
    note: str = input('Enter your note: ')
    with open('notes.txt', 'a') as file:
        file.write(f'{note}\n')
    print('Note added successfully.')


# 3. Shows all the currents notes
def view_notes() -> None:
    try:
        with open('notes.txt', 'r') as file:
            notes: list[str] = file.readlines()
        if notes:
            print('\nYour Notes:')
            for i, note in enumerate(notes, start=1):
                print(f'{i}. {note.strip()}')
        else:
            print('No notes found.')
    except FileNotFoundError:
        print('No notes found.')


# 4. Delete notes
def delete_note() -> None:
    view_notes()
    try:
        with open('notes.txt', 'r') as file:
            notes: list[str] = file.readlines()
        if notes:
            note_num: int = int(input('Enter the note number to delete: '))
            if (
                1 <= note_num <= len(notes)
            ):  # make sure user enters a correct line number
                del notes[note_num - 1]  # delete correct index
                with open('notes.txt', 'w') as file:
                    file.writelines(notes)
                print('Note deleted successfully.')
            else:
                print('Invalid note number.')
    except FileNotFoundError:
        print('No file found...')  # Updated this!
    except ValueError:
        print('Please enter a valid number.')


# 5. Run the app
def main() -> None:
    while True:
        display_menu()
        choice: str = input('Choose an option: ')
        if choice == '1':
            add_note()
        elif choice == '2':
            view_notes()
        elif choice == '3':
            delete_note()
        elif choice == '4':
            print('Exiting the application.')
            break
        else:
            print('Invalid choice. Please try again.')


if __name__ == '__main__':
    main()
