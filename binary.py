def solution(n):
         mod1=""
         while n!=0:
                  if(n!=0):
                           mod=str(n%2)
                           n=int(n/2)
                           mod1=mod+mod1
                  else:
                           return mod1
         print (mod1[::-1])
n=int(input())
solution(n)
