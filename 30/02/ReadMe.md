# [4.4. 数値型 int, float, complex](https://docs.python.jp/3/library/stdtypes.html#numeric-types-int-float-complex)

< [4. 組み込み型](https://docs.python.jp/3/library/functions.html#built-in-functions) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## [4.4. 数値型 int, float, complex](https://docs.python.jp/3/library/stdtypes.html#numeric-types-int-float-complex)

### 基本

* 数値型には 3 種類あります: 整数 、 浮動小数点数 、 複素数 です。
    * ブール型は整数のサブタイプです。
* 整数には精度の制限がありません。
* 浮動小数点型はたいていは C の double を使って実装されています; あなたのプログラムが動作するマシンでの浮動小数点型の精度と内部表現は、 [sys.float_info](https://docs.python.jp/3/library/sys.html#sys.float_info) から利用できます。
* 複素数は実部と虚部を持ち、それぞれ浮動小数点数です。
    * 複素数 z から実部および虚部を取り出すには、 z.real および z.imag を使ってください。
        *  (標準ライブラリには、その他の数値型、分数を保持する [fractions](https://docs.python.jp/3/library/fractions.html#module-fractions) や、ユーザ定義の精度の浮動小数点数を保持する [decimal](https://docs.python.jp/3/library/decimal.html#module-decimal) があります。)

Pythonにはshort,int,longのような精度制限がないらしい。

### 生成

* 数値は、数値リテラルによって、あるいは組み込み関数や演算子の戻り値として生成されます。 (十六進、八進、二進数を含む) 
* 修飾のない整数リテラルは、整数を与えます。
* 小数点または指数表記を含む数値リテラルは浮動小数点数を与えます。
* 数値リテラルに 'j' または 'J' をつけると虚数 (実部がゼロの複素数) を与え、それに整数や浮動小数点数を加えて実部と虚部を持つ複素数を得られます。

```python
#!python3.6
print(bin(15))
print(oct(15))
print(15)
print(hex(15))

print(0.0)
print(7.2e+5)
print(7.2e-5)
print(int(7.2e+5))
print(float(7.2e-5))
print('{0:f}'.format(7.2e-5))

print(3+2j)
print(3+2J)
z = 3+2j
print(f'z={z}')
print(f'z.real={z.real}')
print(f'z.imag={z.imag}')
```
```sh
$ python 0.py 
0b1111
0o17
15
0xf
0.0
720000.0
7.2e-05
720000
7.2e-05
0.000072
(3+2j)
(3+2j)
z=(3+2j)
z.real=3.0
z.imag=2.0
```

### 混合型の演算

> Python は型混合の算術演算に完全に対応しています: ある二項算術演算子の被演算子の数値型が互いに異なるとき、より “制限された” 型の被演算子は他方の型に合わせて広げられます。ここで整数は浮動小数点数より制限されており、浮動小数点数は複素数より制限されています。型混合の数値間での比較も同じ規則に従います。 [2] コンストラクタ int() 、 float() 、 complex() で、特定の型の数を生成できます。

```python
#!python3.6
print(5+1.2)
print(6j)
print(1+2j)
print(3.1+5.2j)

print(bin(15)+bin(15))
print(bin(15)+oct(15)+hex(15))
#print(bin(15)+1) #TypeError: must be str, not int
```
```sh
$ python 1.py 
6.2
6j
(1+2j)
(3.1+5.2j)
0b11110b1111
0b11110o170xf
```

### 演算子

演算子|説明
------|----
`+`|和
`-`|差
`*`|積
`/`|商
`//`|商（切り下げ）
`%`|剰余
`-x`|符号反転
`+x`|`x`と同じ
`**`|乗

関数|説明
----|----
`abs(x)`|絶対値
`int(x)`|整数
`float(x)`|浮動小数点数
`complex(re, im)`|虚数
`c.conjugate()`|複素数 c の共役複素数
`divmod(x, y)`|(x // y, x % y) からなるペア
`pow(x, y)`|x の y 乗

```python
import math
print('1+2=', 1+2)
print('3-1=', 3-1)
print('2*3=', 2*3)
print('2**8=', 2**8)

print('1/2=', 1/2)
print('(-1)/2=', (-1)/2)
print('1/(-2)=', 1/(-2))
print('(-1)/(-2)=', (-1)/(-2))
print('6/2=', 6/2)
print('3/2=', 3/2)
print('4/3=', 4/3)

print('1//2=', 1//2)
print('(-1)//2=', (-1)//2)
print('1//(-2)=', 1//(-2))
print('(-1)//(-2)=', (-1)//(-2))
print('6//2=', 6//2)
print('3//2=', 3//2)
print('4//3=', 4//3)

print('6%2=', 6%2)
print('3%2=', 3%2)
print('4%3=', 4%3)
print('5%3=', 5%3)

print('-1=', -1)
print('+1=', +1)

print('abs(-5)=', abs(-5))
print('abs(-5.2)=', abs(-5.2))
print('int(5.2)=', int(5.2))
print('int(5.9)=', int(5.9))
print('int(-5.2)=', int(-5.2))
print('int(-5.9)=', int(-5.9))
print('math.floor(5.2)=', math.floor(5.2))
print('math.floor(5.9)=', math.floor(5.9))
print('math.floor(-5.2)=', math.floor(-5.2))
print('math.floor(-5.9)=', math.floor(-5.9))
print('math.ceil(5.2)=', math.ceil(5.2))
print('math.ceil(5.9)=', math.ceil(5.9))
print('math.ceil(-5.2)=', math.ceil(-5.2))
print('math.ceil(-5.9)=', math.ceil(-5.9))
print('float(123)=', float(123))
#print('float(+nan)=', float(+nan))#NameError: name 'nan' is not defined
#print('float(+inf)=', float(+inf))#NameError: name 'inf' is not defined
#print('float(-nan)=', float(-nan))#NameError: name 'nan' is not defined
#print('float(-inf)=', float(-inf))#NameError: name 'inf' is not defined
print('complex(5, 2)=', complex(5, 2))
print('complex(5)=', complex(5))
print('complex(5, 2).conjugate()=', complex(5, 2).conjugate())
print('divmod(5, 3)=', divmod(5, 3))
print('pow(2, 8)=', pow(2, 8))
```
```sh
$ python 2.py 
1+2= 3
3-1= 2
2*3= 6
2**8= 256
1/2= 0.5
(-1)/2= -0.5
1/(-2)= -0.5
(-1)/(-2)= 0.5
6/2= 3.0
3/2= 1.5
4/3= 1.3333333333333333
1//2= 0
(-1)//2= -1
1//(-2)= -1
(-1)//(-2)= 0
6//2= 3
3//2= 1
4//3= 1
6%2= 0
3%2= 1
4%3= 1
5%3= 2
-1= -1
+1= 1
abs(-5)= 5
abs(-5.2)= 5.2
int(5.2)= 5
int(5.9)= 5
int(-5.2)= -5
int(-5.9)= -5
math.floor(5.2)= 5
math.floor(5.9)= 5
math.floor(-5.2)= -6
math.floor(-5.9)= -6
math.ceil(5.2)= 6
math.ceil(5.9)= 6
math.ceil(-5.2)= -5
math.ceil(-5.9)= -5
float(123)= 123.0
complex(5, 2)= (5+2j)
complex(5)= (5+0j)
complex(5, 2).conjugate()= (5-2j)
divmod(5, 3)= (1, 2)
pow(2, 8)= 256
```

### int,float型で使える演算

関数|説明
----|----
`math.trunc(x)`|x を Integral (整数) に切り捨てます
`round(x[, n])`|x を n 桁に丸めます。丸め方は偶数丸めです。 n が省略されれば 0 がデフォルトとなります。
`math.floor(x)`|x 以下の最大の Integral (整数) を返します
`math.ceil(x)`|x 以上の最小の Integral (整数) を返します

* [math](https://docs.python.jp/3/library/math.html#module-math)
* [cmath](https://docs.python.jp/3/library/cmath.html#module-cmath)

```python
import math
print(math.trunc(3.14))
print(math.trunc(7.89))
print('----- round(x) -----')
for i in range(10): print(i, round(i+0.5), i+0.5)
print('----- round(x, 1) -----')
for i in range(10): print(i, round((i*0.1)+0.05, 1), (i*0.1)+0.05) # 浮動小数点の誤差がある
print('----- math.floor -----')
for i in range(10): print(i, math.floor(i+0.5), i+0.5)
print('----- math.ceil -----')
for i in range(10): print(i, math.ceil(i+0.5), i+0.5)
```
```sh
$ python 3.py 
3
7
----- round(x) -----
0 0 0.5
1 2 1.5
2 2 2.5
3 4 3.5
4 4 4.5
5 6 5.5
6 6 6.5
7 8 7.5
8 8 8.5
9 10 9.5
----- round(x, 1) -----
0 0.1 0.05
1 0.2 0.15000000000000002
2 0.2 0.25
3 0.4 0.35000000000000003
4 0.5 0.45
5 0.6 0.55
6 0.7 0.6500000000000001
7 0.8 0.7500000000000001
8 0.9 0.8500000000000001
9 1.0 0.9500000000000001
----- math.floor -----
0 0 0.5
1 1 1.5
2 2 2.5
3 3 3.5
4 4 4.5
5 5 5.5
6 6 6.5
7 7 7.5
8 8 8.5
9 9 9.5
----- math.ceil -----
0 1 0.5
1 2 1.5
2 3 2.5
3 4 3.5
4 5 4.5
5 6 5.5
6 7 6.5
7 8 7.5
8 9 8.5
9 10 9.5
```

