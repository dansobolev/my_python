# Упражнение 4.2

s = 'У лукоморья 123 дуб зеленый 456'

# 1)
print(s.find('я'))

# 2)
print(s.count('у'))

# 3)
if s.isalpha():
    print("TRUE")
else:
    print(s.upper())

# 4)
if len(s) > 4:
    print(s.lower())

# 5)
print("О" + s[1:])