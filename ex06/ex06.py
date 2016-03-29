#-*-coding:cp949
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s those who %s." % (binary, do_not) # %s는 () 안에있는 순서 순으로 기입된다.
# 디버그를 해도 여기까지는  print가 없어 Console에 표시되는게 없다.
print x
print y

print "I said: %r." % x
print  "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r" #문자열이 내삽 되는 곳

print joke_evaluation % hilarious # 이미 joke_evaluation에 ""(끈따움표)가 붙어있이때문에 이 행에서는 ""가 붙을 필요 없음

w = "This is the lefg side of..."
e = "a string with a right side."

print w+e  # +의 의미는 문자(문자열)을 이어 붙혀주는 역할
