from ..database.database import session

# Test the session
try:
    # Execute a simple query
    result = session.execute("SELECT 1")
    print("Database connection successful.")
except Exception as e:
    print("Database connection failed:", e)
finally:
    # Close the session
    session.close()