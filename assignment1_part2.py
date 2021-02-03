class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title
        pass

    def display(self):
        print(f'{self.title}, written by {self.author}')


book1 = Book('John Steinbeck', 'Of Mice and Men')
book2 = Book('Harper Lee', 'To Kill a Mockingbird')

book1.display()
book2.display()


if __name__ == "__main__":
    pass
