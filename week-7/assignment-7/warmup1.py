#context manager with
with open('../data/notes.txt', 'r') as file:
    countline = 0
    for line in file:
        countline = countline +1
        print(f"Line {countline}: {line.strip()}")  # .strip() removes the newline character at the end    