import pandas as pd
import sqlite3

# SQL QUERIES

QUERIES = {

    "expensive_books": """
        SELECT *
        FROM books
        WHERE price_gbp > 30
    """,

    "top_books": """
        SELECT *
        FROM books
        ORDER BY price_gbp DESC
        LIMIT 10
    """,

    "categories": """
        SELECT DISTINCT category_name
        FROM categories
    """,

    "price_range": """
        SELECT *
        FROM books
        WHERE price_gbp BETWEEN 20 AND 40
    """,

    "books_with_categories": """
        SELECT
            b.title,
            b.rating,
            b.price_inr,
            c.category_name
        FROM books b
        JOIN categories c
        ON b.category_id = c.category_id
    """
}


#CONNECT TO SQLITE DATABASE
connection = sqlite3.connect(
    "data_pipeline/zepto_books.db"
)



result = pd.read_sql(
    QUERIES["books_with_categories"],
    connection
)

print(result)

books_df = pd.read_sql(
    "SELECT * FROM books",
    connection
)

categories_df = pd.read_sql(
    "SELECT * FROM categories",
    connection
)

merged = pd.merge(
    books_df,
    categories_df,
    on="category_id",
    how="inner"
)

print(merged)