
-- Extended pagination with sorting
-- Reuses Practice8 pagination logic

DROP FUNCTION IF EXISTS get_contacts_page(
    INTEGER,
    INTEGER,
    TEXT
);

CREATE FUNCTION get_contacts_page(
    p_limit INTEGER,
    p_offset INTEGER,
    p_sort_by TEXT
)
RETURNS TABLE (
    id INTEGER,
    first_name VARCHAR,
    phone VARCHAR,
    birthday DATE,
    created_at TIMESTAMP
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF p_sort_by NOT IN ('name', 'birthday', 'created_at') THEN
        RAISE EXCEPTION 'Invalid sorting option';
    END IF;

    RETURN QUERY
    SELECT
        c.id,
        c.first_name,
        COALESCE(
            STRING_AGG(
                p.phone || ' (' || p.type || ')',
                ', ' ORDER BY p.id
            ),
            c.phone
        )::VARCHAR,
        c.birthday,
        c.created_at
    FROM contacts c
    LEFT JOIN phones p ON c.id = p.contact_id
    GROUP BY c.id
    ORDER BY
        CASE WHEN p_sort_by = 'name'
            THEN c.first_name END ASC,
        CASE WHEN p_sort_by = 'birthday'
            THEN c.birthday END ASC NULLS LAST,
        CASE WHEN p_sort_by = 'created_at'
            THEN c.created_at END ASC,
        c.id ASC
    LIMIT GREATEST(p_limit, 1)
    OFFSET GREATEST(p_offset, 0);
END;
$$;
CREATE OR REPLACE FUNCTION get_contacts_by_group(
    p_group_name VARCHAR,
    p_limit INTEGER,
    p_offset INTEGER
)
RETURNS TABLE (
    id INTEGER,
    first_name VARCHAR,
    phone VARCHAR,
    email VARCHAR,
    group_name VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        c.id,
        c.first_name,
        COALESCE(
            STRING_AGG(
                p.phone || ' (' || p.type || ')',
                ', ' ORDER BY p.id
            ),
            c.phone
        )::VARCHAR,
        c.email,
        g.name::VARCHAR
    FROM contacts c
    JOIN groups g ON c.group_id = g.id
    LEFT JOIN phones p ON c.id = p.contact_id
    WHERE g.name = p_group_name
    GROUP BY c.id, g.name
    ORDER BY c.first_name
    LIMIT GREATEST(p_limit, 1)
    OFFSET GREATEST(p_offset, 0);
END;
$$;