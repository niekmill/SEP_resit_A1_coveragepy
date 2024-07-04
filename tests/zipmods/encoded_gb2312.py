# coding: gb2312 
text = u"你好，世界"
ords = [20320, 22909, 65292, 19990, 30028]
assert [ord(c) for c in text] == ords
print(u"All OK with gb2312")
encoding = "gb2312"