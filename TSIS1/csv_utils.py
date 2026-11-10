
import csv
from connect import get_connection


def import_csv():
    try:
        with open("contacts.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            required_columns = [
                "first_name",
                "phone",
                "email",
                "birthday",
                "group",
                "phone_type"
            ]

            if not reader.fieldnames or not all(
                column in reader.fieldnames
                for column in required_columns
            ):
                print("Invalid CSV columns!")
                return

            conn = get_connection()

            try:
                for row_number, row in enumerate(reader, start=2):
                    try:
                        name = (row.get("first_name") or "").strip()
                        phone = (row.get("phone") or "").strip()
                        email = (row.get("email") or "").strip() or None
                        birthday = (row.get("birthday") or "").strip() or None
                        group_name = (row.get("group") or "").strip()
                        phone_type = (
                            row.get("phone_type") or "mobile"
                        ).strip().lower()

                        if not name or not phone:
                            print("Missing name or phone. Row:", row_number)
                            continue

                        if phone_type not in ("home", "work", "mobile"):
                            print("Invalid phone type. Row:", row_number)
                            continue

                        with conn:
                            with conn.cursor() as cur:

                                # Check duplicate phone
                                cur.execute("""
                                    SELECT id
                                    FROM contacts
                                    WHERE phone = %s

                                    UNION

                                    SELECT contact_id
                                    FROM phones
                                    WHERE phone = %s
                                    LIMIT 1
                                """, (phone, phone))

                                if cur.fetchone():
                                    print("Contact already exists:", name)
                                    continue

                                # Find group or use Other
                                cur.execute("""
                                    SELECT id
                                    FROM groups
                                    WHERE LOWER(name) = LOWER(%s)
                                """, (group_name,))

                                group = cur.fetchone()

                                if group:
                                    group_id = group[0]
                                else:
                                    cur.execute("""
                                        SELECT id
                                        FROM groups
                                        WHERE name = 'Other'
                                    """)
                                    group_id = cur.fetchone()[0]

                                # Add contact
                                cur.execute("""
                                    INSERT INTO contacts
                                        (first_name, phone, email,
                                         birthday, group_id)
                                    VALUES (%s, %s, %s, %s, %s)
                                    RETURNING id
                                """, (
                                    name,
                                    phone,
                                    email,
                                    birthday,
                                    group_id
                                ))

                                contact_id = cur.fetchone()[0]

                                # Add phone
                                cur.execute("""
                                    INSERT INTO phones
                                        (contact_id, phone, type)
                                    VALUES (%s, %s, %s)
                                """, (
                                    contact_id,
                                    phone,
                                    phone_type
                                ))

                        print("Imported:", name)

                    except Exception as error:
                        print("Error in row", row_number, ":", error)

            finally:
                conn.close()

        print("CSV import completed!")

    except FileNotFoundError:
        print("CSV file not found!")

    except Exception as error:
        print("Import error:", error)
