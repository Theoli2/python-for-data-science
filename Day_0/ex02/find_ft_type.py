def all_thing_is_obj(object: any) -> int:

    type_labels = {
        list: "List",
        tuple: "Tuple",
        dict: "Dict",
        set: "Set",
    }

    if isinstance(object, str):
        print(f"{object} is in the kitchen : <class 'str'>")
    else:
        label = type_labels.get(type(object), "type not found")

        if label == "type not found":
            print(label)
        else:
            print(f"{label} : <class '{type(object).__name__}'>")
    return 42
