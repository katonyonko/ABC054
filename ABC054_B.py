from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="054"
#問題
problem="b"

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
  N,M=map(int,input().split())
  A=[input() for _ in range(N)]
  B=[input() for _ in range(M)]
  ans='No'
  for i in range(N-M+1):
    for j in range(N-M+1):
      tmp=0
      for k in range(M):
        for l in range(M):
          if A[i+k][j+l]!=B[k][l]:
            tmp=1
      if tmp==0:
        ans='Yes'
  print(ans)
  """ここから上にコードを記述"""

  print(test_case[__+1])