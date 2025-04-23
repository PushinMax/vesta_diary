CREATE TABLE IF NOT EXISTS records(
    id uuid default gen_random_uuid(),
    name varchar(20) not null,
    created_at TIMESTAMP default NOW(),
    marked boolean default false,
    content text
);