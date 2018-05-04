

if __name__ == '__main__':
 n_tests = int(input())
 for i in range(n_tests):
     N, L = map(int, input().split())
     C = list(map(int, input().split()))
     default_p = [(x / N) * 100 for x in C]
     print("Case #{}: {}".format(i + 1, solve(N, sum(C), default_p)))
