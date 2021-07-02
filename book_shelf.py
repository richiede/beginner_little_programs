# This script checks a book shelf for books and adds to it if the book isn't there

current_books = ['musashi', 'the universe in a nutshell', 'man\'s search for meaning', 'pulp fiction']  # defines the initial list

print('What book do you want to add?')
book = input()  # defines the book to add
if book not in current_books:  # check if the book exists. If not, it will add the book.
	current_books.append(book)
else:
	print('We already have that book')

for i in range(len(current_books)):  # prints out the list of books currently on the shelf
	print(f'Index {str(i)} is {current_books[i]}')
