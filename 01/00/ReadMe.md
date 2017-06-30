# [11.8. 10 進浮動小数演算](https://docs.python.jp/3/tutorial/stdlib2.html#decimal-floating-point-arithmetic)

< [11. 標準ライブラリミニツアー — その 2](https://docs.python.jp/3/tutorial/stdlib2.html#brief-tour-of-the-standard-library-part-ii) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## [decimal](https://docs.python.jp/3/library/decimal.html#module-decimal)

> 財務アプリケーションやその他の正確な10進表記が必要なアプリケーション

> 精度の制御

> 法的または規制上の理由に基づく値丸めの制御

> 有効桁数の追跡が必要になる場合

> ユーザが手計算の結果と同じ演算結果を期待するようなアプリケーション

「手計算の結果と同じ」はユーザ的には当たり前の期待だと思うのだが、浮動小数点型の場合はどうしても誤差が出てしまうのだろう。

### 誤差

> 例えば、70 セントの電話代にかかる 5% の税金を計算しようとすると、10 進の浮動小数点値と 2 進の浮動小数点値では違う結果になってしまいます。

「10 進の浮動小数点値」とはdecimalのことで、「2 進の浮動小数点値」とはfloat,doubleのことだろう。

```python
from decimal import *
print(round(Decimal('0.70') * Decimal('1.05'), 2))
print(round(.70 * 1.05, 2))
```
```sh
$ python3 0.py 
0.74
0.73
```

> 上の例で、Decimal を使った計算では、末尾桁のゼロが保存されており、有効数字2桁の被乗数から自動的に有効数字を 4 桁と判断しています。Decimal は手計算と 同じ方法で計算を行い、2 進浮動小数が 10 進小数成分を正確に表現できないことに よって起きる問題を回避しています。

### 10進数の少数計算にはDecimalを使うと誤差をなくせる

> Decimal クラスは厳密な値を表現できるため、2 進浮動小数点数では 期待通りに計算できないような剰余の計算や等値テストも実現できます:

```python
from decimal import Decimal
print(Decimal('1.00') % Decimal('.10'))
print(1.00 % 0.10)

print(sum([Decimal('0.1')]*10) == Decimal('1.0'))
print(sum([0.1]*10) == 1.0)
```
```sh
$ python3 1.py 
0.00
0.09999999999999995
True
False
```

### 精度のコントロール

```python
import decimal
decimal.getcontext().prec = 36
print(decimal.Decimal(1) / decimal.Decimal(7))
decimal.getcontext().prec = 4
print(decimal.Decimal(1) / decimal.Decimal(7))
```
```sh
$ python3 2.py 
0.142857142857142857142857142857142857
0.1429
```

