#!python3.6
#coding:utf-8
# compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)
import sys
#exec(compile('print("AAA")', 'compile_source_0.py', 'single'), globals(), locals())
exec(compile('print("AAA")', sys.argv[0], 'single'), globals(), locals()) # 単一の対話分
exec(compile('print("BBB")', sys.argv[0], 'eval'), globals(), locals()) # 単一の式
exec(compile('print("CCC")', sys.argv[0], 'exec'), globals(), locals()) # 一連の文
#exec(compile(None, 'compile_source_0.py', 'single'), globals(), locals())

