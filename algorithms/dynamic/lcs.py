def lcs_rec(astr: str, bstr: str):
    return _lcs_wh(astr, len(astr) - 1, bstr, len(bstr) - 1)


def _lcs_wh(astr: str, aind: int, bstr: str, bind: int):
    if aind < 0 or bind < 0:
        return 0

    if astr[aind] == bstr[bind]:
        match = 1 + _lcs_wh(astr, aind - 1, bstr, bind - 1)
        return match

    alcs = _lcs_wh(astr, aind - 1, bstr, bind)
    blcs = _lcs_wh(astr, aind, bstr, bind - 1)
    return max(alcs, blcs)


# https://algorithms.tutorialhorizon.com//dynamic-programming-longest-common-subsequence/
def lcs_dp(astr: str, bstr: str):
    alen, blen = len(astr), len(bstr)
    matches = [[0] * (blen + 1) for _ in range(alen + 1)]
    for i in range(1, alen + 1):
        for j in range(1, blen + 1):
            if astr[i - 1] == bstr[j - 1]:
                matches[i][j] = 1 + matches[i - 1][j - 1]
            else:
                alcs = matches[i - 1][j]
                blcs = matches[i][j - 1]
                matches[i][j] = max(alcs, blcs)
    return matches[-1][-1]
