# import sqlite3

# db = sqlite3.connect("Advanced/Day 63/practice/books-collection.db")
# cursor = db.cursor()

# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J.K.Rowling', '9.3')")
# db.commit()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)

class Book(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(250), unique=True, nullable=False)
  author = db.Column(db.String(250), nullable=False)
  rating = db.Column(db.Float, nullable=False)

  def __repr__(self):
    return f'Book {self.title}'

with app.app_context():
  db.create_all()

with app.app_context():
  new_book = Book(id=1,title="Harry Potter",author="J.K.Rowling",rating=9.3)
  db.session.add(new_book)
  db.session.commit()

with app.app_context():
  # Read all records
  result = db.session.execute(db.select(Book).order_by(Book.title))
  all_books = result.scalars()
  # Read particular record by query
  book = db.session.execute(db.select(Book).where(Book.title=="Harry Potter")).scalar()
  # Update particular record by query
  book.title = "Harry Potter and the Goblet of Fire"
  db.session.commit()
  # Delete particular record by primary key
  delete_book = db.session.execute(db.select(Book).where(Book.id==1)).scalar()
  db.session.delete(delete_book)
  db.session.commit()
