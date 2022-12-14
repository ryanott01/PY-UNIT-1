
my_book = {
    "title": "Then Hunger Games",
    "author": "Suzanne Collins",
    "publish_year": 2008,
    "rating": 4.32,
    "pages": 374
}

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.




def book_info(book_name, info_type):
    ret = (book_name[info_type])
    return  ret
    



# Once you are finished with that function, create several more functions which return individual pieces of information from the book.


print(book_info(my_book, "author"))



# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.


from datetime import date

today = date.today()
year = today.strftime("%Y")

def book_age(book_name):
    book_year = book_info(book_name, "publish_year")
    return int(year) - int(book_year)
print(book_age(my_book))


#read_speed is pages per minute
def how_long_to_read(book_name, read_speed):
    net_minutes = book_info(book_name, "pages") / read_speed
    hours = round(net_minutes / 60)
    minutes = round(net_minutes % 60)
    return hours, minutes

input = how_long_to_read(my_book, 3)
print("it will take {} hours".format(input[0]),"and {} minutes.".format(input[1]))

