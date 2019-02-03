# python3
import sys

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def Swap(self, i, j):
    self._swaps.append((i, j))
    self._data[i], self._data[j] = self._data[j], self._data[i]

  def heapify(self, i):
    n = len(self._data)
    l = (i*2+1)
    r = (i*2+2)
    j = i

    min = self._data[i]

    if l < n:
      if self._data[l] < min:
        j, min = l, self._data[l]
    if r < n:
      if self._data[r] < min:
        j, min = r, self._data[r]
    
    if i != j:
      self.Swap(i, j)
      self.heapify(j)

  def GenerateSwaps(self):
    for i in range(len(self._data)//2-1, -1, -1):
      self.heapify(i)      

  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

def unit_test():
  heap_builder = HeapBuilder()
  heap_builder._data = [5, 4, 3, 2, 1]
  heap_builder.GenerateSwaps()
  heap_builder.WriteResponse()  

def main():
  heap_builder = HeapBuilder()
  heap_builder.Solve()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        unit_test()
    else:
        main()  
