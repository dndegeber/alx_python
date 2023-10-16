import MySQLdb
import sys

def filter_states_by_name(username, password, database, state_name):
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

    # Use format to create the SQL query with the user input
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id".format(state_name)

    # Execute the query
    cur.execute(query)

    # Fetch all the rows
    rows = cur.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the cursor and connection
    cur.close()
    db.close()

if __name__ == "__main__":
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 5:
        print("Usage: ./2-my_filter_states.py <username> <password> <database> <state_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Call the function with provided arguments
    filter_states_by_name(username, password, database, state_name)

