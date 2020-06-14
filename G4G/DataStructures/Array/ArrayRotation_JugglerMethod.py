# Python3 program to rotate an array by
# d elements
# Function to left rotate arr[] of size n by d*/

# jugging method is used.

# time complexity O(size of an array)
# space complexity O(1)

# utility function to print an array */


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def printArray(arr, size):
    for i in range(size):
        print (str(arr[i])+" ")


def rotateLeft(arr, d, n):
    g_c_d = gcd(d, n)
    for i in range(g_c_d):
        temp = arr[i]
        j = i
        while 1:
            k = j + d
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def main():
    rotation = input("give number of rotation needed!")
    rotateLeft(arr, rotation, 10)
    printArray(arr, 10)


if __name__ == "__main__":
    main()
