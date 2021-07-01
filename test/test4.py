"""4. 使用键盘输入一个Unicode字符，显示出这个字符对应的Unicode编码值。"""
unicode = input("输入一个Unicode字符:")
print("这个字符对应的Unicode编码值", unicode.encode("utf-16"))
