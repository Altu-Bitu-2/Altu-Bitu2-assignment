MAX=50000
square=[i**2 for i in range(int(MAX**0.5)+1)] #MAX까지의 제곱수 

#한 개의 제곱수 구성인지 판단하는 함수
def is_one_square(n):
    return (n**0.5).is_integer()

#두 개의 제곱수 구성인지 판단하는 함수
def is_two_square(n):
    for i in range(int(n**0.5),0,-1):
        if is_one_square(n-square[i]):
            return True 
    return False

#세 개의 제곱수 구성인지 판단하는 함수
def is_three_square(n):
    for i in range(int(n**0.5),0,-1):
        temp_i=n-square[i]
        if is_two_square(temp_i):
                return True
    return False
            
n=int(input())

if is_one_square(n):
    print(1)
elif is_two_square(n):
    print(2)
elif is_three_square(n):
    print(3)
else:
    print(4)
