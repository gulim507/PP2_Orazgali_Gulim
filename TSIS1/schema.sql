-- TSIS1: Extended Contact Management

-- 1. Create groups table
CREATE TABLE IF NOT EXISTS groups (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);

-- 2. Insert default groups
INSERT INTO groups(name)
VALUES
    ('Family'),
    ('Work'),
    ('Friend'),
    ('Other')
ON CONFLICT (name) DO NOTHING;

-- 3. Extend contacts table
ALTER TABLE contacts
    ADD COLUMN IF NOT EXISTS email VARCHAR(100),
    ADD COLUMN IF NOT EXISTS birthday DATE,
    ADD COLUMN IF NOT EXISTS group_id INTEGER
        REFERENCES groups(id),
    ADD COLUMN IF NOT EXISTS created_at TIMESTAMP
        DEFAULT CURRENT_TIMESTAMP;

-- 4. Create phones table
CREATE TABLE IF NOT EXISTS phones (
    id SERIAL PRIMARY KEY,
    contact_id INTEGER NOT NULL
        REFERENCES contacts(id) ON DELETE CASCADE,
    phone VARCHAR(20) NOT NULL,
    type VARCHAR(10) NOT NULL
        CHECK (type IN ('home', 'work', 'mobile')),
    UNIQUE (contact_id, phone)
);

-- 5. Ensure unique phone numbers per contact
CREATE UNIQUE INDEX IF NOT EXISTS idx_phones_contact_phone
ON phones(contact_id, phone);

-- 6. Migrate old phone numbers from Practice 7/8
INSERT INTO phones(contact_id, phone, type)
SELECT id, phone, 'mobile'
FROM contacts
WHERE phone IS NOT NULL
ON CONFLICT (contact_id, phone) DO NOTHING;

-- 7. Assign default group to contacts without a group
UPDATE contacts
SET group_id = (
    SELECT id FROM groups WHERE name = 'Other'
)
WHERE group_id IS NULL;
