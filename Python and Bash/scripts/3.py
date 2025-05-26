def writeToFile():
    with open("test.txt", "w") as f:
        f.write(input("Enter text to write to file: "))

if __name__ == "__main__":
    try:
        writeToFile()
        print("Text written to file successfully.")
    except Exception as e:
        print("An error occurred: " + str(e))