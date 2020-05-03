def minimumBribes(q):
    bribe_count = 0
    for i in range(1, len(q)):
        if not q[i-1] == i:
            swaps = 0
            v = q[q[i-1]-1]
            z = q[i-1]
            while not q[i-1] == q[q[i-1]-1]:
                q[i-1], q[i] = q[i], q[i-1]
                bribe_count += 1
                swaps += 1
                i += 1
            if swaps > 2:
                return 'Too chaotic'

    return bribe_count

a = [2, 1, 5, 3, 4]

print(minimumBribes(a))
