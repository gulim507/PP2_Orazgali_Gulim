
from connect import get_connection


def show_contacts():
    print("\n===== SORT CONTACTS =====")
    print("1. Sort by name")
    print("2. Sort by birthday")
    print("3. Sort by date added")

    choice = input("Choose sorting: ")

    if choice == "1":
        sort_by = "name"
    elif choice == "2":
        sort_by = "birthday"
    elif choice == "3":
        sort_by = "created_at"
    else:
        print("Invalid choice!")
        return

    limit = 3
    page = 1

    while True:
        offset = (page - 1) * limit

        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT * FROM get_contacts_page(%s, %s, %s)",
                    (limit, offset, sort_by)
                )
                contacts = cur.fetchall()

                cur.execute("SELECT COUNT(*) FROM contacts")
                total = cur.fetchone()[0]

        print("\n===== CONTACTS =====")

        for contact in contacts:
            print("ID:", contact[0])
            print("Name:", contact[1])
            print("Phone:", contact[2])
            print("Birthday:", contact[3])
            print("Date added:", contact[4])
            print("--------------------")

        total_pages = (total + limit - 1) // limit

        print("\nPage:", page, "of", total_pages)
        print("N - Next page")
        print("P - Previous page")
        print("Q - Quit")

        command = input("Choose: ").lower()

        if command == "n":
            if page < total_pages:
                page += 1
            else:
                print("This is the last page.")
        elif command == "p":
            if page > 1:
                page -= 1
            else:
                print("This is the first page.")
        elif command == "q":
            break
        else:
            print("Invalid choice!")


def filter_by_group():
    print("\n===== CONTACT GROUPS =====")
    print("1. Family")
    print("2. Work")
    print("3. Friend")
    print("4. Other")

    choice = input("Choose group: ")

    groups = {
        "1": "Family",
        "2": "Work",
        "3": "Friend",
        "4": "Other"
    }

    if choice not in groups:
        print("Invalid choice!")
        return

    group_name = groups[choice]
    limit = 3
    page = 1

    while True:
        offset = (page - 1) * limit

        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT * FROM get_contacts_by_group(%s, %s, %s)",
                    (group_name, limit, offset)
                )
                contacts = cur.fetchall()

                cur.execute(
                    """
                    SELECT COUNT(*)
                    FROM contacts c
                    JOIN groups g ON c.group_id = g.id
                    WHERE g.name = %s
                    """,
                    (group_name,)
                )
                total = cur.fetchone()[0]

        print("\n===== ", group_name.upper(), " =====")

        if not contacts:
            print("No contacts in this group.")
        else:
            for contact in contacts:
                print("ID:", contact[0])
                print("Name:", contact[1])
                print("Phone:", contact[2])
                print("Email:", contact[3])
                print("Group:", contact[4])
                print("--------------------")

        total_pages = (total + limit - 1) // limit

        print("\nPage:", page, "of", total_pages)
        print("N - Next page")
        print("P - Previous page")
        print("Q - Quit")

        command = input("Choose: ").lower()

        if command == "n":
            if page < total_pages:
                page += 1
            else:
                print("This is the last page.")
        elif command == "p":
            if page > 1:
                page -= 1
            else:
                print("This is the first page.")
        elif command == "q":
            break
        else:
            print("Invalid choice!")


def search_contacts_menu():
    query = input("Enter name, email or phone: ")

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM search_contacts(%s)",
                (query,)
            )
            contacts = cur.fetchall()

    print("\n===== SEARCH RESULTS =====")

    if not contacts:
        print("No contacts found.")
        return

    for contact in contacts:
        print("ID:", contact[0])
        print("Name:", contact[1])
        print("Email:", contact[2])
        print("Birthday:", contact[3])
        print("Group:", contact[4])
        print("Phone:", contact[5])
        print("Phone type:", contact[6])
        print("--------------------")

def add_phone_menu():
    print("\n===== ADD PHONE =====")

    contact_name = input("Enter contact name: ")
    phone = input("Enter new phone number: ")

    print("Phone types: home, work, mobile")
    phone_type = input("Enter phone type: ").lower()

    if phone_type not in ("home", "work", "mobile"):
        print("Invalid phone type!")
        return

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "CALL add_phone(%s, %s, %s)",
                    (contact_name, phone, phone_type)
                )

        print("Phone added successfully!")

    except Exception as error:
        print("Error:", error)


def move_contact_menu():
    print("\n===== MOVE CONTACT TO GROUP =====")

    contact_name = input("Enter contact name: ")

    print("1. Family")
    print("2. Work")
    print("3. Friend")
    print("4. Other")

    choice = input("Choose new group: ")

    groups = {
        "1": "Family",
        "2": "Work",
        "3": "Friend",
        "4": "Other"
    }

    if choice not in groups:
        print("Invalid group!")
        return

    group_name = groups[choice]

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "CALL move_to_group(%s, %s)",
                    (contact_name, group_name)
                )

        print("Contact moved successfully!")

    except Exception as error:
        print("Error:", error)







def main():
    while True:
        print("\n========== PHONEBOOK ==========")
        print("1. Show contacts")
        print("2. Filter by group")
        print("3. Search contacts")
        print("4. Add phone")
        print("5. Move contact to group")
        print("6. Export contacts to JSON")
        print("7. Import contacts from JSON")
        print("8. Import contacts from CSV")
        print("0. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            show_contacts()
        elif choice == "2":
            filter_by_group()
        elif choice == "3":
            search_contacts_menu()
        elif choice == "4":
            add_phone_menu()
        elif choice == "5":
            move_contact_menu()
        elif choice == "6":
            from json_utils import export_contacts
            export_contacts()
        elif choice == "7":
            from json_utils import import_contacts
            import_contacts()
        elif choice == "8":
            from csv_utils import import_csv
            import_csv()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
