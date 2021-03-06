def get_phone_key(n: int, p: int):
    answers = {
        2: {1: "a", 2: "b", 3: "c"},
        3: {1: "d", 2: "e", 3: "f"},
        4: {1: "g", 2: "h", 3: "i"},
        5: {1: "j", 2: "k", 3: "l"},
        6: {1: "m", 2: "n", 3: "o"},
        7: {1: "p", 2: "q", 3: "r"},
        8: {1: "s", 2: "t", 3: "u"},
        9: {1: "v", 2: "x", 3: "y"},
    }
    return answers[n][p]


def get_phone_words_rec(phone: str, n: int = 0):
    if not phone:
        raise ValueError("invalid phone number")
    if n > len(phone) - 1:
        return []
    digit = int(phone[n])
    if n == len(phone) - 1:
        return [get_phone_key(digit, p) for p in range(1, 4)]
    result = []
    for option in get_phone_words_rec(phone, n + 1):
        for p in range(1, 4):
            result.append(get_phone_key(digit, p) + option)
    return result


def get_phone_words_stk(phone: str, n: int = 0):
    if not phone:
        raise ValueError("invalid phone number")
    digit = int(phone[n])
    prv_st = [get_phone_key(digit, p) for p in range(1, 4)]
    cur_st = []
    for i in range(n + 1, len(phone)):
        digit = int(phone[i])
        while len(prv_st) > 0:
            prv_seq = prv_st.pop()
            for p in range(1, 4):
                cur_seq = get_phone_key(digit, p) + prv_seq
                cur_st.append(cur_seq)
        cur_st, prv_st = prv_st, cur_st
    return prv_st
