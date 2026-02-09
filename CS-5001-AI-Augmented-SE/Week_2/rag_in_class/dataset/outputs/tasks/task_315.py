def find_Max_Len_Even(s: str) -> str:
    """
    Finds the longest substring with an even number of characters, separated by spaces.
    Returns the substring itself if found, otherwise returns "-1".
    """
    n = len(s)
    i = 0
    currlen = 0
    maxlen = 0
    start_index = -1

    while i < n:
        if s[i] == ' ':
            if currlen % 2 == 0:
                if maxlen < currlen:
                    maxlen = currlen
                    start_index = i - currlen
            currlen = 0
        else:
            currlen += 1
        i += 1

    if currlen % 2 == 0:
        if maxlen < currlen:
            maxlen = currlen
            start_index = i - currlen

    if start_index == -1:
        return "-1"
    return s[start_index: start_index + maxlen]
