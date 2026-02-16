"""Files and I/O in Python"""

import time
import pickle
import json


# ! ------------------------------------------------------------------------------------------------

# ! FILES and I/O

# ! ------------------------------------------------------------------------------------------------

# ? File I/O operations:
# File Input/Output operations are how a Python program reads data from a file and writes data to
# a file stored in disk.

# Without this File I/O, program data will be lost when the program ends/after execution.
# No logs, no reports, no data storage, no persistence of data across program runs.

# ? ------------------------------------------------------------------------------------------------

# ? Every file operation follows these steps:

# ? 1. Open a file
file = open("data/sample.txt", "w")  # Open file in write mode
# If file does not exist, it will be created

file2 = open("data/sample2.txt", "a")  # Open file in append mode
# If file does not exist, it will be created


# file = open("sample.txt", "r")  # Open file in read mode
# file = open("sample.txt", "x")  # Open file in exclusive creation mode

# file = open("sample.txt", "r+")  # Open file in read and write mode
# File must exist, else raises FileNotFoundError

# file = open("sample.txt", "w+")  # Open file in write and read mode (not recommended)
# file = open("sample.txt", "a+")  # Open file in append and read mode (not recommended)

# file = open("sample.txt", "t")  # Text mode (default)
# file = open("sample.bin", "b")  # Binary mode
# file = open("sample.bin", "rb")  # Binary read mode
# file = open("sample.bin", "wb")  # Binary write mode

# ? ------------------------------------------------------------------------------------------------

# ? 2. Perform file operations (read/write)
file.write("Hello, World!\n")  # Write to file
# print(file.read())  # Read from file (not readable if opened in write mode)

file2.write("Hello, again!\n")  # Write to file2

# ? ------------------------------------------------------------------------------------------------

# ? 3. Close the file
file.close()  # Close the file to save changes
file2.close()  # Close the file2 to save changes
# Always close the file after operations to free up resources

# The file object contains information about the file like its name, mode, and encoding.
print(file)  # ? <_io.TextIOWrapper name='sample.txt' mode='w' encoding='cp1252'>
print(file2)  # ? <_io.TextIOWrapper name='sample2.txt' mode='a' encoding='cp1252'>
# <_io.TextIOWrapper> indicates it's a text file object (a class that wraps a file descriptor)

# Printing the file object shows its metadata (name, mode, encoding), even if the file is closed.
# The file object still exists in memory, but it is not usable for reading/writing once closed.

# ? ------------------------------------------------------------------------------------------------

# ? Creating a file using open() with "x" mode and handling exceptions:

# file3 = open("data/sample4.txt", "x")  # Create a new file
# try:

#     if file3:
#         # File created successfully. (first time)
#         print("File created successfully.")
#     else:
#         # Throws FileExistsError if file exists
#         raise FileExistsError("File already exists.")

# except Exception as y:
#     print(y)
# else:
#     print("New file created.")

# ! ------------------------------------------------------------------------------------------------

# ! BINARY FILES AND COPYING FILES

# ! ------------------------------------------------------------------------------------------------

# ? Binary files are files that contain data in a format that is not human-readable, such as images,
# ? audio files, or executable files. They are read and written in binary mode using "rb" and "wb"
# ? modes in the open() function.

# ? Example 1: Using rb and wb binary modeS to write and read binary data

# Writing bytes to a file
with open("binary/sample7.bin", "wb") as g:
    g.write(b"Hello in binary!\n")

# Reading bytes back
with open("binary/sample7.bin", "rb") as k:
    print(k.read())  # ? Output: b'Hello in binary!\n'

# ? ------------------------------------------------------------------------------------------------

# ? Example 2: Copying a binary file (a PNG image)
# Copies sample.png -> output.png (sample.png must exist in the same folder as this .py file)
with open("assets/sample.png", "rb") as src, open("assets/output.png", "wb") as dst:
    dst.write(src.read())

print("Copied sample.png -> output.png")
# ? Output: Copied sample.png -> output.png
# ? (and the file output.png will be created as a copy of sample.png)


# ! ------------------------------------------------------------------------------------------------

# ! SEEK() & TELL() METHODS

# ! ------------------------------------------------------------------------------------------------

# ? seek() sets the file pointer to a specific position
# ? tell() returns the current position of the file pointer

# ? A file is like a book, the file pointer is like a bookmark that keeps track of where you are.
# seek() --> move the bookmark to a specific page (position in the file)
# tell() --> tells you the current page number (position of the file pointer)

# ? tell() --> used to read the current cursor position
f = open("data/sample3.txt", "r")
print(f.tell())
# ? Output: 0 (initial position at the beginning of the file)

f.read(10)  # Move pointer forward 10 characters
print(f.tell())  # Now the pointer is at position 10
# ? Output: 10

# Now read the rest of the file from position 10 onward
print(f.read())
# ? Output:
# ? rem Ipsum?
# ? Lorem Ipsum is simply dummy text of the printing and typesetting industry.
f.close()


# ? seek() --> move the cursor to specific position
f = open("data/sample3.txt", "r")
f.seek(2)  # Move pointer to position 2 (3rd character in file)
print(f.read())  # Now read from that position to the end
# ? Output:
# ? at is Lorem Ipsum?
# ? Lorem Ipsum is simply dummy text of the printing and typesetting industry.

f.close()

# ? ------------------------------------------------------------------------------------------------

# ? seek() method syntax:
# file.seek(offset, whence)  - Moves the file pointer to a specific position
# offset is the number of bytes/characters to move
# whence is reference point for offset (0: beginning of file, 1: current position, 2: end of file)

# ? When to use the seek method?
# 1. To read specific parts of a file without reading the entire file
# 2. To update specific parts of a file without overwriting the entire file
# 3. To read the logs or data from a specific point in a file, especially in large files
# 4. Chat application to read recent messages without loading the entire chat history

# ? ------------------------------------------------------------------------------------------------

# ? Example of using seek() to read specific parts of a file:
# Open file in binary mode to use byte offsets
f1 = open("data/seekfile.txt", "rb")
f1.seek(0)  # Move file pointer back to the beginning of the file
print(f1.read(5))  # Read first 5 characters
# ? Output: b'ABCDE'

f1.seek(3, 0)  # Move file pointer to the 3rd character from the beginning
print(f1.read(5))  # Read next 5 characters from the 3rd character
# ? Output: b'DEFGH'

f1.seek(2, 1)  # Move file pointer 2 characters forward from current position
print(f1.read(5))  # Read next 5 characters from the current position
# ? Output: b'KLMNO'
f1.seek(-5, 2)  # Move file pointer 5 characters backward from the end of the file
print(f1.read(5))  # Read last 5 characters of the file
# ? Output: b'VWXYZ'

f1.close()

# ? The code above will not work if you open the file in read mode (text mode) because seek() uses
# ? character offsets, which can lead to unexpected behavior with multi-byte characters.

# ? ------------------------------------------------------------------------------------------------

# ? Another example of using seek() like a chat application to read new messages added in real time:

# Open file in read mode using context manager (automatically closes file after block)
with open("data/seekfile2.txt", "r") as g:
    g.seek(0, 2)  # Move file pointer to the end of the file (0 bytes from end)

    start = time.time()  # Start time for demonstration
    while time.time() - start < 20:  # Run for 20 seconds to demonstrate real-time reading
        # Read a line from the file (returns empty string if end of file is reached)
        message = g.readline()

        if not message:  # If message is empty, it means we have reached the end of the file
            # Wait for new data instead of spinning the CPU with a tight loop
            time.sleep(0.2)
            continue  # Continue to wait for new messages to be added to the file
        # Print the new message (this will print any new lines added to the file in real time)
        print("New message: " + message, end="")
        # end="" to avoid adding extra newline since message already has one


# ? Output:
# File has new line added "This message has just been saved to this file in real time."
# ? New message: This message has just been saved to this file in real time.


# ? ------------------------------------------------------------------------------------------------

# ? tell() real time example:
count = 0
in_paragraph = False

with open("data/tellfile.txt", "r") as f:
    while True:
        line = f.readline()  # Read a line from the file
        if not line:  # If line is empty, it means we have reached the end of the file
            break  # Exit the loop

        # Print the current position in the file after reading the line
        print(f.tell())

        if line.strip():  # If the line is not empty (after stripping whitespace)
            in_paragraph = True  # We are in a paragraph
        else:
            if in_paragraph:  # If we were in a paragraph and now we have an empty line, it means the paragraph has ended
                count += 1  # Increment paragraph count
                in_paragraph = False  # Reset for next paragraph

    if in_paragraph:  # If we ended the file while still in a paragraph, count that paragraph as well
        count += 1
    print("Number of paragraphs:", count)

# ? Output:
# ? 22 (22 bytes after reading first line)
# ? 598 (598 bytes after reading second line)
# ? 600 (600 bytes after reading third line - a blank line)
# ? 619 (619 bytes after reading fourth line)
# ? 1234 (1234 bytes after reading fifth line)
# ? Number of paragraphs: 2 (since there are 2 blank lines separating the paragraphs)

# ! ------------------------------------------------------------------------------------------------

# ! CONTEXT MANAGERS AND SAFE FILE HANDLING

# ! ------------------------------------------------------------------------------------------------

# ? Context managers (with statement) are used for safe file handling, ensuring that files are
# ? properly closed after their block of code is executed, even if an error occurs. This prevents
# ? resource leaks and ensures that file handles are not left open unintentionally.

# ? Example 1: Why context managers help

# If an exception happens before f.close(), the file may stay open
f = open("data/lorem_ipsum.txt", "r")
text = f.read()
print(text)
# print(10 / 0)  # If this runs, f.close() below will never execute
f.close()

# Using a context manager ensures the file is closed even if an error happens
with open("data/lorem_ipsum.txt", "r") as r:
    text = r.read()
    print(text)

# ? Example 2: read(), readline(), readlines()

with open("data/lorem_ipsum.txt", "r") as r:  # Open file in read mode using context manager
    print("readline():", r.readline())      # reads 1 line
    print("read(20):", r.read(20))          # reads next 20 characters
    # reads remaining lines (show first 2)
    print("readlines():", r.readlines()[:2])

# ? Output:
# ? readline(): What is Lorem Ipsum?
# ? read(20): Lorem Ipsum is simpl
# ? readlines(): ['y dummy text of the printing and typesetting industry.\n', 'Lorem Ipsum etc...


# ! ------------------------------------------------------------------------------------------------

# ! PICKLING AND UNPICKLING

# ! ------------------------------------------------------------------------------------------------

# ? Pickling is the process of converting a Python object into a byte stream (binary), which can
# ? be saved to a file or transmitted over a network.
# ? Unpickling is the process of converting a byte stream back into a Python object.

# import pickle - top of the file

# ? Example 1: Writing plain text to a file without pickling:
# a = 8
# b = 6

# f = open("sample5.txt", "w")
# f.write(str(a + b))
# f.close()
# This does not use context manager, so will not automatically close the file after writing

# Better way using context manager:
a = 8
b = 6
with open("data/sample5.txt", "w") as f:  # Open file in write mode using context manager
    f.write(str(a + b))  # Write the sum of a and b to the file as a string
# File is automatically closed after this block, even if an error occurs

# ? ------------------------------------------------------------------------------------------------

# ? Example 2: Pickling a dictionary to a file and unpickling it back to a dictionary object:
dict1 = {1: 100, 2: 200, 3: 300}
with open("data/sample6.txt", "w") as f:
    # This stores the string representation of the dictionary, so not pickled
    f.write(str(dict1))

with open("binary/sample.pkl", "wb") as f:
    pickle.dump(dict1, f)  # Pickling the dictionary to a file

with open("binary/sample.pkl", "rb") as g:
    ans = pickle.load(g)  # Unpickling the dictionary from the file
    print(ans)
    print(type(ans))

# ? Output:
# ? {1: 100, 2: 200, 3: 300}
# (the dictionary is successfully unpickled)
# ? <class 'dict'>

# Pickling is used to save the state of an object or data structure, allowing it to be stored and
# retrieved later. It is commonly used for saving machine learning models, caching data, and
# transferring data between different Python programs.

# Pickling is not secure against erroneous or maliciously constructed data. Never unpickle data
# received from an untrusted source, as it may lead to code execution vulnerabilities.

# ! ------------------------------------------------------------------------------------------------

# ! JSON (JavaScript Object Notation)

# ! ------------------------------------------------------------------------------------------------

# ? JSON is a lightweight data interchange format that is easy for humans to read and write, and
# ? easy for machines to parse and generate. It is commonly used for data exchange between a server
# ? and a web application, as well as for storing data in files.

# import JSON (top of the file)

# ? Example 1: Converting a Python list to a JSON string and back to a Python list:

l1 = [1, 2, 3, 4, 5]

ans = json.dumps(l1)  # Convert Python list to JSON string
print(ans)  # ? Output: '[1, 2, 3, 4, 5]'
print(type(ans))  # ? Output: <class 'str'>

decode = json.loads(ans)  # Convert JSON string back to list
print(decode)  # ? Output: [1, 2, 3, 4, 5]
print(type(decode))  # ? Output: <class 'list'>

# ? ------------------------------------------------------------------------------------------------

# ? Example 2: Difference between using str() and json.dumps() to convert a list to a string:

l2 = [1, 2, 3, 4, 5, 6]
print(str(l1))  # ? Output: '[1, 2, 3, 4, 5]'
print(type(str(l1)))  # ? Output: <class 'str'>
# Output is just a Python string representation of the list
# It looks like JSON, but it is not guaranteed to follow string JSON rules
# e.g. dictionaries will use single quotes instead of double quotes, which is not valid JSON

ans2 = json.dumps(l2)  # Convert list to JSON string
print(ans2)  # ? Output: '[1, 2, 3, 4, 5, 6]'
print(type(ans2))  # ? Output: <class 'str'>
# This is a valid JSON-formatted string that can safely be parsed back to a Python list
# using json.loads().

# ? ------------------------------------------------------------------------------------------------

# ? Example 3: Returning a JSON response from a Django view using JsonResponse:

# import requests - this is a library to make HTTP requests in Python
# from django.http import JsonResponse

# This code only works inside a Django project:

# def my_view(request):
#     data = {
#         'name': 'Alice',
#         'age': 30,
#         'city': 'New York'
#     }
#     return JsonResponse(data)  # This will return a JSON response with the data dictionary


# url = "https://jsonplaceholder.typicode.com/posts/1"
# response = requests.get(url)  # Make a GET request to the URL
# print(response)  # ? Output: <Response [200]> (indicates successful response)
# print(response.json())
# ? Output: JSON data from the response (parsed as a Python dictionary)

# ? ------------------------------------------------------------------------------------------------

# ? Example 4: Saving a Python dictionary to a JSON file

data = {
    "name": "Anton",
    "age": 31,
    "courses": ["Python", "SQL", "HTML"]
}

# ? Writing (Serialising) Python object to JSON file
with open("data/data.json", "w") as f:
    json.dump(data, f, indent=4)
    # json.dump() writes Python object directly to file as JSON
    # indent=4 makes the file readable (pretty formatting)

print("Data written to data.json")
# ? Output: Data written to data.json
# (and the file data.json will contain the JSON representation of the data dictionary)


# ?Reading (Deserialising) JSON file back into Python object
with open("data/data.json", "r") as f:
    loaded_data = json.load(f)
    # json.load() reads JSON from file and converts it back to Python object

print("Data read from data.json:")
print(loaded_data)
print(type(loaded_data))
# ? Output:
# ? Data read from data.json:
# ? {'name': 'Anton', 'age': 31, 'courses': ['Python', 'SQL', 'HTML']}
# ? <class 'dict'>
# (the JSON data is successfully loaded back into a Python dictionary
