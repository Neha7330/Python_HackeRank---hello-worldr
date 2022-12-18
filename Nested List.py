if __name__ == '__main__':
    students = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        scores.append(score)
        
min_score = min(scores)

while min_score in scores:
    scores.remove(min_score)
    
second_lowest_grades = min(scores)    

names = []
for i in range(len(students)):
    if second_lowest_grades == students[i][1]:
        names.append(students[i][0])

names.sort()
for name in names:
    print(name) 
