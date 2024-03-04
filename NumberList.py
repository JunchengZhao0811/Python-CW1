import random

class NumberList:
    def __init__(self):
        # Initialize an empty list to store the data
        self.__data = []

    @staticmethod
    def __getNDataFromKeyboard():
        # Static method to get the number of data elements from the user
        print("Enter the number of data set elements (integer and >= 2): ")
        while True:
            try:
                ndata = int(input())  # Attempt to convert user input to integer
                if ndata >= 2:
                    return ndata
                else:
                    print("Please enter an integer >= 2.")
            except ValueError:
                print("Invalid input. Please enter an integer.")

    def getDataFromKeyboard(self):
      ndata = self.__getNDataFromKeyboard()
      print("Enter the data elements (numeric values only, use '.' as decimal separator):")
      for i in range(ndata):
          while True:
              user_input = input(f"Enter element {i+1} of {ndata}: ").strip()  # Strip whitespace
              user_input = user_input.replace(',', '.')  # Replace comma with dot for decimal
              try:
                  num = float(user_input)  # Attempt to convert user input to float
                  self.__data.append(num)  # Append the number to the data list
                  break  # Exit the loop after successful conversion
              except ValueError:
                  print("Invalid input. Please enter a numeric value using '.' as decimal separator.")

    def getRandomData(self, ndata, range1, range2=None):
        # Public method to generate random data within a specified range
        ndata = int(ndata)
        range1, range2 = float(range1), float(range2) if range2 is not None else float(range1)
        if range2 <= range1:
            print("Error: range2 must be greater than range1.")
            return
        self.__data.extend(random.uniform(range1, range2) for _ in range(ndata))  # Append random numbers to the data list

    def getDataFromFile(self, fileName):
        # Public method to read data from a file
        try:
            with open(fileName, 'r') as file:
                for line in file:
                    try:
                        num = float(line.strip())
                        self.__data.append(num)
                    except ValueError:
                        print(f"Error: Cannot convert line to float: {line.strip()}")
        except FileNotFoundError:
            print(f"Error: No such file: {fileName}")

    def getData(self):
        # Public method to access the data stored in the list
        return self.__data
