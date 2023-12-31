## 리스트와 튜플
- 파이썬에서는 배열을 리스트와 튜플로 구현할 수 있다.
- 리스트와 튜플은 데이터컨테이너라한다.
- 리스트는 뮤터블 자료형이고 튜플은 이뮤터블 자료형이다.

- **뮤터블 자료형** : 리스트, 딕셔너리, 집합 등이 있으며 값을 변경할 수 있다.
- **이뮤터블 자료형** : 수, 문자열, 튜플 등이 있으며 값을 변경할 수 없다.


### 리스트 언팩
```
x = [1, 2, 3] # 리스트 x 선언
a, b, c = x # x를 언팩하여 변수 a, b, c에 대입
a, b, c


>>> (1, 2, 3)
```

### 리스트 내포 표기 생성
- 리스트 안에서 for, if 문을 사용해서 새로운 리스트를 생성하는 기법
```
numbers = [1, 2, 3, 4, 5]
twise = [num * 2 for num in numbers if num % 2 == 1]
print(twise)
>>> [2, 6, 10]
```
### 주석과 자료형 힌트
`from typing import Any, Sequence`

- Any : 제약이 없는 임의의 자료형을 의미
- Sequence :  시퀀스형을 의미, 시퀀스형에는 리스트형 바이트 배열형, 문자열형, 튜플형, 바이트열형이 있음

### enumerate()
- 원소를 짝지어 튜플로 꺼내는 내장함수이다.
- 인덱스값을 따로 지정하지 않아도 되는 이유는 이터러블 객체 = 순차 반복 객체이기 때문이다.

### 배열 원소를 역순으로 정렬하기
`[2,5,1,3,9,6,7] -> [7,6,9,3,1,5,2]`
- 교환 횟수 = 원소 수 // 2
- 원소 수가 홀수인 경우에 가운데 원소는 교환할 필요가 없음
- 정수//정수 연산에서는 나머지(소숫값)는 버리고 정숫값만 얻을 수 있다. 예를 들어 7//2는 3이 된다.
```
# 뮤터블 시퀀스 원소를 역순으로 정렬
from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n // 2): 
        # 역순으로 바꿀 때는 배열 갯수의 반 번만 실행 하면 되므로 n//2
        a[i], a[n-i-1] = a[n-i-1], a[i] # n이 배열의 마지막 원소이고 n - i 실행 될 때마다 뒤에서 i번 옮겨가면서 순회
        
if __name__ == '__main__':
    print('배열 원소를 역순으로 정렬합니다.')
    nx = int(input('원소 수를 입력하세요.: '))
    x = [None] * nx # 원소 수가 nx인 리스트를 생성
    
    for i in range(nx):
        x[i] = int(input(f'x[{i}]값을 입력하세요.: '))
        
    reverse_array(x) # x를 역순으로 정렬
    
    print('배열 원소를 역순으로 정렬했습니다.')
    for i in range(nx):
        print(f'x[{i}] = {x[i]}')
```
