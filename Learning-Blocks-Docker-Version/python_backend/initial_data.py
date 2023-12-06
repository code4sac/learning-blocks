import logging

from db.init_db import init_db
from db.session import SessionLocal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init() -> None:
    """
    Initialize the database with example data.
    """
    db = SessionLocal()
    init_db(db)


def main() -> None:
    """
    This is the main function when run from the command line.
    """
    logger.info("Creating initial data")
    init()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
