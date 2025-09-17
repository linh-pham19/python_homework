from datetime import date
import pathlib
import sqlite3

BASEDIR = pathlib.Path(__file__).parent.parent
print(BASEDIR)

#task 1
def task_1(db_path: pathlib.Path | str) -> None:
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        query = """
        SELECT o.order_id, SUM(p.price * li.quantity) AS total_price
        FROM orders o
        JOIN line_items li ON o.order_id = li.order_id
        JOIN products p ON li.product_id = p.product_id
        GROUP BY o.order_id
        ORDER BY o.order_id
        LIMIT 5;
        """

        cursor.execute(query)
        results = cursor.fetchall()

        print("First 5 Orders and Their Total Prices:")
        if results:
            for order_id, total_price in results:
                print(f"Order ID: {order_id}, Total Price: ${total_price:.2f}")
        else:
            print("No orders found.")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        if conn:
            conn.close()

#task 2
def task_2(db_path: pathlib.Path | str) -> None:
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        query = """
        SELECT c.customer_name AS customer_name, AVG(order_totals.total_price) AS average_total_price
        FROM customers c

        LEFT JOIN (
            SELECT o.customer_id AS customer_id_b, SUM(p.price * li.quantity) AS total_price
            FROM orders o
            JOIN line_items li ON o.order_id = li.order_id
            JOIN products p ON li.product_id = p.product_id
            GROUP BY o.order_id
        ) AS order_totals

        ON c.customer_id = order_totals.customer_id_b
        GROUP BY c.customer_id
        ORDER BY c.customer_name;
        """

        cursor.execute(query)
        results = cursor.fetchall()

        print("\n\nCustomer Name and Their Average Order Price:")
        for customer_name, avg_price in results:
            avg_display = f"${avg_price:.2f}" if avg_price is not None else "No Orders"
            print(f"{customer_name}: {avg_display}")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        if conn:
            conn.close()

#task 3
def task_3(db_path: pathlib.Path | str) -> None:
    try:
        conn = sqlite3.connect(db_path)
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()

        conn.execute("BEGIN")

        cursor.execute(
            """SELECT customer_id 
            FROM customers 
            WHERE customer_name = ?""",
            ("Perez and Sons",),
        )
        customer_row = cursor.fetchone()
        if not customer_row:
            raise ValueError("Customer 'Perez and Sons' not found.")
        customer_id = customer_row[0]

        cursor.execute(
            "SELECT employee_id FROM employees WHERE first_name = ? AND last_name = ?",
            (
                "Miranda",
                "Harris",
            ),
        )
        employee_row = cursor.fetchone()
        if not employee_row:
            raise ValueError("Employee 'Miranda Harris' not found.")
        employee_id = employee_row[0]

        cursor.execute("SELECT product_id FROM products ORDER BY price ASC LIMIT 5")
        product_rows = cursor.fetchall()
        product_ids = [row[0] for row in product_rows]

        current_date = date.today().isoformat()


        cursor.execute(
            """
            INSERT INTO orders (customer_id, employee_id, date)
            VALUES (?, ?, ?)
            RETURNING order_id
            """,
            (customer_id, employee_id, current_date),
        )
        order_id = cursor.fetchone()[0]

        for product_id in product_ids:
            cursor.execute(
                """INSERT INTO line_items (order_id, product_id, quantity)
                VALUES (?, ?, ?)""",
                (order_id, product_id, 10),
            )

        conn.commit()

        cursor.execute(
            """SELECT line_items.line_item_id, line_items.quantity, products.product_name
            FROM line_items
            JOIN products ON line_items.product_id = products.product_id
            WHERE line_items.order_id = ?""",
            (order_id,),
        )
        results = cursor.fetchall()

        print(f"\n\nOrder ID {order_id} - Line Items:")
        for line_item_id, quantity, product_name in results:
            print(
                f"Line Item ID: {line_item_id}, Quantity: {quantity}, Product: {product_name}"
            )

    except Exception as e:
        conn.rollback()
        print(f"Task 3: Error: {e}")
    finally:
        if conn:
            conn.close()

#task 4
def task_4(db_path: pathlib.Path | str) -> None:
    try:
        conn = sqlite3.connect(db_path)
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()

        query = """
        SELECT employees.first_name, employees.last_name, COUNT(orders.order_id) AS order_count
        FROM employees
        JOIN orders ON employees.employee_id = orders.employee_id
        GROUP BY employees.employee_id
        HAVING COUNT(orders.order_id) > 5
        ORDER BY order_count DESC;
        """

        cursor.execute(query)
        results = cursor.fetchall()

        print("\n\nEmployees with more than 5 orders:")
        for first_name, last_name, count in results:
            print(f"{first_name} {last_name}: {count} orders")

    except sqlite3.Error as e:
        print(f"Task 4 : Database error: {e}")
    except Exception as e:
        print(f"Task 4 : Unexpected error: {e}")
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    task_1(BASEDIR / "db/lesson.db")
    task_2(BASEDIR / "db/lesson.db")
    task_3(BASEDIR / "db/lesson.db")
    task_4(BASEDIR / "db/lesson.db")