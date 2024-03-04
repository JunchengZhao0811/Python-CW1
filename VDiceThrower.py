import random

def get_n_faces():
    while True:
        try:
            n_faces = int(input("Enter the number of dice faces: "))
            if n_faces > 0:
                return n_faces
            else:
                print("The number of faces must be greater than 0.")
        except ValueError:
            print("Please enter a valid integer.")

def get_n_throws(n_faces):
    while True:
        try:
            n_throws = int(input("Enter the number of throws: "))
            if n_throws % n_faces == 0:
                return n_throws
            else:
                print(f"The number of throws must be a multiple of {n_faces}.")
        except ValueError:
            print("Please enter a valid integer.")

def throw_dice(n_faces, n_throws):
    results = {i: 0 for i in range(1, n_faces + 1)}  # Initialize results with all faces set to 0 occurrences.
    for _ in range(n_throws):
        throw = random.randint(1, n_faces)  # Simulate a dice throw.
        results[throw] += 1  # Increment the count for the thrown face.
    return results

def main():
    n_faces = get_n_faces()  # Get the number of faces from the user.
    n_throws = get_n_throws(n_faces)  # Get the number of throws from the user.
    results = throw_dice(n_faces, n_throws)  # Perform the dice throws and gather results.

    # Display the results sorted by dice face.
    for face, count in sorted(results.items()):
        print(f"Side {face}: {count} times")

if __name__ == "__main__":
    main()  # Execute the main function.
