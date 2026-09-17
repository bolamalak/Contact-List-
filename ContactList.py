import json
import os

CONTACTS_FILE = "contacts.json"


def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return []

    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except Exception:
        return []


def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file)


def validate_phone(phone):
    if phone.startswith("+"):
        phone = phone[1:]

    return phone.isdigit() and 7 <= len(phone) <= 15


def validate_email(email):
    return email.count("@") == 1 and "." in email.split("@")[1]


def add_contact(contacts):
    name = input("Enter Name: ").strip()

    if not name:
        print("Name cannot be empty!")
        return

    phone = input("Enter Phone Number: ").strip()

    if not validate_phone(phone):
        print("Invalid phone number format!")
        return

    email = input("Enter Email Address: ").strip()

    if not validate_email(email):
        print("Invalid email format!")
        return

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })

    save_contacts(contacts)
    print("Contact added successfully!")

def search_contacts(contacts):
    search = input("Enter name or phone to search: ").strip().lower()

    results = [
        c for c in contacts
        if search in c["name"].lower() or search in c["phone"]
    ]

    if results:
        print("\n--- Search Results ---")

        for c in results:
            print(
                f"Name: {c['name']} | "
                f"Phone: {c['phone']} | "
                f"Email: {c['email']}"
            )
    else:
        print("No contacts found.")


def delete_contact(contacts):
    name = input("Enter exact Name of contact to delete: ").strip().lower()

    updated = [
        c for c in contacts
        if c["name"].lower() != name
    ]

    if len(updated) < len(contacts):
        save_contacts(updated)

        contacts.clear()
        contacts.extend(updated)

        print("Contact deleted successfully!")
    else:
        print("Contact not found.")


def view_contacts(contacts):
    if not contacts:
        print("\nNo contacts saved yet.")
        return

    print("\n--- Contact List ---")

    for c in contacts:
        print(
            f"Name: {c['name']} | "
            f"Phone: {c['phone']} | "
            f"Email: {c['email']}"
        )


def main():
    contacts = load_contacts()

    while True:
        print("\n--- Contact List Application ---")
        print("1. View All Contacts")
        print("2. Add Contact")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            view_contacts(contacts)

        elif choice == "2":
            add_contact(contacts)

        elif choice == "3":
            search_contacts(contacts)

        elif choice == "4":
            delete_contact(contacts)

        elif choice == "5":
            print("Exiting Contact Application. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter 1-5.")


main()