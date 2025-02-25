def to_boolean(value):
    if value.lower() in ['true', '1']:
        return True
    elif value.lower() in ['false', '0']:
        return False
    try:
        return int(value) != 0
    except ValueError:
        return bool(value)

def check_all_true(tpl):
    return all(tpl)

user_input = tuple(map(to_boolean, input("Введите элементы кортежа через пробел: ").split()))
print(check_all_true(user_input))

