from Module.Tools import *
import random

def singleplayer():
    match_num = generate_random_number()
    print(f"[ 혼자 게임 ] 컴퓨터가 숫자를 생각했습니다. 맞춰보세요!")
    
    try_times = 0
    while True:
        guess_num = input("숫자를 입력해주세요 (세 자리 숫자): ")
        if not guess_num.isdigit() or len(guess_num) != 3:
            print("세 자리 숫자를 입력해주세요.")
            continue
        if guess_num[0] == guess_num[1] or guess_num[1] == guess_num[2] or guess_num[0] == guess_num[2]:
            print("중복되지 않는 세 자리 숫자를 입력해주세요.")
            continue

        try_times += 1
        strike, ball = calculate_strike_ball(match_num, guess_num)

        if strike == 3:
            print(f"홈런! 시도 횟수: {try_times}")
            break
        else:
            if strike == 0 and ball == 0:
                print("OUT.")
            elif strike > 0 and ball == 0:
                print(f"{strike}S")
            elif strike == 0 and ball > 0:
                print(f"{ball}B")
            else:
                print(f"{strike}S {ball}B")

def main():
    while True:
        try:
            ent = input("[ 시작 ] 방 호스트하기(1) / 방 참가하기(2) / 혼자서 게임하기(3): ")
            if ent == "1":
                host()
            elif ent == "2":
                join(input("호스트 IP를 입력해주세요: "))
            elif ent == "3":
                singleplayer()
            else:
                print("잘못된 입력입니다.")
        except ConnectionAbortedError:
            print("상대방의 연결이 끊어졌습니다. 처음으로 돌아갑니다.")
        except Exception as e:
            print(f"오류가 발생하였습니다: {e}. 처음으로 돌아갑니다.")

if __name__ == "__main__":
    main()
    