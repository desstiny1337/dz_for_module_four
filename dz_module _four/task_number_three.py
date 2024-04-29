
def parse_input(user_input):
    # Dividing line to command and arguments
    parts = user_input.strip().lower().split()
    command = parts[0]
    args = parts[1:]

    return command, args

def add_contact(name, phone_number, contacts):
    # Add a new contact to dictionary contacts
    contacts[name] = phone_number
    print("Contact added.")

def change_contact(name, new_phone_number, contacts):
    #  Changing already existing number
    if name in contacts:
        contacts[name] = new_phone_number
        print("Contact updated.")
    else:
        print("Contact not found.")

def show_phone(name, contacts):
    # Displaying number for contact
    if name in contacts:
        print(contacts[name])
    else:
        print("Contact not found.")

def show_all(contacts):
    # Displaying all numbers of contacts
    for name, phone_number in contacts.items():
        print(f"{name}: {phone_number}")

def main():
    contacts = {}  # Dict for contacts

    print("How can I help you?")

    while True:
        user_input = input("> ")

        # Parsing of entered string(line)
        command, args = parse_input(user_input)

        # Processing of various commands
        if command == "add":
            if len(args) == 2:
                add_contact(args[0], args[1], contacts)
            else:
                print("Invalid command format.")
        elif command == "change":
            if len(args) == 2:
                change_contact(args[0], args[1], contacts)
            else:
                print("Invalid command format.")
        elif command == "phone":
            if len(args) == 1:
                show_phone(args[0], contacts)
            else:
                print("Invalid command format.")
        elif command == "all":
            show_all(contacts)
        elif command == "exit" or command == "close":
            print("Good bye!")
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()