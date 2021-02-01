import sys
sys.setrecursionlimit(10**7)
a=0
def split(p):
    left =-1
    right=-1
    for idx in range( len(p)):
        
        if p[idx] =='(':
            left+=1
        else:
            right+=1
        if right == len(p)//2:
            return len(p)
        if left>=0 and left==right:
            return idx+1 #idx가 len(p와 같으면 올바른 문자열이다.)
    return len(p)
def check_correct(p):
    left=0
    right=0
    for idx in range( len(p)):
        
        if p[idx] =='(':
            left+=1
        else:
            right+=1
        if right>left :
            return False
    if left==right:
        return True
    else:
        return False
def make_reverse(p):
    temp=""
    for i in range(len(p)):
        if p[i]=='(':
            temp+=')'
        else :
            temp+='('
    return temp
def correct(p):
    #1
    if len(p)==0:
        return ""    
    #2
    split_idx = split(p)
    
    front = p[:split_idx]
    back = p[split_idx:]
    if check_correct(front):   
        return front+correct(back)
    else:
        return '('+correct(back) +')'+  make_reverse(front[1:-1])
    

def solution(p):
    answer = ''
    if len(p)==0:
        return ""
    answer  = correct(p)
    return answer