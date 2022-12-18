if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    list_marks = student_marks[query_name]
    list_len = len(list_marks)
    total = sum(list_marks)
    
    average_score = round(total/ list_len, 2)
    print('{0:.2f}'.format(average_score))
