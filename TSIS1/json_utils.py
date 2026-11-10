
import json
from connect import get_connection


def export_contacts():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT
                    c.first_name,
                    c.email,
                    c.birthday,
                    g.name,
                    COALESCE(
                        json_agg(
                            json_build_object(
                                'phone', p.phone,
                                'type', p.type
                            )
                        ) FILTER (WHERE p.id IS NOT NULL),
                        '[]'::json
                    )
                FROM contacts c
                LEFT JOIN groups g ON c.group_id = g.id
                LEFT JOIN phones p ON c.id = p.contact_id
                GROUP BY c.id, g.name
                ORDER BY c.id
            """)

            rows = cur.fetchall()

    contacts = []

    for row in rows:
        contacts.append({
            "first_name": row[0],
            "email": row[1],
            "birthday": str(row[2]) if row[2] else None,
            "group": row[3],
            "phones": row[4]
        })

    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

    print("Contacts exported to contacts.json")


def import_contacts():
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)

        if not isinstance(contacts, list):
            print("Invalid JSON format!")
            return

    except FileNotFoundError:
        print("JSON file not found!")
        return

    except json.JSONDecodeError:
        print("Invalid JSON file!")
        return

    conn = get_connection()

    try:
        for contact in contacts:
            try:
                if not isinstance(contact, dict):
                    print("Invalid contact. Skipped.")
                    continue

                name = contact.get("first_name")

                if not name:
                    print("Contact without name. Skipped.")
                    continue

                group_name = contact.get("group") or "Other"

                phones = contact.get("phones") or []

                if not isinstance(phones, list):
                    print("Invalid phones for:", name)
                    continue

                valid_phones = []

                for phone in phones:
                    if not isinstance(phone, dict):
                        continue

                    number = phone.get("phone")
                    phone_type = phone.get("type", "mobile")

                    if not number:
                        continue

                    phone_type = str(phone_type).strip().lower()

                    if phone_type not in ("home", "work", "mobile"):
                        print("Invalid phone type for:", name)
                        continue

                    valid_phones.append((number, phone_type))

                with conn:
                    with conn.cursor() as cur:

                        # Find contact
                        cur.execute("""
                            SELECT id, phone
                            FROM contacts
                            WHERE first_name = %s
                            LIMIT 1
                        """, (name,))

                        existing = cur.fetchone()

                        if existing:
                            print("\nContact already exists:", name)
                            print("1. Skip")
                            print("2. Overwrite")

                            choice = input("Choose: ")

                            if choice == "1":
                                print("Skipped:", name)
                                continue

                            elif choice != "2":
                                print("Invalid choice. Skipped.")
                                continue

                            contact_id = existing[0]

                            if valid_phones:
                                main_phone = valid_phones[0][0]
                            else:
                                main_phone = existing[1]

                            cur.execute("""
                                INSERT INTO groups(name)
                                VALUES (%s)
                                ON CONFLICT (name) DO NOTHING
                            """, (group_name,))

                            cur.execute("""
                                SELECT id FROM groups
                                WHERE name = %s
                            """, (group_name,))

                            group_id = cur.fetchone()[0]

                            cur.execute("""
                                UPDATE contacts
                                SET phone = %s,
                                    email = %s,
                                    birthday = %s,
                                    group_id = %s
                                WHERE id = %s
                            """, (
                                main_phone,
                                contact.get("email"),
                                contact.get("birthday"),
                                group_id,
                                contact_id
                            ))

                            cur.execute("""
                                DELETE FROM phones
                                WHERE contact_id = %s
                            """, (contact_id,))

                        else:
                            if not valid_phones:
                                print("No phone number for:", name)
                                continue

                            main_phone = valid_phones[0][0]

                            cur.execute("""
                                INSERT INTO groups(name)
                                VALUES (%s)
                                ON CONFLICT (name) DO NOTHING
                            """, (group_name,))

                            cur.execute("""
                                SELECT id FROM groups
                                WHERE name = %s
                            """, (group_name,))

                            group_id = cur.fetchone()[0]

                            cur.execute("""
                                INSERT INTO contacts
                                    (first_name, phone, email,
                                     birthday, group_id)
                                VALUES (%s, %s, %s, %s, %s)
                                RETURNING id
                            """, (
                                name,
                                main_phone,
                                contact.get("email"),
                                contact.get("birthday"),
                                group_id
                            ))

                            contact_id = cur.fetchone()[0]

                        # Insert all phone numbers
                        for number, phone_type in valid_phones:
                            cur.execute("""
                                INSERT INTO phones
                                    (contact_id, phone, type)
                                VALUES (%s, %s, %s)
                                ON CONFLICT (contact_id, phone)
                                DO NOTHING
                            """, (
                                contact_id,
                                number,
                                phone_type
                            ))

                print("Imported:", name)

            except Exception as error:
                print("Error importing", name, ":", error)

        print("\nJSON import completed!")

    finally:
        conn.close()
