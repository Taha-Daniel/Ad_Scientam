

def tuplist_to_dict(tuplist):
    """
    Transform a tuple list [(str,int)] in dict{str:int} with summing between tuples having the same key
    :param tuplist: tuple list [(str,int)]
    :return: dict: {str:int}
    """
    dict = {}
    for x, y in tuplist:
        if x not in dict.keys():
            dict[x] = int(y or 1)
        else:
            dict[x] += int(y or 1)
    return dict


def dict_fusion(dict1, dict2, index=1):
    """
    Fusion between two dictionary which can have same key (if same key we sum the value together)
    """
    dict = {}
    keys = set(dict1) | set(dict2)
    for key in keys:
        dict[key] = ((dict1.get(key, 0) or 0) + (dict2.get(key, 0) or 0)) * index
    return dict