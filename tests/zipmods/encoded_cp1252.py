# coding: cp1252 
text = u"“hi”"
ords = [8220, 104, 105, 8221]
assert [ord(c) for c in text] == ords
print(u"All OK with cp1252")
encoding = "cp1252"