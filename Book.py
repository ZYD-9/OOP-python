class Book:
   #constructor of book
    def __init__(self,author,bookname):
        self.author = author
        self.bookname = bookname
    @classmethod
    def inputHeader(self):
        print("Insert the information of a book: ")
        print("----------------------------------------")
        print("Information of Book 1:")

    @classmethod
    def getInfo(self):
        bookname = input("Input title of the book: ")
        author = input("Input author of the book: ")
        return self(author, bookname)


    def displayBookinfo(self):
        print("Title = " + self.bookname + ", " + "Author = " + self.author)
    def addBook(newbook):
        newbook = input("Input new Book :  ")
        return newbook


#CALL functions
book = Book.inputHeader()
book = Book.getInfo()
book.displayBookinfo()
newbook = book.addBook()
print(newbook)

