


x = [5/4, 1/4,]
y = [1.5, 1.25, -1.25, -1.25, 0.75, -0.75, 0.75, -1.25, -1.25, 1.0]

L = len(x) - 1 
# Here L is 1
K = 5
# If your target symbol is 10-digit, then your K should be 9. Because 0 counts a position

current_candidates = []
current_candidates.append([1])
current_candidates.append([-1])

LookUpDict = {}

def checkScore(seq):
    K_temp = len(seq) - 1
    if (K_temp > 1):
        if str(seq) in LookUpDict:
            score1 = LookUpDict[str(seq)]
        else:
            score1 = checkScore(seq=seq[0:len(seq)-1])
        score3 = 0
        for n in range(K_temp - L, K_temp):
            score3 += seq[n]*x[n-K_temp]
        score2 = seq[K_temp]*(y[K_temp]-(1/2)*seq[K_temp]*x[0]-score3)
        return score1 + score2
    else:
        score4 = 0
        for n in range(0,K_temp+1):
            score4 += seq[n]*y[n]
        
        score5 = 0
        for n in range(0,K_temp+1):
            for m in range(0,K_temp+1):
                score5 += seq[n]*seq[m]*X_Lookup(n-m)
        return score4 - (1/2)*score5

def X_Lookup(somevalue):
    return x[abs(somevalue)]

now_K = 0
while (now_K <= K):
    if (now_K == 0):
        for candidate in current_candidates:
            score = checkScore(candidate)
            LookUpDict[str(candidate)] = score

    if (now_K > 0):
        if (now_K + 1  >= L):
            eliminateList = []
            for runner1 in current_candidates:
                for runner2 in current_candidates:
                    if (str(runner1) != str(runner2)) and (runner1[len(runner1)-L:len(runner1)]==runner2[len(runner2)-L:len(runner2)]):
                        if LookUpDict[str(runner1)] >= LookUpDict[str(runner2)]:
                            eliminateList.append(runner2)
                        else: 
                            eliminateList.append(runner1)

            for candidate in current_candidates:
                if candidate in eliminateList:
                    current_candidates.remove(candidate)
        
        current_candidates_new = []
        for candidate in current_candidates:
            score0 = checkScore( candidate + [1])
            score1 = checkScore( candidate + [-1])
            LookUpDict[str(candidate + [1])] = score0
            LookUpDict[str(candidate +[-1])] = score1
            current_candidates_new.append(candidate + [1])
            current_candidates_new.append(candidate + [-1])
        
        current_candidates = current_candidates_new
    now_K += 1

for candidate in current_candidates_new:
    print( str(candidate) + ", score is " + str(LookUpDict[str(candidate)]) )

    

    

