class Solution:
    def isHappy(self, n: int) -> bool:
        if n < 9:
            n*=n
        
        while(n > 9):
            mysum = 0
            while(n > 0):
                mysum += (n%10)**2
                n//=10
            print(mysum)
            n = mysum
        
        return(n==1)
        