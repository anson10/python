def announce(f):
    def wrapper():
        print("About to run the functiomn ")
        f()
        print("Done with the function")
    return wrapper

@announce
def hello():
    print("Hello, World!")

hello()
