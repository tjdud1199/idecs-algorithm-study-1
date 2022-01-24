'''
< 음유시인 영재 >
- 시는 대문자, 소문자, 알파벳과 빈칸으로 이루어져 있다.
- 시에 나오는 단어들의 첫 글자를 대문자로 바꾼 뒤 순서대로 이어서 제목으로 만든다.
- 스페이스 바와 영자판을 누를 수 있는 횟수가 정해져 있다.
- 같은 문자가 연속으로 나오거나 빈칸이 연속으로 나오는 경우 한번만 사용해도 된다.
- 시의 내용과 시의 제목은 Enter 키로 구분된다.
- 시의 내용과 제목을 모두 기록할 수 있다면 시의 제목 출력, 기록을 완벽하게 못한다면 -1 출력
- 대소문자 구분한다.

< 아이디어 >
- 영자판의 사용횟수 담는 딕셔너리 만들기
- 딕셔너리에 음수값이 생기면 -1을 출력한다.
- pre 와 post에 이전 값과 현재 값을 저장해 비교해준다.
'''

import string
import sys
input = sys.stdin.readline
from string import ascii_lowercase

poem = input().rstrip()
space = int(input())
alpha = [i for i in string.ascii_lowercase]
num = list(map(int, input().split()))

# 사용횟수 담는 리스트를 생성한다.
eng_use = dict(zip(alpha, num))

# 시의 제목 만들기
title = ''.join(a[0].upper() for a in poem.split())
poem += title

# 시의 내용과 제목에 대해서 가능한지 확인한다
pre = poem[0]
eng_use[pre.lower()] -= 1
if eng_use[pre.lower()] < 0:
    print(-1)
    sys.exit(0)

for s in poem[1:]:
    if pre == s:
        continue
    if s == ' ':
        space -= 1
        if space < 0:
            print(-1)
            sys.exit(0)
    else:
        pre = s
        eng_use[s.lower()] -= 1
        if eng_use[s.lower()] < 0:
            print(-1)
            sys.exit(0)

pre = title[0]
result = str(pre)
eng_use[pre] -= 1
if eng_use[pre] < 0:
    print(-1)
    sys.exit(0)

for s in title[1:]:
    if pre == s:
        continue
    eng_use[s] -= 1
    if eng_use[s] < 0:
        print(-1)
        sys.exit(0)
    result += s
    pre = s

print(result.upper())



# 다시 짜보기
import string
import sys
input = sys.stdin.readline
from string import ascii_lowercase

poem = input().rstrip()
space = int(input())

# 사용횟수 담는 리스트를 생성한다.
eng_use = dict(zip([i for i in string.ascii_lowercase], list(map(int, input().split()))))

# 시의 제목 만들기
title = ''.join(a[0].upper() for a in poem.split())
poem += title

# 시의 내용과 제목에 대해서 가능한지 확인한다
pre = poem[0]
eng_use[pre.lower()] -= 1
if eng_use[pre.lower()] < 0:
    print(-1)
    sys.exit(0)

for s in poem[1:]:
    if pre == s:
        continue
    if s == ' ':
        space -= 1
        if space < 0:
            print(-1)
            sys.exit(0)
        pre = s
    else:
        pre = s
        eng_use[s.lower()] -= 1
        if eng_use[s.lower()] < 0:
            print(-1)
            sys.exit(0)

else:
    print(title.upper())