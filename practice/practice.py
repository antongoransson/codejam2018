
def percent_sum(x):
    return sum(map(round, x))

def solve(N, L, votes):
    while N != L:
        found = False
        l = len(votes)
        p = (1 / N) * 100
        new_votes1 = [v for v in votes]
        new_votes1.append(0)
        new_votes = list(map(lambda x: (x + p) % 1, new_votes1))
        i = new_votes.index(max(new_votes))
        if i == len(votes): votes.append(p)
        else: votes[i] += p
        L += 1
    return percent_sum(votes)


if __name__ == '__main__':
 n_tests = int(input())
 for i in range(n_tests):
     N, L = map(int, input().split())
     C = list(map(int, input().split()))
     default_p = [(x / N) * 100 for x in C]
     print("Case #{}: {}".format(i + 1, solve(N, sum(C), default_p)))
