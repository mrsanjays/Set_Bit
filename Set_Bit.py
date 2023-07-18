def power(base,x):
    if x==0:
        return 1
    return base*power(base,x-1)
def Set_Bit(A,B):
    if A==B:
        return power(2,A)
    return power(2,A)+power(2,B)

if __name__ == '__main__':
    A=int(input())
    B=int(input())
    print(Set_Bit(A,B))
"""
You are given two integers A and B.
Set the A-th bit and B-th bit in 0, and return output in decimal Number System.
"""