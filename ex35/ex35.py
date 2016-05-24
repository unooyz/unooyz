from sys import  exit

def gold_room():
    print "this room is full of gold. How much do you take?"

    choice = raw_input(">")
    if "0" in choice or "1" in choice:
        how_much = int(choice) #int 안에서 choice는 상수항을 써야한다.
    else:
        dead("man, learn to type a number.")

    if how_much < 50:   #가급적 상수를 오른쪽으로 쓰는게 좋음. 코드 오류를 방지하기 위해서 ==와 =를 실수하는경우가 많아 상수=문자 가 안되고 문자=상수만 되므로 오류를 쉽게 잡아낼수있음.
        print "Nice. you're not greedy, you win!"
        exit(0)
    else :
        dead("You greedy bastard")


def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        choice = raw_input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."   # if elif 문을 스위치 뮈시기 라고 함 ㅋ

def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    choice = raw_input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()
        #계속해서 반복되는 함수 재귀호출(recursion) - 시험출제!
        # 함수 호출때마다 call stack 이 쌓임 (디버그) - 무한반복시 call stack 이 계속쌓여 컴퓨터 과부화가 됨(stack overflow)


def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    choice = raw_input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()


# 구조적프로그램 (structural programming)
# 1개의 기능에 1개의 함수를 만드는 것   1을 실행하기 위해서 1에서만 쓰이는 함수를 만듬 - 오류를 찾아내서나 기능추가, 수정이 쉬움


# 객체 지향프로그램 ( Object oriental programming)





