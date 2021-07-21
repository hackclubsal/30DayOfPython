def part(array, l, h):
  pi = array[h]
  i = l - 1
  for j in range(l, h):
    if array[j] <= pi:
      i = i + 1
      array[i], array[j] = array[j], array[i]
  array[i + 1], array[h] = array[h], array[i + 1]
  return i + 1
  
def quick(array, l, h):
  if l < h:
    pi = part(array, l, h)
    quick(array, l, pi - 1)
    quick(array, pi + 1, h)

def List()
    data = [int(input()) for i in range(n)]
    size = len(data)-1
    return quick(data, 0, size),data

if __name__ == '__main__':
    n = int(input("Enter number: "))
    _,data = List()
    print(data)
