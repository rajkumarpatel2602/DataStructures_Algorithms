# proble statement : array rotation without temp array

# time complexity O(size*rotations)
# space complexity O(1)

# Python3 program to rotate an array by
# d elements
# Function to left rotate arr[] of size n by d*/

# utility function to print an array */


def printArray(arr, size):
    for i in range(size):
        print (str(arr[i])+" ")


def leftRotateByOne(arr, size):
    temp = arr[0]
    for i in range(size-1):
        arr[i] = arr[i+1]
    arr[size-1] = temp


def leftRotate(arr, rotation, size):
    for i in range(rotation):
        leftRotateByOne(arr, size)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def main():
    rotation = input("give number of rotation needed!")
    leftRotate(arr, rotation, 10)
    printArray(arr, 10)


if __name__ == "__main__":
    main()
