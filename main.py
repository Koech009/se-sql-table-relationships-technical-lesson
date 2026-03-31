import sqlite3
import pandas as pd
conn = sqlite3.connect('data.sqlite')

# step 2 one to many relationship
# sales rep employees
q = """
SELECT firstName, lastName, email
FROM employees
WHERE jobTitle = 'Sales Rep';
"""
df = pd.read_sql_query(q, conn)
# print(df)
# print("Number of results: ", len(df))
# citis for sales rep employees
q = """
SELECT firstName, lastName, email, city
FROM employees
JOIN offices
ON employees.officeCode = offices.officeCode
WHERE jobTitle = 'Sales Rep';
"""

df = pd.read_sql_query(q, conn)
# print(df)
# print("Number of results:", len(df))


q = """
SELECT productLine, textDescription
FROM productlines
;
"""
df = pd.read_sql(q, conn)
print(df)
print("Number of results:", len(df))
#  let's join the productlines table with the products table, and select the vendor and product description.

q = """
SELECT productLine, textDescription, productVendor, productDescription
FROM productlines
JOIN products
  USING (productLine)
;"""
df = pd.read_sql(q, conn)
print(df)
print("Number of results:", len(df))

# many to many relationship
# OFFICE TABLE
q = """
SELECT *
FROM offices
;"""
df = pd.read_sql(q, conn)
print(df)
print("Number of results:", len(df))


q = """
SELECT *
FROM customers
;
"""

df = pd.read_sql(q, conn)
print('Number of results:', len(df))
# Joined Offices and Customers
q = """
SELECT *
FROM offices
JOIN customers
    USING(state)
;
"""

df = pd.read_sql(q, conn)
print('Number of results:', len(df))
conn.close()
