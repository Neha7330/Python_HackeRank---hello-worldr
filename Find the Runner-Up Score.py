if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
score_list = list(arr)
max_score = max(score_list)

while max_score in score_list:
    score_list.remove(max_score)
    
score = max(score_list)
print(score)
