numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

def show_menu():
    #Print Number Cruncher Menu
    print("")
    print("=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")
    print("")

    option = input("Choose an option (1-5):")
    return option

#Find Minimum Function
def find_min(numbers):

    min_number = numbers[0]
    for number in numbers:
        if number < min_number:
            min_number = number

    return min_number

#Find Maximum
def find_max(numbers):

    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number

    return max_number

#Search for a number
def search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1



#Sort the List
def bubble_sort(numbers):
    sorted_numbers = numbers.copy()
    swapped = True

    while swapped: 
        swapped = False

        n = len(sorted_numbers)

        for index in range(n-1):
                if sorted_numbers[index] > sorted_numbers[index + 1]:
                    sorted_numbers[index], sorted_numbers[index + 1 ] = (sorted_numbers[index+ 1], sorted_numbers[index])

                    swapped = True 

    return sorted_numbers  

#Quit Loop
def quit_loop():
    print("Quitting Number Cruncher")
    


def main():
    while True: 
        result = show_menu()
        if result == "1":
            min_number_result = find_min(numbers)
            print(f"The minimum number is {min_number_result}.")

        elif result == "2":
            max_number_result = find_max(numbers)
            print(f"The maximum number is {max_number_result}.")

        elif result == "3":
            target = int(input("Enter a number: "))
            search_number_result = search(numbers, target)

            if search_number_result != -1:
                print(f"Found at index {search_number_result}.")

            elif search_number_result == -1:
                print("Not found")

        elif result == "4":
            sorted_list_result = bubble_sort(numbers)
            print(f"Sorted list: {sorted_list_result}")

        elif result == "5":
            quit_loop()
            break

        else:
            print("Please enter a number between 1 and 5.")

        

main()