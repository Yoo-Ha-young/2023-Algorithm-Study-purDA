# 1-13
## +와 -를 번갈아 출력하기 (2)

print('+와 -를 번갈아 출력합니다.')
n = int(input('몇 개 출력할깝쇼 ? :'))

for _ in range(n // 2):
    print('+-', end='')
if n % 2:
    print('+', end='')

#######################################################
'''
< for 문에 언더스코어(_)를 사용한 이유 >
- range() 함수가 for문을 순환하며 반환하는 값(인덱스)을 사용할 필요가 없기 때문.
- 파이선에서는 무시하고 싶은 값을 언더스코어로 표현할 수 있다.
'''
