def write_to_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)
    print(f"Content written to {filename}.")

filename = input("Enter the filename: ")
content = input("Enter the content to write: ")
write_to_file(filename, content)
