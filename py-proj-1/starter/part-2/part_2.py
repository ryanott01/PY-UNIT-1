### Step 1 - Lists ###

# Fill in this list with several authors you are a fan of. At least 7 or 8 should do.
my_authors = ["joe shmoe", "jesus christ", "willie wonka"]

# Now let's add a new author to the end with the .append() method. Type your code below.

my_authors.append("Ryan Ott")
# Example: my_authors.append("H.G. Wells")


# Now let's remove an element in the list

my_authors.remove("Ryan Ott")
# Example: my_authors.remove("H.G. Wells")


# Now access an element by it's index. (Remember it indexes start at 0.)

my_authors[2]
# Example: my_authors[2]


# Now slice the list.

my_authors[1:2]
# Example: my_authors[1:4]


### Step 2 - Tuples ###


# Create your tuple below. Assign it to a variable name you can reference later in the exercise.

my_musician_tuple = ("Lochie Keogh", "Aidan Holmes", "Jamie Hails", "Kurt Cobain", "Corey Taylor", "Dave Grohl", "Jacques Offenbach")
# Example: my_author_tuple = ("F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury")


### Step 3 - Sets ###

# Create a set with your authors.

my_musician_set = {"Lochie Keogh", "Aidan Holmes", "Jamie Hails", "Kurt Cobain", "Corey Taylor", "Dave Grohl", "Jacques Offenbach"}
# Example: my_author_set = {"F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury"}


# Add a new author to your set.

my_musician_set.add("Jimi Hendrix")
# Example: my_author_set.add("J.R.R. Tolkien")


# Try adding the same author again, and be sure to print your set.

my_musician_set.add("Jimi Hendrix")

print(my_musician_set)
# Example: my_author_set.add("J.R.R. Tolkien")



### Step 4 - For Loops ###

# Create a for-loop for each of the data-structures above.

for artist in my_musician_set:
    print(artist)

for artist in my_musician_tuple:
    print(artist)

# Example:

# for book in my_authors:
    # print(book)

# for book in my_authors_tuple:
    # print(book)

# for book in my_authors_set:
    # print(book)

