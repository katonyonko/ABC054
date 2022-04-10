from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="054"
#問題
problem="c"

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
  from itertools import permutations
  N,M=map(int,input().split())
  G=[set() for _ in range(N)]
  for i in range(M):
    a,b=map(int,input().split())
    a-=1; b-=1
    G[a].add(b)
    G[b].add(a)
  ans=0
  for c in permutations(list(range(N-1))):
    tmp=0
    if c[0]+1 not in G[0]: tmp=1
    for i in range(N-2):
      if c[i+1]+1 not in G[c[i]+1]: tmp=1
    if tmp==0:
      ans+=1
  print(ans)
  """ここから上にコードを記述"""

  print(test_case[__+1])