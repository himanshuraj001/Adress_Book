# Adress_Book
An API using FastAPI and SQLite to perform curd operations.

This API is a Address book in FastAPI which perform CURD Task and user can query the address nearby within a distance with provided range
for calculating distance I have used formula which is used to find distance between two points in line.

Databse used in this project is SQLite and name of database is address.db .

You can find the screenshot of results of API calls after making API calls in screenshot directory.

Directory tree:
Address_Book:
  |
  |---Screenshots : Contains screenshot of results in swagger GUI.
  |
  |---database.py : Contains SQLite connection and LocalSession setup.
  |
  |---models.py : contains Schema of Database with address table and column details.
  |
  |---main.py : Contains all code and logic of all operations performed by API.

You can execute this file with command : uvicron main:app --reload
within FASTAPI enviroment with SQlite3.
