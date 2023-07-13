from collections import *
from random import *
d = defaultdict(int)
n = 5
arr = [[] for i in range(n+1)]
rule = ['udp', 'tcp','pim', 'pcp','ospf', 'nos', 'ipinip', 'ip', 'igmp','icmp', 'gre', 'esp', 'eigrp', 'ahp']
totalaccess = 14 # tot
flagstr = ['Permit', 'Deny']
for _  in range(n):
    nums = randint(1,5)
    print('Ip access-list role-based', _)
    for __ in range(nums):
        flag = randint(0,1) # 0 means block, 1 means allow
        ind = randint(0,13)
        r = rule[ind]
        print(flagstr[flag], r)
        arr[_].append([flag,ind])
seen = defaultdict(int)
q = 5 
for _ in range(q):
    a = randint(-1,255)
    b = randint(-1,255)
    r = randint(0,n-1)
    if seen[(a,b)] :
        continue
    seen[(a,b)] = 1

    for flag, ind in arr[r]:
        p1 , p2 = a,b
        if p1 == -1:
            p1 = 'unknown'
        if p2 == -1:
            p2 = 'unknown'
        print('Cts role-based permissions from',a, 'to',b, 'from_rule',r)
        if a == -1:
            for j in range(256):
                d[(j,b,ind)] = flag
                seen[(j,b)] =1
        elif b == -1:
            for j in range(256):
                d[(a,j,ind)] = flag
                seen[(a,j)] = 1
        else:
            d[(a,b,ind)] = flag
def findPermForAPair(a,b):
    ans = []
    for i in range(len(rule)):
        if d[(a,b,r)]:
            ans.append(rule[r])
    return ans

def findPairsWithPerm(perm):
    ans = []
    try:
        r = rule.index(perm)
        for i in range(256):
            for j in range(i+1,256):
                if d[(i,j,r)]:
                    ans.append([i,j])
        return ans
    except:
        return 'No permission found'
while True:
    print('Welcom to Cisco Transfer  Security')
    print()
    print()
    inp = input('''
        Type 0 to exit 
        Type 1 to get the permissions between 2 IP addresses
        Type 2 to get all the Pair of addresses with a particular permission
''')
    inp = int(inp)
    if inp not in [0,1,2]:
        print('Wrong Selection !')
    elif inp == 0:
        break
    elif inp == 1:
        a = int(input('Enter the First address :'))
        b = int(input('Enter the Second address :'))
        ans = findPermForAPair(a,b)
        if ans == []:
            print('No Permission Found')
        else:
            print('Here are the permissions found b/w',a ,'and', b)
            print(*ans)
    else:
        perm = input('Enter the permission : ')
        print(findPairsWithPerm(perm))
        
        