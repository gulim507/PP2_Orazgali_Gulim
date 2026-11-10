
import csv
from connect import get_connection


def import_csv():
    try:
        with open("contacts.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                with get_connection() as conn:
                    with conn.cursor() as cur:

                        cur.execute(
                            "SELECT id FROM contacts WHERE phone = %s",
                            (row["phone"],)
                        )

                        if cur.fetchone():
                            print("Contact already exists:", row["first_name"])
                            continue

                        cur.execute("""
                            INSERT INTO contacts
                                (first_name, phone, email, birthday, group_id)
                            VALUES (
                                %s, %s, %s, %s,
                                (SELECT id FROM groups WHERE name = %s)
                            )
                            RETURNING id
                        """, (
                            row["first_name"],
                            row["phone"],
                            row["email"] or None,
                            row["birthday"] or None,
                            row["group"]
                        ))

                        contact_id = cur.fetchone()[0]

                        cur.execute("""
                            INSERT INTO phones(contact_id, phone, type)
                            VALUES (%s, %s, %s)
                        """, (
                            contact_id,
                            row["phone"],
                            row["phone_type"]
                        ))

                print("Imported:", row["first_name"])

        print("CSV import completed!")

    except FileNotFoundError:
        print("CSV file not found!")
    except Exception as error:
        print("Import error:", error)
