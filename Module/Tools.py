import random

def generate_random_number():
    while True:
        num = random.sample(range(10), 3)
        return ''.join(map(str, num))

def calculate_strike_ball(match_num, rec):
    strike = sum(1 for i in range(3) if rec[i] == match_num[i])
    ball = sum(1 for i in range(3) if rec[i] in match_num and rec[i] != match_num[i])
    return strike, ball

def send_feedback(conn, rec, strike, ball):
    if strike == 0 and ball == 0:
        conn.send("OUT.".encode())
        print(f"[ 게임 ] {rec} : OUT")
    elif strike > 0 and ball == 0:
        conn.send(f"{strike}S".encode())
        print(f"[ 게임 ] {rec} : {strike}S")
    elif strike == 0 and ball > 0:
        conn.send(f"{ball}B".encode())
        print(f"[ 게임 ] {rec} : {ball}B")
    else:
        conn.send(f"{strike}S {ball}B".encode())
        print(f"[ 게임 ] {rec} : {strike}S {ball}B")