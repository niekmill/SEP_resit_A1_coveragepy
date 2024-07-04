# coding: hebrew 
text = u"שלום, עולם"
ords = [1513, 1500, 1493, 1501, 44, 32, 1506, 1493, 1500, 1501]
assert [ord(c) for c in text] == ords
print(u"All OK with hebrew")
encoding = "hebrew"