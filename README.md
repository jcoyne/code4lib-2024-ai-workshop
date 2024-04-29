# code4lib-2024-ai-workshop

AI workshop for code4lib 2024

## Starting the database

- Start docker
- Open a terminal in this directory and start the database by running: `docker compose up db`

### What's included

- Postgres 15: https://postgresapp.com/
- pgvector: https://github.com/pgvector/pgvector#installation-notes

## Create the table

Open another terminal in this directory and run: `docker compose run db /usr/bin/psql postgres://root:password@db:5432/ai`

1. Enable pgvector: `CREATE EXTENSION vector;`
2. Create a table for your data:

```sql
CREATE TABLE courses(id SERIAL PRIMARY KEY,
  title       varchar(200),
  description text,
  embedding   vector(384));
```

3. `\q` to quit psql.
