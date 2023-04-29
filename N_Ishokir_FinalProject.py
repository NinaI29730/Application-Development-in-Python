# N_Ishokir_FinalProject
# Written by: Nina Ishokir
# April 25, 2023
# Final Project

# Final Project main funtion
def main():
    arr = input_list()
    arr1 = []
    arr2 = []
    arr3 = []
   

    # Copy arr to 3 different array
    for i in range(len(arr)):
        arr1.append(arr[i]) #for Bubble Sort
        arr2.append(arr[i]) #for Selection Sort
        arr3.append(arr[i]) #for Insertion Sort
        

    # For Bubble Sort

    print("\nBefore Bubble Sort : ")
    print(arr1)
    com1 = bubbleSort(arr1)
    print("\nAfter Bubble Sort : ")
    print(arr1)
    print("\nNumber of comparison : ", com1)


    # For Selection Sort

    print("\nBefore Selection Sort : ")
    print(arr2)
    com2 = selectionSort(arr2)
    print("\nAfter Selection Sort : ")
    print(arr2)
    print("\nNumber of Comparison : ", com2)


    # For Insertion Sort

    print("\nBefore Insertion Sort : ")
    print(arr3)
    com3 = insertionSort(arr3)
    print("\nAfter insertion Sort : ")
    print(arr3)
    print("\nNumber of Comparison : ", com3)

    


# Function to ask the users to input 25 integers to create an array
def input_list():
    arr = []
    print("Enter 25 numbers : ")
    #for loop 25 times and input from user
    for i in range(25):
        n = int(input("Enter : "))
        arr.append(n)
    return arr

# Bubble sort will repeatedly swap adjacent number if they are unsorted
def bubbleSort(arr1):
    #size of arr1
    n = len(arr1)
    #variable to count comparison
    comp1 = 0
    # loop
    for i in range(n-1):
        # for loop
        for j in range(0, n-i-1):
            # comparson
            if arr1[j] > arr1[j + 1]:
                comp1 += 1
                #swap
                arr1[j], arr1[j+1] = arr1[j+1], arr1[j]
    #return comp1
    return comp1


# Selection sort will find minimum element and store to its correct place in unsorted array
def selectionSort(arr2):
    # variable for comparison
    comp2 = 0
    # loop
    for i in range(len(arr2)):
        #min index
        Min = i
        # for loop
        for j in range(i+1, len(arr2)):
            #comparison
            if arr2[Min] > arr2[j]:
                comp2 += 1
                Min = j

        # Swap the found minimum element with the first element
        arr2[i], arr2[Min] = arr2[Min], arr2[i]
    #return
    return comp2



# Insertion sort an array is split in two half and pick a number from unsorted part and store to its correct place in sorted array
def insertionSort(arr3):
    # variable for comparison
    comp3 = 0
    # for loop
    for i in range(1, len(arr3)):
        #key
        k = arr3[i]
        # Move elements of arr[0..i-1], that are greater than k, to one position ahead of their current position
        j = i-1
        while j >= 0 and k < arr3[j]:
            comp3 += 1
            arr3[j+1] = arr3[j]
            j -= 1
        arr3[j+1] = k
    return comp3

main()

	
