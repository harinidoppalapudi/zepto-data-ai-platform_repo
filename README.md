## Module 1 — Data Pipeline

### Overview

This module collects book data from Books to Scrape, cleans the data using Pandas, stores it in SQLite, and performs SQL and Pandas analysis.

### Pipeline

```text
Books to Scrape
      ↓
Requests + BeautifulSoup
      ↓
Raw Data
      ↓
Pandas Cleaning
      ↓
GBP → INR
      ↓
SQLite Database
      ↓
SQL Queries
      ↓
Pandas Analysis
```

### Technologies

* Python
* Requests
* BeautifulSoup
* Pandas
* SQLite
* SQL

### Data Collected

The scraper collects:

* Book title
* Price
* Star rating
* Availability
* Category

The scraper processes 3 categories:

* Travel
* Mystery
* Historical Fiction

**Total books collected: 69**

### Data Cleaning

The raw data is cleaned using Pandas:

* Convert GBP price to numeric
* Convert star ratings to numbers
* Convert availability to `True/False`
* Convert GBP price to INR
* Handle the `Â£` encoding issue

### GBP to INR Conversion

A fixed exchange rate of **1 GBP = 105.50 INR** is used as required by the project specification.
price_inr = price_gbp * 105.50
The project uses this fixed rate instead of a live exchange-rate API.


The final dataset contains:
title
price
star_rating
availability
category
price_gbp
rating
in_stock
price_inr

### SQLite Database

The cleaned data is stored in:

```text
data_pipeline/zepto_books.db
```

Two related tables are created:

```text
categories
│
└── category_id
      ↓
    books
```

* `categories.category_id` → Primary Key
* `books.book_id` → Primary Key
* `books.category_id` → Foreign Key

### SQL Analysis

The project contains 5 SQL queries:

1. Books priced above £30
2. Top 10 most expensive books
3. List all categories
4. Books priced between £20 and £40
5. Books with their categories using `JOIN`

SQL results are loaded into Pandas using:

```python
pd.read_sql()
```

The SQL JOIN is also reproduced using:

```python
pd.merge()
```

### Validation

The final dataset was checked for:

* Missing values
* Data types
* Ratings
* Stock status
* Category counts

Results:

```text
Books: 69
Categories: 3
Missing values: 0
```

### How to Run

Run the pipeline:

```bash
python3 data_pipeline/run_pipeline.py
```

Create/load the database:

```bash
python3 data_pipeline/load_database.py
```

Run SQL queries:

```bash
python3 data_pipeline/queries.py
```

### Module 1 Status

Complete
