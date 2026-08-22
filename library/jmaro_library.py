def create_book(name, author, publisher, years_of_publication, valume_count, number_of_copies):
    new_book = [name, author, publisher, years_of_publication, valume_count, number_of_copies]
    return new_book


book1 = create_book("Harry Potter", "J.K. Rowling", "Bloomsbury", 2000, 1, 2)
print(book1)