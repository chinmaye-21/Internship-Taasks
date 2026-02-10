# Decorator
def admin_only(func):
    def wrapper(username):
        if username == "admin":
            return func(username)
        else:
            print("Access Denied")
    return wrapper


# Apply decorator
@admin_only
def dashboard(username):
    print("Welcome to Admin Dashboard!")


# Test
dashboard("admin")      # Works
dashboard("aishwarya")  # Blocked