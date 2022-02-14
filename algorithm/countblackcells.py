"""
def countBlackCells(n, m):
    ans = 0
    for i in range(m):
        for j in range(n):
            if j <= -n*i/m + n:
                if j >= -n*(i+1)/m + n-1:
                    ans += 1
                    print("i=",i,"j=",j,"ans=",ans)
    return ans
countBlackCells(2,5)

"""

def countBlackCells(n, m):
    ans = 0
    for i in range(m):
    	ans = ans + int(-float(n)*i/m+n) - int(-float(n)*(i+1)/m+n) + 1
    	print("i=",i,"ans=",ans)
    x,y = n,m
    while y != 0:
        x,y = y, x%y 
    print(y)
    if y > 1:
        return ans - 2 + y
    else:
        return ans - 1
countBlackCells(3,3)