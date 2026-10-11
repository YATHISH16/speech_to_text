def write_to_file(text, filename):

    with open(filename, "a") as file:
        file.write(text + "\n")