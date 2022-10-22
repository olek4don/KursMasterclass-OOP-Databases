# def build_tuple(*args):
#     return args

# message_tuple = build_tuple("hello", "planet", "earth", "take", "me", "to", "your", "leader")
# print(type(message_tuple))
# print(message_tuple)

# number_tuple = build_tuple(1, 2, 3, 4, 5, 6)
# print(type(number_tuple))
# print(number_tuple)

# def print_backwards(*args, end=' ', **kwargs):
# def print_backwards(*args, **kwargs):
#     print(kwargs)
#     kwargs.pop('end', None)
#     for word in args[::-1]:
#         print(word[::-1], end=' ', **kwargs)


def print_backwards(*args, **kwargs):
    end_character = kwargs.pop('end', '\n')
    sep_character = kwargs.pop('sep', ' ')
    for word in args[:0:-1]:    # change the range
        print(word[::-1], end=sep_character, **kwargs)
    print(args[0][::-1], end=end_character, **kwargs)       # and print the first word separately
    # print(end=end_character)  # which means we don't need this line
        
with open("backwards.txt", "w") as backwards:
    print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='\n')
    print("Another string")
    
print()
print("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='', sep='\n')
print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='', sep='\n**\n')
print("=" * 10)