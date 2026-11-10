
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
    except FileNotFoundError:
        print("JSON file not found!")
        return
    except json.JSONDecodeError:
        print("Invalid JSON file!")
        return

    for contact in contacts:
        name = contact["first_name"]

        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT id FROM contacts WHERE first_name = %s LIMIT 1",
                    (name,)
                )

                existing = cur.fetchone()

                if existing:
                    print("\nContact already exists:", name)
                    print("1. Skip")
                    print("2. Overwrite")

                    choice = input("Choose: ")

                    if choice == "1":
                        print("Skipped:", name)
                        continue

                    elif choice == "2":
                        contact_id = existing[0]

                        cur.execute("""
                            UPDATE contacts
                            SET email = %s,
                                birthday = %s,
                                group_id = (
                                    SELECT id FROM groups WHERE name = %s
                                )
                            WHERE id = %s
                        """, (
                            contact.get("email"),
                            contact.get("birthday"),
                            contact.get("group"),
                            contact_id
                        ))

                        cur.execute(
                            "DELETE FROM phones WHERE contact_id = %s",
                            (contact_id,)
                        )

                    else:
                        print("Invalid choice. Skipped.")
                        continue

                else:
                    if not contact.get("phones"):
                        print("No phone number for:", name)
                        continue

                    main_phone = contact["phones"][0]["phone"]

                    cur.execute("""
                        INSERT INTO contacts
                            (first_name, phone, email, birthday, group_id)
                        VALUES (
                            %s, %s, %s, %s,
                            (SELECT id FROM groups WHERE name = %s)
                        )
                        RETURNING id
                    """, (
                        name,
                        main_phone,
                        contact.get("email"),
                        contact.get("birthday"),
                        contact.get("group") or "Other"
                    ))

                    contact_id = cur.fetchone()[0]

                for phone in contact.get("phones", []):
                    cur.execute("""
                        INSERT INTO phones(contact_id, phone, type)
                        VALUES (%s, %s, %s)
                        ON CONFLICT DO NOTHING
                    """, (
                        contact_id,
                        phone["phone"],
                        phone["type"]
                    ))

    print("JSON import completed!")
