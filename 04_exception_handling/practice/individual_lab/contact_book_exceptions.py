"""Individual Lab Work: Extend the Contact Book with Exception Handling"""
import json

# Previous Contact Book from Data Handling Module
contact_book = {} 
contact_book["Anton"] = {
    "phone": "07123456789",
    "email": "anton@example.com"
}

def add_contact(name, phone, email):
    """Add a new contact to the contact book."""
    contact_book[name] = {"phone": phone, "email": email}
    print(f"Contact {name} added.")

def look_up_contact(name):
    """Look up a contact by name and return their details."""
    return contact_book.get(name, "Contact not found.")

def delete_contact(name):
    """Delete a contact from the contact book."""
    if name in contact_book:
        del contact_book[name]
        return f"Contact {name} deleted."
    return "Contact not found."

add_contact("Bob", "07333333333", "bob@example.com")
add_contact("Charlie", "07777777777", "charlie@example.com")
print(look_up_contact("Anton")) # {'phone': '07123456789', 'email': 'anton@example.com'}
print(look_up_contact("Bob")) # {'phone': '07333333333', 'email': 'bob@example.com'}
print(delete_contact("Anton")) # Contact Anton deleted.
print(look_up_contact("Anton")) # Contact not found.
print(contact_book)  # Output the entire contact book
# Output:
# {'Bob': {'phone': '07333333333', 'email': 'bob@example.com'},
# 'Charlie': {'phone': '07777777777', 'email': 'charlie@example.com'}}

def save_contacts(filename):
    """Save the contact book to a file in JSON format."""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(contact_book, file)
    print(f"Contacts saved to {filename}.")

def load_contacts(filename):
    """Load the contact book from a file in JSON format."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with an empty contact book.")
        return {}

def is_valid_phone(phone):
    """Validate that the phone number contains only digits."""
    return phone.isdigit()

def is_valid_email(email):
    """Validate that the email contains an '@' symbol."""
    return "@" in email

def add_contact_validated(name, phone, email):
    """Add a new contact with validated phone and email."""
    if not is_valid_phone(phone):
        print("Invalid phone number. It should contain only digits.")
        return
    if not is_valid_email(email):
        print("Invalid email address. It should contain an '@' symbol.")
        return
    if name in contact_book:
        try:
            raise KeyError(f"Contact '{name}' already exists.")
        except KeyError as e:
            print(e)
            return
    add_contact(name, phone, email)

add_contact_validated("David", "07ABCD", "david@example.com") # Invalid phone number
add_contact_validated("Frank", "07888888888", "frankexample.com") # Invalid email address
add_contact_validated("Eve", "07666666666", "eve@example.com") # Contact Eve added
add_contact_validated("Bob", "07999999999", "bob2@example.com") # Contact Bob already exists.
save_contacts("contacts.json") # Contacts saved to contacts.json.
load_contacts("contacts.json")
contact_book = load_contacts("contacts.json") # Load contacts at start
print(contact_book)  # Output the entire contact book after loading
# JSON output:
# {"Bob": {"phone": "07333333333", "email": "bob@example.com"},
# "Charlie": {"phone": "07777777777", "email": "charlie@example.com"},
# "Eve": {"phone": "07666666666", "email": "eve@example.com"}}
