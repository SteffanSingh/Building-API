from flask import Flask, jsonify,request

app = Flask(__name__)



books = [
            {"id": 1,"title": "The Great Gatsby",  "author": "F. Scott Fitzgerald"},
            {"id": 2, "title": "1984", "author": "George Orwell"},

        ]


def validate_book_data(data):
    if "title" not in data or "author" not in data:
        return False
    return True


@app.route('/api/books1', methods=['GET', 'POST'])
def books():
    if request.method == 'GET':
        # Handle the GET request
        # For now, we'll return a static list
        books = [
            {"id": 1,"title": "The Great Gatsby",  "author": "F. Scott Fitzgerald"},
            {"id": 2, "title": "1984", "author": "George Orwell"}
        ]
        return jsonify(books)


    elif request.method == 'POST':
        # Handle the POST request
        # For now, we'll just return the data the user sent
        # Later, we'll add code to save the new book in our data storage
        new_book = request.get_json()
        if not validate_book_data(new_book):
          return jsonify({"error": "Invalid book data"}), 400

        return jsonify(new_book), 201


@app.route('/api/books2', methods=['GET', 'POST'])
def handle_books():
    if request.method == 'POST':
        # Get the new book data from the client
        new_book = request.get_json()
        if not validate_book_data(new_book):
            return jsonify({"error": "Invalid book data"}), 400

        # Generate a new ID for the book
        new_id = max(book['id'] for book in books) + 1
        new_book['id'] = new_id

        # Add the new book to our list
        books.append(new_book)

        # Return the new book data to the client
        return jsonify(new_book), 201
    else:
        # Handle the GET request
        return jsonify(books)


def find_book_by_id(book_id):
    """ Find the book with the id `book_id`.
    If there is no book with this id, return None. """
    # TODO: implement this
    for book in books:
        if book["id"] == book_id:
            return book

    return None


@app.route('/api/books/<int:id>', methods=['PUT'])
def handle_book(id):
    # Find the book with the given ID
    book = find_book_by_id(id)

    # If the book wasn't found, return a 404 error
    if book is None:
        return '', 404

    # Update the book with the new data
    new_data = request.get_json()
    if not validate_book_data(new_data):
        return jsonify({"error": "Invalid book data"}), 400
    book.update(new_data)
    # Return the updated book
    return jsonify(book)





@app.route('/api/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    # Find the book with the given ID
    book = find_book_by_id(id)

    # If the book wasn't found, return a 404 error
    if book is None:
        return '', 404

    # Remove the book from the list
    # TODO: implement this
    books.remove(book)

    # Return the deleted book
    return jsonify(book)


@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Not Found"}), 404


@app.errorhandler(405)
def method_not_allowed_error(error):
    return jsonify({"error": "Method Not Allowed"}), 405


@app.route('/api/books3', methods=['GET'])
def handle_books_query():
    author = request.args.get('author')
    print(author)
    if author:
        filtered_books = [book for book in books  if book.get('author') == author]
        return jsonify(filtered_books)
    else:
        return jsonify(books)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)