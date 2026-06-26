def NULL_not_found(object):

    if object is None:
        print(f"Nothing: None <class '{type(object).__name__}'>")
        return None
    elif object != object:
        print(f"Cheese: nan <class '{type(object).__name__}'>")
        return None
    elif object == 0 and type(object) is int:
        print(f"Zero: 0 <class '{type(object).__name__}'>")
        return None
    elif object == '':
        print(f"Empty: <class '{type(object).__name__}'>")
        return None
    elif object is False:
        print(f"Fake: False <class '{type(object).__name__}'>")
        return None
    else:
        print("Type not Found")
        return 1
