#https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(raw_input())
    list1 = []
    for i in range(0,N):
        given_input = raw_input().split()
        if given_input[0] == 'insert':
            list1.insert(int(given_input[1]),int(given_input[2]))
        elif given_input[0] == 'print':
            print(list1)
        elif given_input[0] == 'remove':
            list1.remove(int(given_input[1]))
        elif given_input[0] == 'append':
            list1.append(int(given_input[1]))
        elif given_input[0] == 'sort':
            list1.sort()
        elif given_input[0] == 'pop':
            list1.pop()
        elif given_input[0] == 'reverse':
            list1.reverse()
            
