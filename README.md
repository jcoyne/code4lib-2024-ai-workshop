# code4lib-2024-ai-workshop
AI workshop for code4lib 2024

## Starting the database
* Start docker
* Open a terminal in this directory and start the database by running: `docker compose up db`

### What's included
* Postgres 15: https://postgresapp.com/
* pgvector: https://github.com/pgvector/pgvector#installation-notes

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

## Load data
```
docker compose up python
```

## Explore data

Which talk is the most similar to the first talk?
```
docker compose run db /usr/bin/psql postgres://root:password@db:5432/ai
```

https://github.com/pgvector/pgvector#querying


```
SELECT title FROM courses ORDER BY embedding <-> (SELECT embedding FROM courses LIMIT 1) LIMIT 5;
```