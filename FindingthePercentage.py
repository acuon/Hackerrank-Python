#https://www.hackerrank.com/challenges/finding-the-percentage/problem

if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    
    scores = student_marks[query_name]#get the marks of student name stored in query_name
    average = sum(scores)/len(scores)#sum(scores) to add all the marks in scores list divide by the length of list
    average_score = "{:.2f}".format(average)#to print the average score with at most 2 decimals after point
    print(average_score)
