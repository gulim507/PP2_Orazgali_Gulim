
-- 1. Insert or update one contact

CREATE OR REPLACE PROCEDURE upsert_contact(
    p_name VARCHAR,
    p_phone VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM contacts
        WHERE first_name = p_name
    ) THEN

        UPDATE contacts
        SET phone = p_phone
        WHERE first_name = p_name;

    ELSE

        INSERT INTO contacts(first_name, phone)
        VALUES(p_name, p_phone);

    END IF;
END;
$$;


-- 2. Insert multiple contacts with validation

CREATE OR REPLACE PROCEDURE bulk_insert_contacts(
    IN p_contacts JSONB,
    INOUT p_invalid JSONB
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_item JSONB;
    v_name VARCHAR;
    v_phone VARCHAR;
BEGIN

    p_invalid := '[]'::JSONB;

    FOR v_item IN
        SELECT value FROM jsonb_array_elements(p_contacts)
    LOOP

        v_name := v_item->>'first_name';
        v_phone := v_item->>'phone';

        IF v_name IS NULL OR TRIM(v_name) = ''
           OR v_phone IS NULL
           OR v_phone !~ '^\+?[0-9]{10,15}$'
        THEN

            p_invalid := p_invalid || jsonb_build_array(v_item);

        ELSE

            BEGIN

                IF EXISTS (
                    SELECT 1 FROM contacts
                    WHERE first_name = v_name
                ) THEN

                    UPDATE contacts
                    SET phone = v_phone
                    WHERE first_name = v_name;

                ELSE

                    INSERT INTO contacts(first_name, phone)
                    VALUES(v_name, v_phone);

                END IF;

            EXCEPTION
                WHEN unique_violation THEN
                    p_invalid := p_invalid || jsonb_build_array(v_item);
            END;

        END IF;

    END LOOP;

END;
$$;


-- 3. Delete contact by name or phone

CREATE OR REPLACE PROCEDURE delete_contact(
    p_value VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN

    DELETE FROM contacts
    WHERE first_name = p_value
       OR phone = p_value;

END;
$$;
