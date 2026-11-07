
import csv
import json
from connect import get_connection


def search_contacts():
    pattern = input("Enter name or phone: ")

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM search_contacts(%s)",
                (pattern,)
            )

            for row in cur.fetchall():
                print(row)


def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "CALL upsert_contact(%s, %s)",
                (name, phone)
            )

    print("Contact saved!")


def import_contacts():
    contacts = []

    with open("contacts.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            contacts.append({
                "first_name": row["first_name"],
                "phone": row["phone"]
            })

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "CALL bulk_insert_contacts(%s::jsonb, %s::jsonb)",
                (json.dumps(contacts), "[]")
            )

            result = cur.fetchone()

    print("Invalid contacts:", result[0])


def show_contacts():
    limit = int(input("Contacts per page: "))
    page = int(input("Page number: "))

    offset = (page - 1) * limit

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM get_contacts_page(%s, %s)",
                (limit, offset)
            )

            for row in cur.fetchall():
                print(row)


def delete_contact():
    value = input("Enter name or phone: ")

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "CALL delete_contact(%s)",
                (value,)
            )

    print("Contact deleted!")


def main():

    while True:

        print("\n===== PHONEBOOK =====")
        print("1. Search contacts")
        print("2. Add or update contact")
        print("3. Import contacts from CSV")
        print("4. Show contacts")
        print("5. Delete contact")
        print("0. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            search_contacts()

        elif choice == "2":
            add_contact()

        elif choice == "3":
            import_contacts()

        elif choice == "4":
            show_contacts()

        elif choice == "5":
            delete_contact()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
