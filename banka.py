def check_string_brackets(input_pp):
    ll =input_pp.count(')')
    uu = input_pp.count('(')
    if ll == uu :
        print('да')
    else:
        print('нет')
kk =input()
check_string_brackets(kk)