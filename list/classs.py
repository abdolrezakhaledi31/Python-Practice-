class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return "title = " + self.title +" "+ "- author = "+ self.author
    
class Ebook(Book):
    def __init__(self, title, author, size_book):
        super().__init__(title, author)
        self.size_book = size_book
    def __str__(self):
        return super().__str__() + " - size = " + self.size_book
        
    
book1 = Book("شازده کوچولو", "سنت اگزوپری")
print(book1)
ebook1 = Ebook("Atomic Habits", "James Clear", "2MB")
print(ebook1)