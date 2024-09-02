from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from main import Base  # Ensure this import is correct and accessible
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get Alembic configuration
config = context.config

# Set the SQLAlchemy URL from the environment variable
config.set_main_option("sqlalchemy.url", os.environ.get("DATABASE_URL"))

# Configure logging if the config file is provided
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Set the target metadata for 'autogenerate' support
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()

# Determine which mode to use
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
