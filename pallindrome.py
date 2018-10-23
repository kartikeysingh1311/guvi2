def rev(x):
    z=0
    while x>0:
        r=x%10
        z=(z*10)+(r)
        x=(x//10)
    return z
def main():
    x=int(input())
    z=rev(x)
    if(x==z):
        print("pallindrome")
    else:
        print("no")
main()
