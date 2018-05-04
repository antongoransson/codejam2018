def damage(seq):
    m = 1
    dmg = 0
    for i in seq:
        if i == 'C': m *= 2
        elif i == 'S': dmg += m
    return dmg

def solve(seq, max_dmg):
    list_seq = [s for s in seq]
    hacks = 0
    c_ind = len(list_seq) - 1
    last_ind = len(list_seq) - 1
    while damage(list_seq) > max_dmg and last_ind >= 0:
        c_ind = ''.join(list_seq).rfind('C', 0,  last_ind)
        if list_seq[c_ind + 1] == 'S' and c_ind != -1:
            hacks += 1
            list_seq[c_ind], list_seq[c_ind + 1] = list_seq[c_ind + 1], list_seq[c_ind]
        else:
            last_ind = c_ind - 1
    if damage(list_seq) <= max_dmg:
        return hacks
    return 'IMPOSSIBLE'


if __name__ == '__main__':
    i = int(input())
    for j in range(i):
        a = input().split(' ')
        max_dmg = int(a[0])
        seq = a[1]
        print('CASE #{}: {}'.format(j + 1, solve(seq, max_dmg)))
