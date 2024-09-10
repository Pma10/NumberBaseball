from Module.Game import *

def main():
    while True:
        try:
            ent = input("[ 시작 ] 방 호스트하기(1) / 방 참가하기(2): ")
            if ent == "1":
                host()
            elif ent == "2":
                join(input("호스트 IP를 입력해주세요: "))
            else:
                print("잘못된 입력입니다.")
        except ConnectionAbortedError:
            print("상대방의 연결이 끊어졌습니다. 처음으로 돌아갑니다.")
        except Exception as e:
            print(f"오류가 발생하였습니다: {e}. 처음으로 돌아갑니다.")

if __name__ == "__main__":
    main()
