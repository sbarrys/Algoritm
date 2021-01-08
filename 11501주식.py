

# 홍준이는 요즘 주식에 빠져있다. 그는 미래를 내다보는 눈이 뛰어나, 날 별로 주가를 예상하고 언제나 그게 맞아떨어진다. 매일 그는 아래 세 가지 중 한 행동을 한다.

#     주식 하나를 산다.
#     원하는 만큼 가지고 있는 주식을 판다.
#     아무것도 안한다.

# 홍준이는 미래를 예상하는 뛰어난 안목을 가졌지만, 어떻게 해야 자신이 최대 이익을 얻을 수 있는지 모른다. 따라서 당신에게 날 별로 주식의 가격을 알려주었을 때, 최대 이익이 얼마나 되는지 계산을 해달라고 부탁했다.

# 예를 들어 날 수가 3일이고 날 별로 주가가 10, 7, 6일 때, 주가가 계속 감소하므로 최대 이익은 0이 된다. 그러나 만약 날 별로 주가가 3, 5, 9일 때는 처음 두 날에 주식을 하나씩 사고, 마지막날 다 팔아 버리면 이익이 10이 된다.
# 입력

# 입력의 첫 줄에는 테스트케이스 수를 나타내는 자연수 T가 주어진다. 각 테스트케이스 별로 첫 줄에는 날의 수를 나타내는 자연수 N(2 ≤ N ≤ 1,000,000)이 주어지고, 둘째 줄에는 날 별 주가를 나타내는 N개의 자연수들이 공백으로 구분되어 순서대로 주어진다. 날 별 주가는 10,000이하다.
# 출력

# 각 테스트케이스 별로 최대 이익을 나타내는 정수 하나를 출력한다. 답은 부호있는 64bit 정수형으로 표현 가능하다.
# 예제 입력 1

# 3
# 3
# 10 7 6
# 3
# 3 5 9
# 5
# 1 1 3 1 2

# 예제 출력 1

# 0
# 10
# 5


f = int(input())

for _ in range(f):
  a = int( input() )

  dp =[ 0  for _ in range(a)]

  numbers = [ 0 for _  in range(a)]

  numbers = list (map( int, input().split()))

  maxnum = numbers[a-1]
  maxidx =  a-1
  summ=0
  for  i in range( a-2,-1,-1):
    if numbers[i] > maxnum:
      #여지껏 이익 구해주기
      for z in range(maxidx,i,-1):
        if maxnum-numbers[z]>0:
          summ += maxnum-numbers[z]
      maxnum =numbers[i]
      maxidx =i
    
    if i == 0 and maxidx!=0: 
      for z in range(maxidx,-1,-1):
        if maxnum-numbers[z]>0:
          summ += maxnum-numbers[z]

  print(summ)



#   어떻게 풀었는지 복습 : 

 #최대로 오른 날까지는 무조건사고 최대로 오른날 무조건파는것이다. 그이후도 마찬가지로 반복,  편하게 하기위해서 뒤에서 부터 햇다. 