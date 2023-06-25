def process_user_global():
    user_globals = [*filter(lambda x: not x[0].startswith('__'), globals().items())]

    for name, value in user_globals:
        if name != "s" and name.endswith("s") and len(name) > 1:
            globals()[name] = None

    for name, value in user_globals:
        if name.endswith("s") and len(name) > 1:
            globals()[name[:-1]] = value

    new_user_globals = [*filter(lambda x: not x[0].startswith('__') and not x[0] == 'process_user_global', globals().items())]

    for name, value in new_user_globals:
        print(f'{name} = {value}')


a = 123
pas = 245
s = "hello world"
xyzs = [1, 2, 3]
absd = 'abs'

process_user_global()
