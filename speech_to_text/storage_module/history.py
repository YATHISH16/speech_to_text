def show_history(filename):

    try:
        with open(filename, "r") as file:

            print("\n===== TRANSCRIPT HISTORY =====\n")

            print(file.read())

    except FileNotFoundError:

        print("No transcript history found.")