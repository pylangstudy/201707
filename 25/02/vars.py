#vars([object])
print(vars()) # 引数がなければ、vars() は locals() のように振る舞います。ただし、辞書 locals への更新は無視されるため、辞書 locals は読み出し時のみ有用であることに注意してください。
class A: pass
print(vars(A)) # __dict__ 属性を返します。
