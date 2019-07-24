def permutations(content, r=None):
    rval = r or len(content)
    cresult = permutations_wh(content, r=rval)
    return [v for v in sorted(cresult)]


def permutations_wh(content, r):
    if r == 0:
        return []
    if r == 1:
        return [ch for ch in content]
    result = []
    for ix in range(len(content)):
        hchar = content[ix]
        ocontent = content[:ix] + content[ix + 1 :]
        for nseq in permutations_wh(ocontent, r - 1):
            result.append(hchar + nseq)
    return result


def combinations(content, r=None):
    rval = r or len(content)
    cresult = combinations_wh(content, r=rval)
    return [v for v in sorted(cresult)]


def combinations_wh(content, r):
    if r == 0:
        return []
    if r == 1:
        return [ch for ch in content]
    result = []
    for ix in range(len(content)):
        hchar = content[ix]
        tcontent = content[ix + 1 :]
        for tseq in combinations_wh(tcontent, r - 1):
            result.append(hchar + tseq)
    return result
