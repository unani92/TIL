# import sys
# sys.stdin = open('sample_input.txt')

V, E = map(int, input().split())
G = [[] for _ in range(V)]

for _ in range(E) :
    u, v = map(int, input().split())
    G[u-1].append(v)
    G[v-1].append(u)

visited = [False] * V
cnt = 0
while False in visited :

    v = visited.index(0) + 1
    visited[v-1] = True
    stack = [v]

    while stack :
        p = v
        for w in G[v-1] :
            if not visited[w-1] :
                stack.append(w)
                visited[w-1] = True
                v = w
                break
        else :
            if p == v :
                v = stack.pop()

    cnt += 1

print(cnt)