import json
import os

print("========================\nWelcome to Jmaro library\n========================")
print("Please choose\n1. Enter '1' for adding book\n2. Enter '2' for searching book\n3. Enter '3' for searching category\n4. Enter '4' for exit")


class  Book:
    def __init__(self, name, author, publisher, years_of_publication, valume_count, number_of_copies, category):
        self.name = name
        self.author = author
        self.publisher = publisher
        self.year = years_of_publication
        self.valume = valume_count
        self.number = number_of_copies
        self.category = category


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, name, author, publisher, years_of_publication, valume_count, number_of_copies, category):
        new_book = Book(name, author, publisher, years_of_publication, valume_count, number_of_copies, category)
        self.books.append(new_book)
        self.save_to_file()

    def save_to_file(self):
        new_save = []
        for book in self.books:
            new_book = {"name": book.name, "author": book.author, "publisher": book.publisher, "year": book.year, "valume": book.valume, "number": book.number, "category": book.category}
            new_save.append(new_book)
        with open("jmaro_library.json", "w", encoding="utf-8") as file:
            json.dump(new_save, file, ensure_ascii=False, indent=4)

    def load_from_file(self):
        with open("jmaro_library.json", "r", encoding="utf-8") as file:
            loaded_data = json.load(file)
            for item in loaded_data:
                new_book = Book(item["name"], item["author"], item["publisher"], item["year"], item["valume"], item["number"], item["category"])
                self.books.append(new_book)

    def search_book(self, name):
        for book in self.books:
            if book.name.lower() == name.lower():
                return book

    def search_by_category(self, category):
        result = []
        for book in self.books:
            if book.category.lower() == category.lower():
                result.append(book)
        return result


jmaro_library = Library()
if os.path.exists("jmaro_library.json"):
    jmaro_library.load_from_file()
else:
    jmaro_library.add_book("Harry Potter", "J.K. Rowling", "Bloomsbury", 2000, 1, 2, "Computer")
    jmaro_library.add_book("1984", "George Orwel", "Secker & Warburg", 1949, 1, 3, "Literature")
    jmaro_library.add_book("The Hobbit", "J.R.R. Tolkien", "Allen & Unwin", 1937, 1, 1, "History")


while True:
    choice = input("Please Enter 1 or 2 or 3 or 4: ")
    if choice == "1":
        new_name = input("Enter a name of book: ")
        new_author = input("Enter the name of author: ")
        new_publisher = input("Enter the name of publisher: ")
        new_year = int(input("Enter the year of publishe: "))
        new_valume = int(input("Enter count of valume: "))
        new_number = int(input("Enter number of copies: "))
        new_category = input("Enter the name of category: ")
        jmaro_library.add_book(new_name, new_author, new_publisher, new_year, new_valume, new_number, new_category)

    elif choice == "2":
        search_book = input("Enter the name of book:")
        found_book = jmaro_library.search_book(search_book)
        if found_book:
            print(found_book.name, found_book.author, found_book.publisher, found_book.year, found_book.valume, found_book.number)
        else:
            print("No result")

    elif choice == "3":
        search_category = input("Enter category(Computer or Literature or History): ")
        found_category = jmaro_library.search_by_category(search_category)
        if found_category:
            for book in found_category:
                print(book.name, book.author, book.publisher, book.year, book.valume, book.category)
        else:
            print("No result")
    elif choice == "4":
        print("Goodbye")
        break
    else:
        print("Enter correct number")

# for book in jmaro_library.books:
#     print(book.name)