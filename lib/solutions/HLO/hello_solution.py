# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name):
    return "Hello, {}!".format(str(friend_name)) 

print(hello("World"))