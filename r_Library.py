class Library:
    __pri=[]
    def __init__(self, ListOfBooks, LibraryName):
        self.ListOfBooks = ListOfBooks
        self.LibraryName = LibraryName
    def displayBooks(self):
        print(f"Here's the list of Books:")
        j=1
        for i in self.ListOfBooks:
            print(f"({j})" + i);
            j += 1
    
    def returnBook(self, name, book):
        self.ListOfBooks.append(book);
        self._Library__pri.remove(f"{self.name}:{self.book}")

    def lendBook(self, name, book):
        for i in self.ListOfBooks:
            if book == i:
                self.ListOfBooks.remove(book)
                self._Library__pri.append(f"{self.name}:{self.book}")
                return 0
            else:
                continue  
        print('There is no such book present')
    def addBook(self,book):
        self.ListOfBooks.append(book)
        print(f"Thank you Sir")
        
Rakesh_Lib = Library(["Rose", "Physics", "Chemistry", "Mathematics", "BEE", "EME"], "Rakesh")

if __name__ == "__main__":
    while 1:
        name = input(f"Please enter your name sir:\t")
        print(f"How can we help you Sir?\n(1)Display all the books. \n(2)Lend a book. \n(3)Return a book. \n(4)Donate a Book. \n")
        var = int(input())

        if var==1:
            Rakesh_Lib.displayBooks()
        elif var==2:
            Book=input(f"Which Book would you like to lend:\t" )
            Rakesh_Lib.lendBook(name, Book)
        elif var==3:
            Book=input(f"Enter the name of the Book:\t")
            Rakesh_Lib.returnBook(name, Book)
        elif var==4:
            Book=input(f"Enter the name of the Book:\t")
            Rakesh_Lib.addBook(Book)
        print("\n")