import hashlib


def recur_sum(value):
    """
    ATTENTION !!!
    This is recursive functions and it must be used sparingly and skillfully.
    An ill-considered use of recursion can lead to a combinatorial explosion in the number
    of calls and stack size needed to perform recursion.

    We are accepting the object which can contain a variety of things:
        - arrays [1,2,3,4]
        - objects {"a":1, "b":2, "c":3}
        - numbers
        - strings
    This function find all of the numbers throughout the given body and add them together.

    For example:
    - [1,2,3,4] and {"a":6,"b":4} both have a sum of 10.
    - [[[2]]] and {"a":{"b":4},"c":-2} both have a sum of 2.
    - {"a":[-1,1,"dark"]} and [-1,{"a":1, "b":"light"}] both have a sum of 0.
    - [] and {} both have a sum of 0.

    :param value:
    :return:
    """

    if isinstance(value, str):
        return 0
    elif isinstance(value, (int, float)):
        return value
    if isinstance(value, dict):
        value = list(value.values())
    if isinstance(value, list):
        result = 0
        for item in value:
            result += recur_sum(item)
        return result


def get_sha256_hexdigest(value):
    """
    Here we are using SHA256 algorithm to hash given value and return it as a hex digest.
    :param value: number
    :return: sha256 hexdigest
    """
    hash_sha256 = hashlib.sha256()
    hash_sha256.update(bytes(value))
    return hash_sha256.hexdigest()
