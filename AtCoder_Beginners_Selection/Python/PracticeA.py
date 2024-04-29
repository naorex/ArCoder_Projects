# 整数の入力
a = int(input())
# スペース区切りの整数の入力
b, c = map(int, input().split())

'''
split() メソッドは、入力された文字列をデフォルトでは空白文字 (' ') で区切り、サブストリングのリストを返します。
例えば、ユーザーが 10 20 と入力すると、 ['10', '20'] というリストが生成されます。

map(int, input().split()) は、リストの各要素に int 関数を適用し、文字列を整数に変換します。
結果は、イテレータとなります。
'''

# 文字列の入力
s = input()
# 出力
print(a+b+c, s)
