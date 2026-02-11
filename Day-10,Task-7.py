class Session:
    def __del__(self):
        print("Session Ended")


# Creating an object
s = Session()

# Deleting the object manually
del s
