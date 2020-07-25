def remove_outer_layer(string):
    stack = []
    return_string = ''
    x = ''
    for i in string:
        if i == '(':
            if stack:
                x += i
            stack.append(i)
        elif i == ')':
            if not stack:
                pass
            else:
                l = len(stack)
                stack.pop()
                if l == 1:
                    return_string += x
                    x = ''
                else:
                    x += i
    return return_string

print(remove_outer_layer('(())()'))
print(remove_outer_layer('(()())'))
