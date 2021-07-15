def partition(array, low, high):
  pivot = array[high]
  i = low - 1
  for j in range(low, high):
    if array[j] <= pivot:
      i = i + 1
      array[i], array[j] = array[j], array[i]
  array[i + 1], array[high] = array[high], array[i + 1]
  return i + 1

# function to perform quicksort
def quickSort(array, low, high):
  if low < high:
    pi = partition(array, low, high)
    quickSort(array, low, pi - 1)
    quickSort(array, pi + 1, high)

def CreateList():
    # creating a list of n element using list comph...
    data = [int(input()) for i in range(n)]
    size = len(data)-1
    return quickSort(data, 0, size),data

if __name__ == '__main__':
    n = int(input("Enter the value of n : "))
    _,data = CreateList()
    print(data)
