import MySQLdb
import sys

def filter_cities_by_state(username, password, database, state_name):
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
    )

    # Create a cursor object
    cur = db.cursor()

    # Use a parameterized query to prevent SQL injection
    query = """
    SELECT GROUP_CONCAT(name SEPARATOR ', ')
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id
    """
    
    # Execute the query with the user input as a parameter
    cur.execute(query, (state_name,))

    # Fetch the result
    result = cur.fetchone()[0]

    if result:
        print(result)
    else:
        print("No cities found for the given state.")

    # Close the cursor and connection
    cur.close()
    db.close()

if __name__ == "__main__":
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 5:
        print("Usage: ./5-filter_cities.py <username> <password> <database> <state_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Call the function with provided arguments
    filter_cities_by_state(username, password, database, state_name)

