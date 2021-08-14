# p={40, 20, 30, 10, 30} 
class Solution:
  def MatrixChainMultiplicatin(p):
    
    m= [[0 for i in range(len(p))] for _ in range(len(p))]
    s= [[0 for i in range(len(p))]for _ in range(len(p))]

    length=len(p)
    min=0

    for i in range(1,length-1):
        for j in range(1,length-i):
            