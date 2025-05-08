def read_from_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print("File not found.")

filename = input("Enter the filename to read: ")
read_from_file(filename)
