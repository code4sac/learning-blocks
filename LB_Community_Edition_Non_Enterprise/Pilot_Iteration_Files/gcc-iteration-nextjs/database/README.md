# Database

> [!IMPORTANT]  
> The database is currently using example data. Once we have a better understanding of the data we will update the database schema and drop the example tables.

## Quick Start

### Set Up Environment Variables:  

Create a .env file in the root of your project. Add the following environment variables:  

```dotenv
TURSO_CONNECTION_URL=your_connection_url
TURSO_AUTH_TOKEN=your_auth_token
```

### Configure Database Connection:  

Edit database/db.ts to set up the database connection using Drizzle.

### Define Database Schema:  

Edit database/schema.ts to define your database schema.

* Use utility functions from database/schemas/schemaFields.ts to define fields.

### Generate Database Migrations:  

Run the following command to generate database migrations:  

```shell
npm run db:generate
```

### Apply Migrations:  

Apply the generated migrations to your database:  

```shell
npm run db:migrate
```

### Seed Database:

TODO: Creating events and rsvps requires a user to be created first.

## File Structure

- `schema.ts`: Database schema referenced in [drizzle.config.ts](/drizzle.config.ts).
- `db.ts`: Database connection.
- `schemas/`: Database schema and utility files.

## Help

- [Database commands](doc/en/drizzle.md)
