
import psycopg2
import csv
from pathlib import Path
from connect import get_connection


# 1. Create contacts table

def create_table():
    conn = get_connection()

    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS contacts (
                        id SERIAL PRIMARY KEY,
                        first_name VARCHAR(100) NOT NULL,
                        phone VARCHAR(30) UNIQUE NOT NULL
                    )
                """)

        print("Contacts table created successfully!")

    finally:
        conn.close()


# 2. Insert a new contact from console

def insert_contact():
    name = input("Enter first name: ")
    phone = input("Enter phone number: ")

    conn = get_connection()

    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO contacts (first_name, phone)
                    VALUES (%s, %s)
                    ON CONFLICT (phone) DO NOTHING
                    """,
                    (name, phone)
                )

                if cur.rowcount == 1:
                    print("Contact added successfully!")
                else:
                    print("This phone number already exists!")

    finally:
        conn.close()


# 3. Import contacts from CSV

def import_csv():
    file_path = Path(__file__).with_name("contacts.csv")

    conn = get_connection()

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            with conn:
                with conn.cursor() as cur:
                    for row in reader:
                        cur.execute(
                            """
                            INSERT INTO contacts (first_name, phone)
                            VALUES (%s, %s)
                            ON CONFLICT (phone) DO NOTHING
                            """,
                            (row["first_name"], row["phone"])
                        )

        print("CSV data imported successfully!")

    finally:
        conn.close()


# 4. Display all contacts

def show_contacts():
    conn = get_connection()

    try:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM contacts ORDER BY id"
            )

            rows = cur.fetchall()

            if not rows:
                print("PhoneBook is empty!")
            else:
                for row in rows:
                    print(row)

    finally:
        conn.close()


# 5. Search contacts

def search_contacts():
    print("1. Search by name")
    print("2. Search by phone prefix")

    choice = input("Choose search type: ")

    conn = get_connection()

    try:
        with conn.cursor() as cur:

            if choice == "1":
                name = input("Enter name: ")

                cur.execute(
                    """
                    SELECT * FROM contacts
                    WHERE first_name ILIKE %s
                    """,
                    ("%" + name + "%",)
                )

            elif choice == "2":
                prefix = input("Enter phone prefix: ")

                cur.execute(
                    """
                    SELECT * FROM contacts
                    WHERE phone LIKE %s
                    """,
                    (prefix + "%",)
                )

            else:
                print("Invalid choice!")
                return

            rows = cur.fetchall()

            if rows:
                for row in rows:
                    print(row)
            else:
                print("No contacts found!")

    finally:
        conn.close()


# 6. Update contact

def update_contact():
    contact_id = input("Enter contact ID: ")

    print("1. Update first name")
    print("2. Update phone number")

    choice = input("Choose what to update: ")

    if choice == "1":
        new_value = input("Enter new first name: ")
        column = "first_name"

    elif choice == "2":
        new_value = input("Enter new phone number: ")
        column = "phone"

    else:
        print("Invalid choice!")
        return

    conn = get_connection()

    try:
        with conn:
            with conn.cursor() as cur:
                query = f"""
                    UPDATE contacts
                    SET {column} = %s
                    WHERE id = %s
                """

                cur.execute(query, (new_value, contact_id))

                if cur.rowcount == 1:
                    print("Contact updated successfully!")
                else:
                    print("Contact not found!")

    finally:
        conn.close()


# 7. Delete contact

def delete_contact():
    print("1. Delete by username")
    print("2. Delete by phone number")

    choice = input("Choose delete type: ")

    conn = get_connection()

    try:
        with conn:
            with conn.cursor() as cur:

                if choice == "1":
                    name = input("Enter first name: ")

                    cur.execute(
                        """
                        DELETE FROM contacts
                        WHERE first_name ILIKE %s
                        """,
                        (name,)
                    )

                elif choice == "2":
                    phone = input("Enter phone number: ")

                    cur.execute(
                        """
                        DELETE FROM contacts
                        WHERE phone = %s
                        """,
                        (phone,)
                    )

                else:
                    print("Invalid choice!")
                    return

                print(cur.rowcount, "contact(s) deleted!")

    finally:
        conn.close()


# 8. Main menu

def main():
    create_table()

    while True:
        print("\n========== PHONEBOOK ==========")
        print("1. Add contact")
        print("2. Import contacts from CSV")
        print("3. Show all contacts")
        print("4. Search contacts")
        print("5. Update contact")
        print("6. Delete contact")
        print("0. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                insert_contact()

            elif choice == "2":
                import_csv()

            elif choice == "3":
                show_contacts()

            elif choice == "4":
                search_contacts()

            elif choice == "5":
                update_contact()

            elif choice == "6":
                delete_contact()

            elif choice == "0":
                print("Goodbye!")
                break

            else:
                print("Invalid option!")

        except psycopg2.Error as error:
            print("Database error:", error)


if __name__ == "__main__":
    main()
