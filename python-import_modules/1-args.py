import sys

def main():
    # Get the arguments from sys.argv
    arguments = sys.argv[1:]

    # Calculate the number of arguments
    num_arguments = len(arguments)

    # Print the number of arguments
    if num_arguments == 0:
        print("0 arguments.")
    elif num_arguments == 1:
        print("1 argument:")
    else:
        print(f"{num_arguments} arguments:")

    # Print the list of arguments
    for i, arg in enumerate(arguments, 1):
        print(f"{i}: {arg}")

if __name__ == "__main__":
    main()


