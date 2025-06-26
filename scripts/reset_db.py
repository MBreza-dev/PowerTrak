#!/usr/bin/env python3
"""
Reset the database schema and seed it with initial data.
"""
from sqlmodel import SQLModel
from powertrak.db import engine
from powertrak.models import Customer, Equipment, Job
from scripts.seed_data import seed_database

# load model classes so metadata includes all tables
_ = (Customer, Equipment, Job)


def main() -> None:
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)
    seed_database()
    print("Database reset and seeded.")


if __name__ == "__main__":
    main()
