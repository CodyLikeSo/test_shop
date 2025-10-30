#!/usr/bin/env python
import os
import time
import psycopg2
from psycopg2 import OperationalError


def wait_for_db():
    """Wait for PostgreSQL to be available"""
    db_host = os.environ.get("POSTGRES_HOST", "db")
    db_port = os.environ.get("POSTGRES_PORT", 5432)
    db_name = os.environ.get("POSTGRES_DB")
    db_user = os.environ.get("POSTGRES_USER")
    db_password = os.environ.get("POSTGRES_PASSWORD")

    print("Waiting for PostgreSQL...")

    while True:
        try:
            conn = psycopg2.connect(
                host=db_host,
                port=db_port,
                dbname=db_name,
                user=db_user,
                password=db_password,
            )
            conn.close()
            print("PostgreSQL is available!")
            break
        except OperationalError:
            print("PostgreSQL is unavailable - sleeping")
            time.sleep(1)


if __name__ == "__main__":
    wait_for_db()
