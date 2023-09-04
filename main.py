from flask import Flask, jsonify,request
from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import logging


app = Flask(__name__)

limiter = Limiter(get_remote_address,app=app)




books = [
            {"id": 1,"title": "The Great Gatsby",  "author": "F. Scott Fitzgerald"},
            {"id": 2, "title": "1984", "author": "George Orwell"},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"id": 4, "title": "1984", "author": "George Orwell"},
    {"id": 6, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"id": 7, "title": "1984", "author": "George Orwell"}, {"id": 1,"title": "The Great Gatsby",  "author": "F. Scott Fitzgerald"},
            {"id": 8, "title": "1984", "author": "George Orwell"}, {"id": 1,"title": "The Great Gatsby",  "author": "F. Scott Fitzgerald"},
            {"id": 9, "title": "1984", "author": "George Orwell"}, {"id": 1,"title": "The Great Gatsby",  "author": "F. Scott Fitzgerald"},
            {"id": 10, "title": "1984", "author": "George Orwell"}, {"id": 1,"title": "The Great Gatsby",  "author": "F. Scott Fitzgerald"},
            {"id": 11, "title": "1984", "author": "George Orwell"}, {"id": 1,"title": "The Great Gatsby",  "author": "F. Scott Fitzgerald"},
            {"id": 12, "title": "1984", "author": "George Orwell"},
{"id": 2, "title": "1984", "author": "George Orwell"}, {"id": 1,"title": "The Great Gatsby",  "author": "F. Scott Fitzgerald"},
            {"id": 2, "title": "1984", "author": "George Orwell"},
{"id": 2, "title": "1984", "author": "George Orwell"}, {"id": 1,"title": "The Great Gatsby",  "author": "F. Scott Fitzgerald"},
            {"id": 2, "title": "1984", "author": "George Orwell"},
{"id": 2, "title": "1984", "author": "George Orwell"}, {"id": 1,"title": "The Great Gatsby",  "author": "F. Scott Fitzgerald"},
            {"id": 2, "title": "1984", "author": "George Orwell"},
{"id": 2, "title": "1984", "author": "George Orwell"}, {"id": 1,"title": "The Great Gatsby",  "author": "F. Scott Fitzgerald"},
            {"id": 2, "title": "1984", "author": "George Orwell"},

        ]



@app.route('/api/books3', methods=['GET'])
def handle_books():
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))

    start_index = (page - 1) * limit
    end_index = start_index + limit
    paginated_books =  books[start_index:end_index]
    return jsonify(paginated_books)


@app.route('/api/books2', methods=['GET'])
def handle_books_query():
    author = request.args.get('author')

    if author:
        filtered_books = [book for book in books if book.get('author') == author]
        return jsonify(filtered_books)
    else:
        return jsonify(books)



@app.route('/api/books', methods=['GET'])
@limiter.limit("10/minute")  # Limit to 10 requests per minute
def handle_books1():
    # Handle the request logic
    return jsonify(books)


logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

@app.route('/api/books5', methods=['GET'])
def handle_books5():
    app.logger.info('GET request received for /api/books')  # Log a message

    # Handle the request logic
    return jsonify(books)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
