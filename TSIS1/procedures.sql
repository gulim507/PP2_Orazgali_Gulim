
-- TSIS1: Extended Contact Management
-- New procedures and function

-- 1. Add a phone number to an existing contact

CREATE OR REPLACE PROCEDURE add_phone(
    p_contact_name VARCHAR,
    p_phone VARCHAR,
    p_type VARCHAR
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_contact_id INTEGER;
BEGIN
    SELECT id INTO v_contact_id
    FROM contacts
    WHERE first_name = p_contact_name
    ORDER BY id
    LIMIT 1;

    IF v_contact_id IS NULL THEN
        RAISE EXCEPTION 'Contact not found';
    END IF;

    IF p_type NOT IN ('home', 'work', 'mobile') THEN
        RAISE EXCEPTION 'Invalid phone type';
    END IF;

    INSERT INTO phones(contact_id, phone, type)
    VALUES(v_contact_id, p_phone, p_type);
END;
$$;


-- 2. Move a contact to another group

CREATE OR REPLACE PROCEDURE move_to_group(
    p_contact_name VARCHAR,
    p_group_name VARCHAR
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_group_id INTEGER;
    v_contact_id INTEGER;
BEGIN
    SELECT id INTO v_contact_id
    FROM contacts
    WHERE first_name = p_contact_name
    ORDER BY id
    LIMIT 1;

    IF v_contact_id IS NULL THEN
        RAISE EXCEPTION 'Contact not found';
    END IF;

    INSERT INTO groups(name)
    VALUES(p_group_name)
    ON CONFLICT(name) DO NOTHING;

    SELECT id INTO v_group_id
    FROM groups
    WHERE name = p_group_name;

    UPDATE contacts
    SET group_id = v_group_id
    WHERE id = v_contact_id;
END;
$$;


-- 3. Search contacts by name, email or any phone number

CREATE OR REPLACE FUNCTION search_contacts(
    p_query TEXT
)
RETURNS TABLE (
    id INTEGER,
    first_name VARCHAR,
    email VARCHAR,
    birthday DATE,
    group_name VARCHAR,
    phone VARCHAR,
    phone_type VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT DISTINCT
        c.id,
        c.first_name,
        c.email,
        c.birthday,
        g.name,
        p.phone,
        p.type
    FROM contacts c
    LEFT JOIN groups g
        ON c.group_id = g.id
    LEFT JOIN phones p
        ON c.id = p.contact_id
    WHERE
        c.first_name ILIKE '%' || p_query || '%'
        OR COALESCE(c.email, '')
            ILIKE '%' || p_query || '%'
        OR COALESCE(p.phone, '')
            ILIKE '%' || p_query || '%'
    ORDER BY c.id;
END;
$$;
