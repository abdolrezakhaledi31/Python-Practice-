import sqlite3
import argparse


class Library:
    def __init__(self):
        self.conn = sqlite3.connect("jmaro_library.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS books(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            author TEXT,
            publisher TEXT,
            year INTEGER,
            volume INTEGER,
            number INTEGER,
            category TEXT
            )
        """)
        self.conn.commit()

    def add_book(self, name, author, publisher, year, volume, number, category):
        self.cursor.execute(
            """
        INSERT INTO books(name, author, publisher, year, volume, number, category)
        VALUES(?, ?, ?, ?, ?, ?, ?)
        """,
            (name, author, publisher, year, volume, number, category),
        )
        self.conn.commit()

    def count_book(self):
        self.cursor.execute("SELECT COUNT(*) FROM books")
        result = self.cursor.fetchone()
        return result[0]

    def search_book(self, name):
        self.cursor.execute("SELECT * FROM books WHERE LOWER(name) = LOWER(?)", (name,))
        return self.cursor.fetchone()

    def search_by_category(self, category):
        self.cursor.execute(
            "SELECT * FROM books WHERE LOWER(category) = LOWER(?)", (category,)
        )
        return self.cursor.fetchall()


def run_menu(jmaro_library):
    print(
        "========================\nWelcome to Jmaro library\n========================"
    )
    print(
        "Please choose\n1. Enter '1' for adding book\n2. Enter '2' for searching book\n3. Enter '3' for searching category\n4. Enter '4' for exit"
    )
    while True:
        choice = input("Please Enter 1 or 2 or 3 or 4: ")
        if choice == "1":
            new_name = input("Enter a name of book: ")
            new_author = input("Enter the name of author: ")
            new_publisher = input("Enter the name of publisher: ")
            new_year = int(input("Enter the year of publishe: "))
            new_volume = int(input("Enter count of volume: "))
            new_number = int(input("Enter number of copies: "))
            new_category = input("Enter the name of category: ")
            jmaro_library.add_book(
                new_name,
                new_author,
                new_publisher,
                new_year,
                new_volume,
                new_number,
                new_category,
            )

        elif choice == "2":
            search_name = input("Enter the name of book:")
            found_book = jmaro_library.search_book(search_name)
            if found_book:
                print(
                    found_book[1],
                    found_book[2],
                    found_book[3],
                    found_book[4],
                    found_book[5],
                    found_book[6],
                )
            else:
                print("No result")

        elif choice == "3":
            search_category = input(
                "Enter category(Computer or Literature or History): "
            )
            found_category = jmaro_library.search_by_category(search_category)
            if found_category:
                for book in found_category:
                    print(book[1], book[2], book[3], book[4], book[5], book[6], book[7])
            else:
                print("No result")

        elif choice == "4":
            print("Goodbye")
            break

        else:
            print("Enter correct number")


# ---- argparse ----
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command")

add_parser = subparsers.add_parser("add")
add_parser.add_argument("--name", required=True)
add_parser.add_argument("--author", required=True)
add_parser.add_argument("--publisher", required=True)
add_parser.add_argument("--year", type=int, required=True)
add_parser.add_argument("--volume", type=int, required=True)
add_parser.add_argument("--number", type=int, required=True)
add_parser.add_argument("--category", required=True)

search_parser = subparsers.add_parser("search")
search_parser.add_argument("--name", required=True)

category_parser = subparsers.add_parser("category")
category_parser.add_argument("--name", required=True)

args = parser.parse_args()


# ---- اجرای برنامه ----
jmaro_library = Library()
if jmaro_library.count_book() == 0:
    jmaro_library.add_book(
        "Harry Potter", "J.K. Rowling", "Bloomsbury", 2000, 1, 2, "Computer"
    )
    jmaro_library.add_book(
        "1984", "George Orwel", "Secker & Warburg", 1949, 1, 3, "Literature"
    )
    jmaro_library.add_book(
        "The Hobbit", "J.R.R. Tolkien", "Allen & Unwin", 1937, 1, 1, "History"
    )

if args.command is None:
    run_menu(jmaro_library)
elif args.command == "add":
    jmaro_library.add_book(
        args.name,
        args.author,
        args.publisher,
        args.year,
        args.volume,
        args.number,
        args.category,
    )
    print("Book added.")
elif args.command == "search":
    found_book = jmaro_library.search_book(args.name)
    if found_book:
        print(
            found_book[1],
            found_book[2],
            found_book[3],
            found_book[4],
            found_book[5],
            found_book[6],
        )
    else:
        print("No result")
elif args.command == "category":
    found_category = jmaro_library.search_by_category(args.name)
    if found_category:
        for book in found_category:
            print(book[1], book[2], book[3], book[4], book[5], book[6], book[7])
    else:
        print("No result")
