# coding: shift_jis 
text = u"こんにちは世界"
ords = [12371, 12435, 12395, 12385, 12399, 19990, 30028]
assert [ord(c) for c in text] == ords
print(u"All OK with shift_jis")
encoding = "shift_jis"