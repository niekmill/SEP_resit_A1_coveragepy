# coding: utf-8 
text = u"ⓗⓔⓛⓛⓞ, ⓦⓞⓡⓛⓓ"
ords = [9431, 9428, 9435, 9435, 9438, 44, 32, 9446, 9438, 9441, 9435, 9427] 
assert [ord(c) for c in text] == ords 
print(u"All OK with utf-8") 
encoding = "utf-8" 