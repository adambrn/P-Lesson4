def process_arguments(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if not hash(key):
            result[value] = key
        else:
            result[str(value)] = key
    return result

arguments = process_arguments(a=1, b=2, c='hello', d=[1, 2, 3])
print(arguments)
