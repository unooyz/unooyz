#-*-coding:cp949
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s those who %s." % (binary, do_not) # %s�� () �ȿ��ִ� ���� ������ ���Եȴ�.
# ����׸� �ص� ���������  print�� ���� Console�� ǥ�õǴ°� ����.
print x
print y

print "I said: %r." % x
print  "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r" #���ڿ��� ���� �Ǵ� ��

print joke_evaluation % hilarious # �̹� joke_evaluation�� ""(������ǥ)�� �پ����̶����� �� �࿡���� ""�� ���� �ʿ� ����

w = "This is the lefg side of..."
e = "a string with a right side."

print w+e  # +�� �ǹ̴� ����(���ڿ�)�� �̾� �����ִ� ����
