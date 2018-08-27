# 関数validateを定義してください
def validate(hand):
    # handの値によって条件分岐してください
    if hand<0 or hand>2:
        return False
    else:
        return True
    
def print_hand(hand, name='ゲスト'):
    hands = ['グー', 'チョキ', 'パー']
    print(name + 'は' + hands[hand] + 'を出しました')

print('じゃんけんをはじめます')
player_name = input('名前を入力してください：')
print('何を出しますか？（0: グー, 1: チョキ, 2: パー）')
player_hand = int(input('数字で入力してください：'))

# 関数validateの戻り値の値によって条件分岐してください
if validate(player_hand)==True:
    
    if player_name == '':
        print_hand(player_hand)
    else:
        print_hand(player_hand, player_name)
else:
    print('正しい数値を入力してください')