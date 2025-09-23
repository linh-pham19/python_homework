import sqlite3
import pandas as pd

def task_5():
    with sqlite3.connect("../db/lesson.db") as conn:
        sql_statement = """
        SELECT li.line_item_id, li.quantity, p.product_id, p.product_name, p.price
        FROM line_items li
        JOIN products p ON li.product_id = p.product_id;"""
        df = pd.read_sql_query(sql_statement, conn)

        print(df.head(5))

        df["total"] = df["quantity"] * df["price"]
        print("\nTotal:\n")
        print(df.head(5))

        df_group = df.groupby("product_id").agg(
            {"line_item_id": "count", "total": "sum", "product_name": "first"}
        )
        print("\nGroup By:\n")
        print(df_group.head(5))

        df = df.sort_values(by="product_name", axis="rows", ascending=False)
        print("\nSorted:\n")
        print(df.head(5))

        df.to_csv("order_summary.csv", header=True)


if __name__ == "__main__":
    task_5()