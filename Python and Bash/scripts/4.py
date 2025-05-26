def readFromFile(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File not found."
    except IOError:
        return "Error reading file."

if __name__ == "__main__":
    try:
        filepath = input("Enter the file path to read from: ")
        content = readFromFile(filepath)
        print("Content read from file: " + content)
    except Exception as e:
        print("An error occurred: " + str(e))
