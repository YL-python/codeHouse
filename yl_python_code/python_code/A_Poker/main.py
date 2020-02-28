import random

def Builder_Poker():  # 生成玩家手牌
    poker_color_kind = ["黑桃","红桃","梅花","方块"]
    poker_num_kind = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    poker_power = [x for x in range(54)]
    poker_all = list()
    for temp in poker_num_kind:
        poker_all.append(poker_color_kind[0] + temp)
        poker_all.append(poker_color_kind[1] + temp)
        poker_all.append(poker_color_kind[2] + temp)
        poker_all.append(poker_color_kind[3] + temp)
    poker_all.append('大鬼')
    poker_all.append('小鬼')
    print(len(poker_power))
    print(len(poker_all))
    poker_alls = [poker_all,poker_power]
    dict(poker_alls)
    print(poker_alls)
    # random.shuffle(poker_all)
    # return poker_all


def main():
    # 1 生成三个玩家的手牌
    poker_all = Builder_Poker()
    poker_player1 = poker_all[0:17]
    poker_player2 = poker_all[17:2 * 17]
    poker_player3 = poker_all[2 * 17:3 * 17]
    poker_finally = poker_all[3 * 17:]
    # print('底牌是：', poker_finally)
    # print('玩家一：', poker_player1)
    # print('玩家二：', poker_player2)
    # print('玩家三：', poker_player3)

if __name__ =="__main__":
    main()