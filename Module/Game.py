import socket
from Module.Tools import *

PORT = 34568

def joingame(conn):
    try_times = 0
    while True:
        while True:
            guess_num = input("숫자를 입력해주세요 (세 자리 숫자): ")
            if not guess_num.isdigit() or len(guess_num) != 3:
                print("세 자리 숫자를 입력해주세요.")
                continue
            if guess_num[0] == guess_num[1] or guess_num[1] == guess_num[2] or guess_num[0] == guess_num[2]:
                print("중복되지 않는 세 자리 숫자를 입력해주세요.")
                continue
        conn.send(guess_num.encode())
        try_times += 1
        rec = conn.recv(1024).decode()
        if rec == "홈런.":
            print(f"홈런! 게임이 종료되었습니다. 시도 횟수: {try_times}")
            conn.close()
            break
        else:
            print(rec)

def hostgame(conn):
    match_num = generate_random_number()
    print(f"[ 게임 ] 상대방이 맞춰야 할 숫자: {match_num}")

    try_times = 0
    while True:
        rec = conn.recv(1024).decode()
        if not rec.isdigit() or len(rec) != 3:
            conn.send("세 자리 숫자를 입력해주세요.".encode())
            continue

        try_times += 1
        strike, ball = calculate_strike_ball(match_num, rec)

        if strike == 3:
            conn.send("홈런.".encode())
            conn.close()
            print(f"[ 게임 ] 게임 종료. 시도 횟수: {try_times}")
            break
        else:
            send_feedback(conn, rec, strike, ball)



def host():
    print("[ 호스트 ] 방 호스트 준비중..")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('0.0.0.0', PORT))
        s.listen(1)
        print("[ 호스트 ] 방 호스트 완료. 대기 중...")

        conn, addr = s.accept()
        with conn:
            allo = input(f"[ 호스트 ] IP {addr}님이 참여하셨습니다. 허용(1) / 거절(2): ")
            if allo == "1":
                conn.send("joined".encode())
                hostgame(conn)
            else:
                conn.send("denied".encode())

def join(ip):
    print("[ 참가 ] 방 참가 준비중..")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip, PORT))
        jl = s.recv(1024).decode()
        if jl != "denied":
            print("[ 참가 ] 방 참가 완료")
            joingame(s)
        else:
            print("[ 참가 ] 호스트가 참가를 거절하였습니다.")
