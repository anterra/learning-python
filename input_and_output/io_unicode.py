#encoding=utf-8
#(putting the above comment at the beginning of program is necessary when using unicode literals (u"text"))
#(and Python itself must be told we are using utf-8 via the encoding argument)

import io

f = io.open("abc.txt", "wt", encoding="utf-8")
f.write(u"Imagine non-English language here")
f.close()

text = io.open("abc.txt", encoding="utf-8").read()
print(text)
