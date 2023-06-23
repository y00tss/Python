s = input("Enter a string: ")

dstack = []
flag = True
for i in s:
    if i in '([{':
        dstack.append(i)
    elif i in ")]}":
        if not dstack:
            flag = False
            break
        result = dstack.pop()
        if result == '(' and i == ')':
            continue
        elif result == '[' and i == ']':
            continue
        elif result == '{' and i == '}':
            continue
        else:
            flag = False

if flag:
    print("YES")
else:
    print("NO")

