# 튜플(Tuple)
## - 튜플은 몇 가지 점을 제외하곤 리스트와 거의 비슷하다.
t1 = () # 튜플은 ()로 둘러싼다.
t2 = (1,) # 1개의 요소만을 가질 때는 요소 뒤에 콤마(,)를 반드시 붙여야 한다.
t3 = (1,2,3)
t4 = 1,2,3
t5 = ('a','b',('ab','cd'))


# 튜플의 요솟값 변경
# - 튜플은 값은 바꿀 수 없다.
## 1. 튜블 요솟값 삭제
t1 = (1,2,'a','b')
del t1[0] # 튜플 t1의 0번째 요소를 삭제 => Type Error

## 2. 튜플 요솟값 변경
t1 = (1,2,'a','b')
t1[0] = 'c' # 튜플 t1의 0번째 요소를 변경 => Type Error


# 튜플 다루기
## 1. 인덱싱하기
t1 = (1,2,'a','b')
t1[0]
t1[3]

## 2. 슬라이싱
t1 = (1,2,'a','b')
t1[1:] # 1부터 끝까지

## 3. 튜플 더하기
t1 = (1,2,'a','b')
t2 = (3,4)
t1 + t2

## 4. 튜플 곱하기
t2 = (3,4)
t2 * 3

## 5. 튜플 길이 구하기
t1 = (1,2,'a','b')
len(t1)