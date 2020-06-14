# proble statement : array rotation with reversal algo

# time complexity O(n) : n = size of an array
# space complexity O(1)

# Python3 program to rotate an array by
# d elements
# Function to left rotate arr[] of size n by d*/

# utility function to print an array */


def printArray(arr, size):
    for i in range(size):
        print (str(arr[i])+" ")


def reverseArray(arr, start, end):
    i = start
    j = end
    while i < j:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i = i+1
        j = j-1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arrSize = 10


def RotateArr(arr, rotation, arrSize):
    reverseArray(arr, 0, rotation-1)
    reverseArray(arr, rotation, arrSize-1)
    reverseArray(arr, 0, arrSize-1)


def main():
    rotation = input("give number of rotation needed!")
    RotateArr(arr, rotation, arrSize)
    printArray(arr, arrSize)


if __name__ == "__main__":
    main()
