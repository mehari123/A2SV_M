class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        
        if n==1 or n==-1 or n==0:
            
            return x**n
        
        if n%2==0:
        
            return self.myPow(x,n//2)**2
        
        else:
            
            return self.myPow(x,n//2)**2*x
            
            
            
        
        
        