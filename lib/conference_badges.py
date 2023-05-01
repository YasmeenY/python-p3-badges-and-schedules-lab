def badge_maker(name):
    return (f'Hello, my name is {name}.')

def batch_badge_creator(names):
    # name_list = list()
    # for name in names:
    #     name_list.append(f'Hello, my name is {name}.')
    # return name_list
    return ([f"Hello, my name is {name}." for name in names])


def assign_rooms(names):
    count = 1
    assign_list = list()
    for name in names:
        assign_list.append(f"Hello, {name}! You'll be assigned to room {count}!")
        count +=1
    return assign_list

def printer(names):
    count = 0
    for name in names:
        print(f"Hello, my name is {name}.")
    for name in names:
        count +=1
        print(f"Hello, {name}! You'll be assigned to room {count}!")
