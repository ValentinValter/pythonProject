def lst_to_flat(S):
    if S == []:
        return S
    if isinstance(S[0], list):
        return lst_to_flat(S[0]) + lst_to_flat(S[1:])
    return S[:1] + lst_to_flat(S[1:])
