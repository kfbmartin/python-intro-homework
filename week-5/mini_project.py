numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

while True:
    #Print Number Cruncher Menu
    print("")
    print("=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")
    print("")

    option = int(input("Choose an option (1-5):"))

    #Find Minimum
    if option == 1:
        min_number = numbers[0]
        for number in numbers:
            if number < min_number:
                min_number = number

        print(f"The minimum number is {min_number}.")

    #Find Maximum
    elif option == 2:

        max_number = numbers[0]
        for number in numbers:
            if number > max_number:
                max_number = number

        print(f"The maximum number is {max_number}.")

    #Search for a number
    elif option == 3:

        target = int(input("Enter a number: "))

        def linear_search(data, target):
            for i in range(len(data)):
                if data[i] == target:
                    return i
            return -1

        result = linear_search(numbers, target)
        if result != -1:
            print(f"Found at index {result}") 
        elif result == -1:
                print(f"{target} not found")

    #Sort the List
    elif option == 4:

        swapped = True

        while swapped: 
            swapped = False

            n = len(numbers)

            for index in range(n-1):
                    if numbers[index] > numbers[index + 1]:
                        numbers[index], numbers[index + 1 ] = (numbers[index+ 1], numbers[index])

                        swapped = True 

        print(f"Sorted list: {numbers}")        

    #Quit Loop

    elif option == 5:
        print("Quitting Number Cruncher")
        break