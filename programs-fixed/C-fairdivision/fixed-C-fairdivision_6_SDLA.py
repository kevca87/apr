
def main():
    while True:
        try:
            N, M = map(int, input().split())
        except:
            break  # Exit the loop if input is not valid

        if N > 200:
            N = 200

        if N == 1:
            print(M, 1)
            continue
        
        lo = 1; hi = 1000000000*1000000000*10;
        ansnum=0; ansdenom=0;
        while(lo<hi):
            mid=(lo+hi)/2
            sums=0
            sums1=0
            curr=1.0
            for i in range(N):
                sums+=curr
                curr/=mid
               
            if sums>=M:
                ansnum=sums
                ansdenom=mid
                hi=mid
            else:
                lo=mid+1
        
        print(int(ansnum), '/', int(ansdenom))

main()
