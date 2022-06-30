#tower of Hanoi in a single stack in python
def towerofHanoi(n, source, destination, aux):
    if n == 1:
        print(source, destination)
    else:
        towerofHanoi(n-1, source, aux, destination)
        print(source, destination)
        towerofHanoi(n-1, aux, destination, source)


n = int(input())
towerofHanoi(n, 'A', 'C')