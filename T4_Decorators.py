


def split_dec(func):
    def wrapper():
        return func().split(" ")
    return wrapper

def upper_dec(func):
    def wrapper():
        return [word.upper() for word in func()]
    return wrapper


def filter_dec(func):
    def wrapper():
        return [word for word in func() if len(word)>4]
    return wrapper

@filter_dec
@upper_dec
@split_dec
def get_data():
    data='This is An exAmPlE StRinG' 
    return data

print(get_data())