(N, K) = map(int,input().split())

item = [[0,0]]

for i in range(0, N):
    item.append(list(map(int,input().split())))

dp = [[0 for col in range(K+2)] for row in range(N+2)]

for i in range(1,N+1):
    
    weight = item[i][0] 
    val=item[i][1]
    
    for j in range(1,K+1):
        if j<item[i][0]: 
            dp[i][j]=dp[i-1][j]
        else: 
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-weight]+val)