"""
사용자 정의 오류를 발생시키는 방법: (개발자가 직접 오류를 발생 시키겠다)
raise

"""

# age = int(input('나이를 입력 하세요 >>'))
# print('입력한 나이:', age)
# 정상적으로 입력 되었을 때 age 도 정상적으로 출력
# Actually, this is the same as input integer:
# But the limit is only for integers (which means that the minus age (-2,-3) are also permissible)

try:
    age = int(input('나이를 입력 하세요 >>'))
    if(age < 0):
        raise ValueError('Age must be either 0 or positive integer') # For instance, age such as -123, gramatically correct but logically wrong -> programmer should deal with it
                        # Now, when the input is a negative number, it returns ' Input wrong age '
    print('입력한 나이:', age)
except ValueError as e: # numbers with decimals (i.e. 12.3) or letters/ characters
    print(e.args)
# when we typed character (i.e. 11 -> invalid literal for int() with base 10: 'qq') => 10진수로 변환할 수 없다
# when typed negative integer (i.e. -93 : Age must be either 0 or positive integer => returned what we wrote)
# since -193 is an integer, there was no problem up to saving it up, but we put a raise statement => we forcefully made it an error
# args (https://www.geeksforgeeks.org/args-kwargs-python/)



