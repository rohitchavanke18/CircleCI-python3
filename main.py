def to_upper(name):
    return name.upper()

def say_hello(name):
    return print(f'Hello,{name}')

if __name__=='__main__':
    name='Train With Rohit'
    say_hello(name)
    up=to_upper(name)
    print(up)