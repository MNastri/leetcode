import os
import sqlite3

# Write your MySQL query statement below
SQL_STATEMENT = """
SELECT product_id FROM Products
WHERE low_fats = 'Y'
AND recyclable = 'Y'
"""
DATABASE = os.path.join(os.getcwd(), "database.db")


def create_table():
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE Products ("
        "  product_id  INTEGER                                 PRIMARY KEY"
        ", low_fats    TEXT CHECK ( low_fats IN ('Y', 'N') )"
        ", recyclable  TEXT CHECK ( recyclable IN ('Y', 'N') )"
        ")"
    )
    cur.execute("INSERT INTO Products VALUES (0, 'Y', 'N')")
    cur.execute("INSERT INTO Products VALUES (1, 'Y', 'Y')")
    cur.execute("INSERT INTO Products VALUES (2, 'N', 'Y')")
    cur.execute("INSERT INTO Products VALUES (3, 'Y', 'Y')")
    cur.execute("INSERT INTO Products VALUES (4, 'N', 'N')")
    con.commit()
    con.close()


# if __name__ == "__main__":
#     create_table()


def main():
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    for row in cur.execute(SQL_STATEMENT):
        print(row)
    con.close()


if __name__ == "__main__":
    main()
