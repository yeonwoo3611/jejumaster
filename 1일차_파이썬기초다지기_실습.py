'''#설치된 파이썬 버전 출력
import sys
print('파이썬 버전: %s ' % sys.version)
print(f'파이썬 버전: {sys.version} ')

#파이썬 실행파일 위치
print(f'파이썬 실행파일 위치: {sys.executable} ')'''

'''#사칙연산
num1 = int (input('첫번째 숫자:'))
num2 = int (input('두번째 숫자:'))

print('-'*50)

#덧셈
print(f'덧셈:{num1}+{num2}={num1+num2}')

#뺄셈
print(f'뺄셈:{num1}-{num2}={num1-num2}')

#곱셈
print(f'곱셈:{num1}*{num2}={num1*num2}')

#몫
print(f'몫:{num1}//{num2}={num1//num2}')

#나머지
print(f'나머지:{num1}%{num2}={num1%num2}')'''

# 정수a를 입력받아 a+aa+aaa의 결과 값을 구하는 코드
'''a=int(input('정수를 입력하세요:'))
answer=a+(a*11)+(a*111)
print(f'결과:{a}+{a*11}+{a*111}={answer}')


a = input('숫자 입력: ')
aaa = int(a+a+a)
aa = int(a+a)
a = int(a)
print(f'{a} + {aa} + {aaa} = {a+aa+aaa}')



a = input('정수를 입력하시오 :')
aa = int(a+a)
aaa = int(a+a+a)
a = int(a)

print(f'{a} + {aa} + {aaa} = {a+aa+aaa}' )'''


'''print("Mary’s cosmetics")

print('박씨가 소리질렀다."도둑이야!"')'''

# 파일 읽어서 음성으로 출력하기
'''from gtts import gTTS
from IPython.display import Audio

with open("./오감도.txt", 'r') as f:
    s = f.read()
    print(s)

kor_wav = gTTS(s, lang = 'ko')
kor_wav.save('kor.wav')

display(Audio('kor.wav', autoplay=True))'''

#문자열 거꾸로 출력
'''s = input('문자열입력: ')
print(s[::-1])'''

'''
meal, tax, tip =4450, 0.0675, 0.15
tax=meal*tax #세금
meal = meal+tax
tip=meal*tip
total = meal+tip

print(f'내가 지불해야할 총 금액은:{total}')'''


#동전 교환 프로그램 만들기
'''a = int(input('동전으로 교환할 금액을 입력하세요: '))
a1 = a // 500
a2 = (a % 500) // 100
a3 = ((a % 500) % 100) // 50
a4 = (((a % 500) % 100) % 50) // 10
a5 = (((a % 500) % 100) % 50) % 10
print('--' * 20)
print(f'500원짜리 ==> {a1} 개')
print(f'100원짜리 ==> {a2} 개')
print(f'50원짜리 ==> {a3} 개')
print(f'10원짜리 ==> {a4} 개')
print(f'잔돈 ==> {a5} 개')'''


#중첩리스트에서 파이썬 출력하기
'''a = [1, 2, ['a', 'b', ['사랑해', '파이썬']], 3]
print(a[2][2][1])'''

a=int(input("첫 번째 변의길이:"))
b=int(input("두 번째 변의길이:"))
c=int(input("세  번째 변의길이:"))
if a**2+b**2==c**2:
    print("직각삼각형")
else:
    print("직삼이아니오")
