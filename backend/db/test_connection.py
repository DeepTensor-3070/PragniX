from sqlalchemy import text

from db.session import engine


def main():
    try:
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT DATABASE(), CURRENT_USER()")
            )
            database, user = result.fetchone()

            print("MySQL connection successful!")
            print(f"Database: {database}")
            print(f"User: {user}")

    except Exception as exc:
        print(f"MySQL connection failed: {exc}")


if __name__ == "__main__":
    main()