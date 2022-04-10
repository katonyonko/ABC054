from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="054"
#問題
problem="d"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/abc{0}_{1}".format(times, problem)) as res:
  html = res.read().decode("utf-8")
# 2. Load a html by BeautifulSoup.
soup = BeautifulSoup(html, "html.parser")
# 3. Get items you want.
test_case = soup.select(".lang-ja pre")
test_case =[t.text for t in test_case[1:]]
x = '''
'''
y = '''
'''
additional_case = []
test_case += additional_case

for __ in range(0,len(test_case),2):
  sys.stdin = io.StringIO(test_case[__])

  """ここから下にコードを記述"""
  N,Ma,Mb=map(int,input().split())
  chemicals=[list(map(int,input().split())) for _ in range(N)]
  chemicals=[(chemicals[i][0]*(-Mb)+chemicals[i][1]*Ma,chemicals[i][2]) for i in range(N)]
  c1,c2=dict(),dict()
  ans=10**10
  for i in range(1,2**(N//2)):
    d,e=sum([chemicals[j][0] for j in range(N//2) if (i>>j)&1==1]),sum([chemicals[j][1] for j in range(N//2) if (i>>j)&1==1])
    if d==e==0: print(i)
    if d in c1: c1[d]=min(c1[d],e)
    else: c1[d]=e
    if d==0: ans=min(ans,e)
  for i in range(1,2**(N-N//2)):
    d,e=sum([chemicals[j+N//2][0] for j in range(N-N//2) if (i>>j)&1==1]),sum([chemicals[j+N//2][1] for j in range(N-N//2) if (i>>j)&1==1])
    if d in c2: c2[d]=min(c2[d],e)
    else: c2[d]=e
    if d==0: ans=min(ans,e)
  for key in c1:
    if -key in c2:
      ans=min(ans,c1[key]+c2[-key])
  if ans==10**10: print(-1)
  else: print(ans)
  """ここから上にコードを記述"""

  print(test_case[__+1])