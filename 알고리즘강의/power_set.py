def backtrack(selected, idx, n):
    #selected: 각노드의 선택 여부를 판단하는 배열
    # idx 깊이
    # n 목표 개수
    candidates = [0] * 2
    if idx == n:
        for i in range(n):
            if selected[i]:
                print(i, end=" ")
        print()
        return

    else:
        # n_candidate = make_condidate(candidates)
        # for i in range(n_candidate):
        #     selected[idx] = candidates[i]
        #     backtrack(selected, idx+1, n)
        selected[idx] = 1
        backtrack(selected, idx+1, n)
        selected[idx] = 0
        backtrack(selected, idx+1, n)
        
def make_condidate(candidates):
    candidates[0] = 1
    candidates[1] = 0
    return 2
    pass

N = 5
backtrack([0]*N, 0, N)