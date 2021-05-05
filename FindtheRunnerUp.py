#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())

arr.sort()
#print(arr)
n=len(arr)
#print(n)

for i in range(n):
    #print(i)
    r_up = arr[i]
    if (r_up<arr[n-1]):
        temp = r_up
        
    #if (temp<r_up and r_up<arr[n-1]):
    #    runner_up = r_up
        
print(temp)
    
