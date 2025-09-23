import sqlite3
import os

def create_database():
    """Create and connect to the SQLite database"""
    try:
        # Create db directory if it doesn't exist
        os.makedirs('../db', exist_ok=True)
        
        # Connect to database (creates it if it doesn't exist)
        conn = sqlite3.connect('../db/magazines.db')
        print("Successfully connected to magazines.db")
        return conn
    except Exception as e:
        print(f"Error creating/connecting to database: {e}")
        return None

def create_tables(conn):
    """Create all necessary tables with proper constraints and foreign keys"""
    try:
        # Enable foreign key constraints
        conn.execute("PRAGMA foreign_keys = 1")
        
        # Create publishers table
        conn.execute('''
            CREATE TABLE IF NOT EXISTS publishers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            )
        ''')
        
        # Create magazines table (has foreign key to publishers)
        conn.execute('''
            CREATE TABLE IF NOT EXISTS magazines (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                publisher_id INTEGER NOT NULL,
                FOREIGN KEY (publisher_id) REFERENCES publishers(id)
            )
        ''')
        
        # Create subscribers table
        conn.execute('''
            CREATE TABLE IF NOT EXISTS subscribers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                address TEXT NOT NULL
            )
        ''')
        
        # Create subscriptions table (join table with foreign keys to both magazines and subscribers)
        conn.execute('''
            CREATE TABLE IF NOT EXISTS subscriptions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                subscriber_id INTEGER NOT NULL,
                magazine_id INTEGER NOT NULL,
                expiration_date TEXT NOT NULL,
                FOREIGN KEY (subscriber_id) REFERENCES subscribers(id),
                FOREIGN KEY (magazine_id) REFERENCES magazines(id),
                UNIQUE(subscriber_id, magazine_id)
            )
        ''')
        
        print("All tables created successfully")
        
    except Exception as e:
        print(f"Error creating tables: {e}")

def add_publisher(conn, name):
    """Add a publisher, avoiding duplicates"""
    try:
        # Check if publisher already exists
        cursor = conn.execute("SELECT id FROM publishers WHERE name = ?", (name,))
        if cursor.fetchone():
            print(f"Publisher '{name}' already exists")
            return
        
        # Insert new publisher
        conn.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
        print(f"Added publisher: {name}")
        
    except Exception as e:
        print(f"Error adding publisher '{name}': {e}")

def add_magazine(conn, name, publisher_name):
    """Add a magazine, avoiding duplicates"""
    try:
        # Check if magazine already exists
        cursor = conn.execute("SELECT id FROM magazines WHERE name = ?", (name,))
        if cursor.fetchone():
            print(f"Magazine '{name}' already exists")
            return
        
        # Get publisher ID
        cursor = conn.execute("SELECT id FROM publishers WHERE name = ?", (publisher_name,))
        publisher_row = cursor.fetchone()
        if not publisher_row:
            print(f"Publisher '{publisher_name}' not found")
            return
        
        publisher_id = publisher_row[0]
        
        # Insert new magazine
        conn.execute("INSERT INTO magazines (name, publisher_id) VALUES (?, ?)", 
                    (name, publisher_id))
        print(f"Added magazine: {name} (Publisher: {publisher_name})")
        
    except Exception as e:
        print(f"Error adding magazine '{name}': {e}")

def add_subscriber(conn, name, address):
    """Add a subscriber, avoiding duplicates based on both name and address"""
    try:
        # Check if subscriber with same name AND address already exists
        cursor = conn.execute("SELECT id FROM subscribers WHERE name = ? AND address = ?", 
                            (name, address))
        if cursor.fetchone():
            print(f"Subscriber '{name}' at '{address}' already exists")
            return
        
        # Insert new subscriber
        conn.execute("INSERT INTO subscribers (name, address) VALUES (?, ?)", 
                    (name, address))
        print(f"Added subscriber: {name} at {address}")
        
    except Exception as e:
        print(f"Error adding subscriber '{name}': {e}")

def add_subscription(conn, subscriber_name, subscriber_address, magazine_name, expiration_date):
    """Add a subscription, avoiding duplicates"""
    try:
        # Get subscriber ID
        cursor = conn.execute("SELECT id FROM subscribers WHERE name = ? AND address = ?", 
                            (subscriber_name, subscriber_address))
        subscriber_row = cursor.fetchone()
        if not subscriber_row:
            print(f"Subscriber '{subscriber_name}' at '{subscriber_address}' not found")
            return
        subscriber_id = subscriber_row[0]
        
        # Get magazine ID
        cursor = conn.execute("SELECT id FROM magazines WHERE name = ?", (magazine_name,))
        magazine_row = cursor.fetchone()
        if not magazine_row:
            print(f"Magazine '{magazine_name}' not found")
            return
        magazine_id = magazine_row[0]
        
        # Check if subscription already exists
        cursor = conn.execute("SELECT id FROM subscriptions WHERE subscriber_id = ? AND magazine_id = ?", 
                            (subscriber_id, magazine_id))
        if cursor.fetchone():
            print(f"Subscription already exists for '{subscriber_name}' to '{magazine_name}'")
            return
        
        # Insert new subscription
        conn.execute("INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)", 
                    (subscriber_id, magazine_id, expiration_date))
        print(f"Added subscription: {subscriber_name} -> {magazine_name} (expires: {expiration_date})")
        
    except Exception as e:
        print(f"Error adding subscription: {e}")

def populate_data(conn):
    """Populate all tables with sample data"""
    try:
        print("\n--- Populating Publishers ---")
        add_publisher(conn, "National Geographic Society")
        add_publisher(conn, "Time Inc.")
        add_publisher(conn, "Condé Nast")
        
        print("\n--- Populating Magazines ---")
        add_magazine(conn, "National Geographic", "National Geographic Society")
        add_magazine(conn, "National Geographic Kids", "National Geographic Society")
        add_magazine(conn, "Time Magazine", "Time Inc.")
        add_magazine(conn, "Sports Illustrated", "Time Inc.")
        add_magazine(conn, "Vogue", "Condé Nast")
        add_magazine(conn, "Wired", "Condé Nast")
        
        print("\n--- Populating Subscribers ---")
        add_subscriber(conn, "John Smith", "123 Main St, New York, NY")
        add_subscriber(conn, "Jane Doe", "456 Oak Ave, Los Angeles, CA")
        add_subscriber(conn, "Bob Johnson", "789 Pine Rd, Chicago, IL")
        add_subscriber(conn, "Alice Brown", "321 Elm St, Houston, TX")
        
        print("\n--- Populating Subscriptions ---")
        add_subscription(conn, "John Smith", "123 Main St, New York, NY", "National Geographic", "2024-12-31")
        add_subscription(conn, "John Smith", "123 Main St, New York, NY", "Time Magazine", "2024-11-30")
        add_subscription(conn, "Jane Doe", "456 Oak Ave, Los Angeles, CA", "Vogue", "2025-01-31")
        add_subscription(conn, "Jane Doe", "456 Oak Ave, Los Angeles, CA", "Wired", "2024-10-31")
        add_subscription(conn, "Bob Johnson", "789 Pine Rd, Chicago, IL", "Sports Illustrated", "2025-03-31")
        add_subscription(conn, "Alice Brown", "321 Elm St, Houston, TX", "National Geographic Kids", "2024-09-30")
        
        # Commit all changes
        conn.commit()
        print("\nAll data committed successfully!")
        
    except Exception as e:
        print(f"Error populating data: {e}")
        conn.rollback()

def run_queries(conn):
    """Execute and display results of various SQL queries"""
    print("\n" + "="*60)
    print("RUNNING QUERIES")
    print("="*60)
    
    try:
        # Query 1: Retrieve all information from subscribers table
        print("\n1. All Subscribers:")
        print("-" * 40)
        cursor = conn.execute("SELECT * FROM subscribers")
        rows = cursor.fetchall()
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Address: {row[2]}")
        
        # Query 2: Retrieve all magazines sorted by name
        print("\n2. All Magazines (sorted by name):")
        print("-" * 40)
        cursor = conn.execute("SELECT * FROM magazines ORDER BY name")
        rows = cursor.fetchall()
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Publisher ID: {row[2]}")
        
        # Query 3: Find magazines for a particular publisher (using JOIN)
        print("\n3. Magazines published by 'Time Inc.':")
        print("-" * 40)
        cursor = conn.execute("""
            SELECT m.id, m.name, p.name as publisher_name
            FROM magazines m
            JOIN publishers p ON m.publisher_id = p.id
            WHERE p.name = ?
        """, ("Time Inc.",))
        rows = cursor.fetchall()
        for row in rows:
            print(f"Magazine ID: {row[0]}, Name: {row[1]}, Publisher: {row[2]}")
        
        print("\n4. Bonus - All Subscriptions with Details:")
        print("-" * 40)
        cursor = conn.execute("""
            SELECT 
                sub.name as subscriber_name,
                sub.address,
                m.name as magazine_name,
                p.name as publisher_name,
                s.expiration_date
            FROM subscriptions s
            JOIN subscribers sub ON s.subscriber_id = sub.id
            JOIN magazines m ON s.magazine_id = m.id
            JOIN publishers p ON m.publisher_id = p.id
            ORDER BY sub.name, m.name
        """)
        rows = cursor.fetchall()
        for row in rows:
            print(f"{row[0]} ({row[1]}) subscribes to {row[2]} by {row[3]}, expires: {row[4]}")
        
    except Exception as e:
        print(f"Error running queries: {e}")

def main():
    """Main function to orchestrate the database operations"""
    print("Starting SQLite Database Assignment")
    print("="*50)
    
    # Task 1: Create database connection
    conn = create_database()
    if not conn:
        return
    
    try:
        # Task 2: Create tables
        create_tables(conn)
        
        # Task 3: Populate tables with data
        populate_data(conn)
        
        # Task 4: Run queries
        run_queries(conn)

        conn.commit()
        print("Database populated.")
        
    finally:
        conn.close()
        print("\nDatabase connection closed.")

if __name__ == "__main__":
    main()