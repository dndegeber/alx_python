import sys

# Get the list of arguments
arguments = sys.argv[1:]

# Get the number of arguments
num_arguments = len(arguments)

# Print the number of arguments and a colon or period
if num_arguments == 0:
    print("Number of argument(s): .")
else:
    print(f"Number of argument(s): {num_arguments}:")

    # Print each argument with its position
    for i, arg in enumerate(arguments, 1):
        print(f"{i}: {arg}")

