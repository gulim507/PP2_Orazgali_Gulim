
-- 1. Search contacts by name or phone

CREATE OR REPLACE FUNCTION search_contacts(p_pattern TEXT)
RETURNS TABLE (
    id INTEGER,
    first_name VARCHAR,
    phone VARCHAR
)
AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, c.first_name, c.phone
    FROM contacts c
    WHERE c.first_name ILIKE '%' || p_pattern || '%'
       OR c.phone ILIKE '%' || p_pattern || '%';
END;
$$ LANGUAGE plpgsql;


-- 2. Get contacts with pagination

CREATE OR REPLACE FUNCTION get_contacts_page(
    p_limit INTEGER,
    p_offset INTEGER
)
RETURNS TABLE (
    id INTEGER,
    first_name VARCHAR,
    phone VARCHAR
)
AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, c.first_name, c.phone
    FROM contacts c
    ORDER BY c.id
    LIMIT GREATEST(p_limit, 1)
    OFFSET GREATEST(p_offset, 0);
END;
$$ LANGUAGE plpgsql;
