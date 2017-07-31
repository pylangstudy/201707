# [4.4.4. 数値型のハッシュ化](https://docs.python.jp/3/library/stdtypes.html#hashing-of-numeric-types)

< [4.4. 数値型 int, float, complex](https://docs.python.jp/3/library/stdtypes.html#numeric-types-int-float-complex) < [4. 組み込み型](https://docs.python.jp/3/library/functions.html#built-in-functions) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## [4.4.4. 数値型のハッシュ化](https://docs.python.jp/3/library/stdtypes.html#hashing-of-numeric-types)

> 数 x と y に対して、型が異なっていたとしても、 x == y であれば必ず hash(x) == hash(y) であることが要請されます (詳細は __hash__() メソッドドキュメントを参照してください)。実装の簡単さと 複数の数値型 (int 、 float 、 decimal.Decimal 、 fractions.Fraction を含みます) 間の効率のため、Python の 数値型に対するハッシュ値はある単一の数学的関数に基づいていて、 その関数はすべての有理数に対し定義されているため、 int と fractions.Fraction のすべてのインスタンスと、 float と decimal.Decimal のすべての有限なインスタンスに 対して適用されます。本質的には、この関数は定数の素数 P に対して P を法とする還元で与えられます。 値 P は、 sys.hash_info の modulus 属性として Python で利用できます。

> CPython 実装の詳細: 現在使われている素数は、32 bit C long のマシンでは P = 2**31 - 1 、 64-bit C long のマシンでは P = 2**61 - 1 です。

意味不明。そもそもハッシュ値って何？

http://wa3.i-3-i.info/word11949.html

何のために使うのか？学習する必要はあるのか？

### 詳細な規則

> 詳細な規則はこうです:

> * x = m / n が非負の有理数で、 n が P で割り切れないなら、 invmod(n, P) を n を P で割った剰余の (剰余演算の意味での) 逆数を与えるものとして、 hash(x) を m * invmod(n, P) % P と定義します。

> * x = m / n が非負の有理数で、 n が P で割り切れる (が m は割り切れない) なら、 n は P で割った余りの逆数を持たず、上の規則は適用できません。この場合、 hash(x) を定数 sys.hash_info.inf と定義します。

> * x = m / n が負の有理数なら、 hash(x) を -hash(-x) と定義します。その結果のハッシュが -1 なら、 -2 に置き換えます。

> * 特定の値 sys.hash_info.inf 、 -sys.hash_info.inf 、 sys.hash_info.nan は、正の無限大、負の無限大、nan を (それぞれ) 表すのに使われます。(すべてのハッシュ可能な nan は同じハッシュ値を持ちます。)

> * 複素 (complex) 数 z に対して、実部と虚部のハッシュ値は、 hash(z.real) + sys.hash_info.imag * hash(z.imag) の 2**sys.hash_info.width を法とする還元を計算することにより組み合わせられ、よってこれは range(-2**(sys.hash_info.width - 1), 2**(sys.hash_info.width - 1)) に収まります。再び、結果が -1 なら、 -2 で置き換えられます。

### コード例

> 上述の規則をわかりやすくするため、有理数 float や、 complex のハッシュを計算する組み込みのハッシュと等価な Python コードの例を挙げます:

```python
import sys, math

def hash_fraction(m, n):
    """Compute the hash of a rational number m / n.

    Assumes m and n are integers, with n positive.
    Equivalent to hash(fractions.Fraction(m, n)).

    """
    P = sys.hash_info.modulus
    # Remove common factors of P.  (Unnecessary if m and n already coprime.)
    while m % P == n % P == 0:
        m, n = m // P, n // P

    if n % P == 0:
        hash_value = sys.hash_info.inf
    else:
        # Fermat's Little Theorem: pow(n, P-1, P) is 1, so
        # pow(n, P-2, P) gives the inverse of n modulo P.
        hash_value = (abs(m) % P) * pow(n, P - 2, P) % P
    if m < 0:
        hash_value = -hash_value
    if hash_value == -1:
        hash_value = -2
    return hash_value

def hash_float(x):
    """Compute the hash of a float x."""

    if math.isnan(x):
        return sys.hash_info.nan
    elif math.isinf(x):
        return sys.hash_info.inf if x > 0 else -sys.hash_info.inf
    else:
        return hash_fraction(*x.as_integer_ratio())

def hash_complex(z):
    """Compute the hash of a complex number z."""

    hash_value = hash_float(z.real) + sys.hash_info.imag * hash_float(z.imag)
    # do a signed reduction modulo 2**sys.hash_info.width
    M = 2**(sys.hash_info.width - 1)
    hash_value = (hash_value & (M - 1)) - (hash_value & M)
    if hash_value == -1:
        hash_value = -2
    return hash_value

print(hash_fraction(3,2))
print(hash_float(3.2))
print(hash_complex(3.2j))
```
```sh
$ python 0.py 
1073741825
1717987740
1680595924
```

