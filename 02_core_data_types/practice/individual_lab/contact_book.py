"""Individual Lab Work: Create a Contact Book program"""
import json

contact_book = {}  # Initialise empty contact book
# keys are contact names (strings)
# values are phone numbers and email (strings) in another dictionary
contact_book["Anton"] = {  # Add initial contact
    "phone": "07123456789",
    "email": "anton@example.com"
}


def add_contact(name, phone, email):
    """Add a new contact to the contact book."""
    contact_book[name] = {"phone": phone, "email": email}
    print(f"Contact {name} added.")
    # Add contact details as a nested dictionary


def look_up_contact(name):
    """Look up a contact by name and return their details."""
    return contact_book.get(name, "Contact not found.")
    # Return contact details or not found message


def delete_contact(name):
    """Delete a contact from the contact book."""
    if name in contact_book:  # Check if contact exists
        del contact_book[name]  # Delete contact
        return f"Contact {name} deleted."  # f is for formatted string
    return "Contact not found."


# Example usage
add_contact("Bob", "07333333333", "bob@example.com")
add_contact("Charlie", "07777777777", "charlie@example.com")
# {'phone': '07123456789', 'email': 'anton@example.com'}
print(look_up_contact("Anton"))
# {'phone': '07333333333', 'email': 'bob@example.com'}
print(look_up_contact("Bob"))
print(delete_contact("Anton"))  # Contact Anton deleted.
print(look_up_contact("Anton"))  # Contact not found.
print(contact_book)  # ? Output:
# {'Bob': {'phone': '07333333333', 'email': 'bob@example.com'},
# 'Charlie': {'phone': '07777777777', 'email': 'charlie@example.com'}}

# ! -------------------------------------------------------------

# ! Team Lab Work: Extend the Contact Book to save/load contact dictionaries & validate input data


def save_contacts(filename):
    """Save the contact book to a file in JSON format."""
    with open(filename, 'w', encoding='utf-8') as file:  # Open file for writing
        json.dump(contact_book, file)  # Save contact book as JSON
    print(f"Contacts saved to {filename}.")


def load_contacts(filename):
    """Load the contact book from a file in JSON format."""
    try:  # Try to open and read the file
        with open(filename, 'r', encoding='utf-8') as file:  # Open file for reading
            return json.load(file)  # Load contact book from JSON
    except FileNotFoundError:  # Handle file not found error
        print(f"File {filename} not found. Starting with an empty contact book.")
        return {}  # Return empty contact book if file not found


def is_valid_phone(phone):
    """Validate that the phone number contains only digits."""
    return phone.isdigit()  # Check if all characters are digits


def is_valid_email(email):
    """Validate that the email contains an '@' symbol."""
    return "@" in email  # Check if '@' is in the email string


def add_contact_validated(name, phone, email):
    """Add a new contact with validated phone and email."""
    if not is_valid_phone(phone):  # Validate phone number
        print("Invalid phone number. It should contain only digits.")
        return
    if not is_valid_email(email):  # Validate email address
        print("Invalid email address. It should contain an '@' symbol.")
        return
    add_contact(name, phone, email)  # Call original add_contact function


# Example usage of save/load and validation
# Invalid phone number
add_contact_validated("David", "07ABCD", "david@example.com")
add_contact_validated("Frank", "07888888888",
                      "frankexample.com")  # Invalid email address
add_contact_validated("Eve", "07666666666",
                      "eve@example.com")  # Contact Eve added
save_contacts("contacts.json")  # Contacts saved to contacts.json.
load_contacts("contacts.json")
contact_book = load_contacts("contacts.json")  # Load contacts at start
print(contact_book)  # Output the entire contact book after loading
# ? JSON output:
# {"Bob": {"phone": "07333333333", "email": "bob@example.com"},
# "Charlie": {"phone": "07777777777", "email": "charlie@example.com"},
# "Eve": {"phone": "07666666666", "email": "eve@example.com"}}
