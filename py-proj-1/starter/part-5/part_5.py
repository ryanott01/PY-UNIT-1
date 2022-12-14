### Step 1 - Store data in a 

## This step's instructions explains how to use the open() function, to write and read info from a  file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the  file properly formatted with commas as separators.

def create_new_book():
    title = input("\nWhat is the title of the book you would like to add? - ")
    author = input("Who is the author of the book you would like to add? - ")
    try:
        year = int(input("What year was this book published? - "))
    except:
        year = int(input("Please type a number? - "))
    try:
        rating = float(input("Rate the book out of 10"))
    except:
        rating = float(input("please type a number"))
    try:
        pages = int(input("How many pages or in the book?"))
    except:
        pages = int(input("please type a number"))

    with open("a_file.txt", "a") as file:
        file.write(f"{title}, {author}, {year}, {rating}, {pages}\n")



def get_books_as_list_of_dictionaries():
    books_list = []
    with open("a_file.txt", "r") as f:
        file = f.readlines()
        for line in file:
            title, author, year, rating, pages = line.split(", ")
            books_list.append({
                "title": title,
                "author": author,
                "year": int(year),
                "rating": float(rating),
                "pages": int(pages)
            })
    return books_list

def get_book_printed(book):
    print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Rating: {book['rating']}, Pages: {book['pages']}")


def view_books():
    print("\nHere are all your books...\n")
    for book in get_books_as_list_of_dictionaries():
        get_book_printed(book)


def alphabetically_sort():
    print("\nBooks Sorted alphabetically\n")
    list = (get_books_as_list_of_dictionaries())
    list = sorted(list, key=lambda x: str(x["title"]))
    for book in list:
        get_book_printed(book)


def search_for_book(search_input):
    print("results:")
    list = (get_books_as_list_of_dictionaries())
    for book in list:
        if book['title'] == search_input:
            get_book_printed(book)

def main_menu():

    active = True

    while active:
        choice = input("""
Choose 1 to add a book...
Choose 2 to see all your books...
Choose 3 to see a count of your books...
Choose 4 to sort books in alphabetical order...
Choose 5 search for a book
Choose 0 to exit.
Type here: """)

        if choice == "1":
            create_new_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            print(f"\nYou have a total of {len(get_books_as_list_of_dictionaries())} books.\n")
        elif choice == "4":
            alphabetically_sort()
        elif choice == "5":
            print("\n what are you looking for?\n")
            search = input()
            search_for_book(search)
        elif choice == "0":
            print("\nGoodbye")
            active = False
        else:
            print("\nSorry please type a number for one of the options.\n")

if __name__ == "__main__":
    main_menu()