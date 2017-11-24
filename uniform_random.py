# 離散的な値をもつ分布にしたがう乱数を計算するシミュレーション

def uniform_coin():
    x = random.uniform(0, 1)
    if x < 0.5:
        y = "on"
    else:
        y = "off"

def common_coin(p):
    x = random.uniform(0, 1)
    if p < 0.5:
        y = "on"
    else:
        y = "off"

def common_dice(p1, p2, p3, p4, p5):
    x = random.uniform(0, 1)
    if x < p1:
        print(1)
    elif x < p1 + p2:
        print(2)
    elif x < p1 + p2 + p3:
        print(3)
    elif x < p1 + p2 + p3 + p4:
        print(4)
    elif x < p1 + p2 + p3 + p4 + p5:
        print(5)
    else:
        print(6) 

def main():
    pass
