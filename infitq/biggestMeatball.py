def meatball(N, D, queue)->int:
    queue = [queue[i]/D for i in range(N)]
    person = queue.index(max(queue))
    return person+1


if __name__ == '__main__':
    N = int(input("Enter the number of Meatballs: "))
    D = int(input("Enter the number of days: "))
    queue = list(map(int,input("Enter the meatballs: ").split(' ')))
    print(meatball(N, D, queue))