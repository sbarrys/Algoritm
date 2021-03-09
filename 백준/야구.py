# 한이닝 3아웃 이닝 종료
# 총 N이닝(공격/수비) 게임

# 이닝동안은 1~9번타자가 친다.
# 직전의 다음타자가 친다.
# 타자바꾸는 함수를 지정하고
# 타자 idx 를 global 로 두자.
from itertools import permutations

n = int(input())# 총 이닝의 갯수
ining = []  #이닝 별 타자 별 성적
for i in range(n):
  a= list(map(int,input().split()))
  ining.append(a)
sum_score=0
max_score= 0
#(index+1)타순에 value 번 선수가 친다.
#4번타자는 0번선수로 고정
for order  in permutations(range(1,9),8):
  order= list(order[:3])+[0]+list(order[3:])
  # order=[4,5,6,0,1,2,3,7,8]
  base_1,base_2,base_3=0,0,0
  next_hitter=0
  out_cnt=0
  temp_score=0

  for i in range(n):
    while True:
      shot = ining[i][order[next_hitter]] #현재 타수가 낸 점수
      #다음타수 지정
      next_hitter+=1
      if next_hitter==9:
        next_hitter=0
      #점수에따라
      if shot==0:
        out_cnt+=1
        #3아웃이면 다음이닝
        if out_cnt==3:
          base_1,base_2,base_3=0,0,0
          out_cnt=0
          break
      elif shot==1:
        temp_score+=base_3
        base_1,base_2,base_3 = 1,base_1,base_2
      elif shot==2:
        temp_score+=base_2+base_3
        base_1,base_2,base_3 = 0,1,base_1
      elif shot==3:
        temp_score+=base_1+base_2+base_3
        base_1,base_2,base_3 = 0,0,1
      elif shot==4: 
        temp_score+=base_1+base_2+base_3+1
        base_1,base_2,base_3 = 0,0,0

  max_score=max(max_score,temp_score)
print(max_score)