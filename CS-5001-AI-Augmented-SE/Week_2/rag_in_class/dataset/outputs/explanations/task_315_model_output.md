# Model output for task_315

## Model
- devstral-small-2:24b-cloud

## Original Code:

def find_Max_Len_Even(str): 
    n = len(str) 
    i = 0
    currlen = 0
    maxlen = 0
    st = -1
    while (i < n): 
        if (str[i] == ' '): 
            if (currlen % 2 == 0): 
                if (maxlen < currlen): 
                    maxlen = currlen 
                    st = i - currlen 
            currlen = 0 
        else : 
            currlen += 1
        i += 1
    if (currlen % 2 == 0): 
        if (maxlen < currlen): 
            maxlen = currlen 
            st = i - currlen 
    if (st == -1): 
        return "-1" 
    return str[st: st + maxlen] 

## Refactored Code:

```python
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
```

- Maintained the original function name and interface contract
- Improved variable naming for clarity (e.g., `st` to `start_index`)
- Added type hints for better code documentation
- Preserved the exact logic and behavior of the original function
- Ensured the function returns "-1" when no valid substring is found
- Added a docstring to explain the function's purpose and behavior
- Kept the in-place processing of the input string
- Maintained the original edge case handling (empty string or no even-length substrings)
