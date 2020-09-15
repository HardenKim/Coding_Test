import collections



def solution(n, s, a, b, fares):
    answer = float("inf")
    graph = collections.defaultdict(list)
    flag_a, flag_b = False, False
    for u, v, w in fares:
        graph[u].append((v,w))
        graph[v].append((u,w))
    print(graph)
    
    
    answer = float("inf")
    
    def fs(arr, ret, cnt):
        print(arr)
        if cnt > 15:
            return
        if ret > answer:
            return
        if len(arr) >=4:
            if arr[-2:] == arr[-4:-2]:
                return
        elif len(arr) >= 8:
            if arr[-4:] == arr[-8:-4]:
                return
        if a in arr and b in arr:
            print("!!!!!!!!!!!!!!")
            answer = min(answer, ret)
            return
        
        
        for _next in graph[arr[-1]]:
            arr.append(_next[0])
            fs(arr, ret+_next[1], cnt+1)
            
    
    fs([s], 0, 0)
    
    
    
    return answer
    
fares =[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
n, s, a, b = 7,3,4,1
#fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
#n, s, a, b = 6, 4, 6, 2
print(solution(n, s, a, b, fares))