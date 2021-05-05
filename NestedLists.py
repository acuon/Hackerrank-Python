#https://www.hackerrank.com/challenges/nested-list/problem

output=[]
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    s=[name,score]
    
    output.append(s)
#print(output)
#print(output[0][1])
l = len(output)
#print(l)
stu = []
s_min=[]


#for i in range(0,l-1):
#    for j in range(0,l-i-1):
#        if(output[j][1]>output[j+1][1]):
#            temp = output[j]
#            output[j] = output[j+1]
#            output[j+1] = temp
output.sort(key = lambda x:x[1])
#print(output)


min_output = min(output,key = lambda x:x[1])
#print(min_output,"i am here")
#print(min_output[1])

for i in range(0,l):
    if (min_output[1] != output[i][1]):
        stu.append(output[i])

#print(stu)

for i in range(0,len(stu)):
    if(stu[i][1] == stu[0][1]):
        s_min.append(stu[i][0])
#print(s_min)
s_min.sort()      
for i in range(0,len(s_min)):
    print(s_min[i])



#just an incomplete code
#for i in range(0,l):
#    if (output[i][1] > min_output[1]):
#        s_lowest_index = i
#    break
#    print(s_lowest_index)

#print(s_lowest_index,"hey")
