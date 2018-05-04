def troubleSort(L): # L is a 0-indexed list of integers
    done = False
    while not done:
      done = True
      for i in range(len(L) - 2):
        if L[i] > L[i + 2]:
          done = False
          L[i], L[i + 2] = L[i + 2], L[i]
    return L

def validate(L):
    for i in range(len(L) - 1):
        if L[i] > L[i + 1]:
            return i
    return 'OK'

def solve(L):
    sorted_L = troubleSort(L)
    return validate(sorted_L)

if __name__ == '__main__':
    i = int(input())
    for j in range(i):
        length = int(input())
        L = list(map(int, input().split(' ')))
        print('CASE #{}: {}'.format(j + 1, solve(L)))
