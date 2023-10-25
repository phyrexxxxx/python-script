
"""
全形符號          半形符號
0x3000           0x0020
0xFF01~0xFF5E    0x0021~0x007E
"""

def fullwidth_to_halfwidth(s):
    """
    將全形符號轉換成半形符號
    """
    n = []
    for c in s:
        num = ord(c)

        if num == 0x3000:              # fullwidth whitespace "　"
            num = 0x0020
        elif 0xFF01 <= num <= 0xFF5E:  # fullwidth - 0xFEE0 = halfwidth
            num -= 0xFEE0
        
        n.append(chr(num))
        
    return ''.join(n)


def halfwidth_to_fullwidth(s):
    """
    將半形符號轉換成全形符號
    """
    n = []
    for c in s:
        num = ord(c)

        if num == 0x0020:              # halfwidth whitespace " "
            num = 0x3000
        elif 0x0021 <= num <= 0x007E:  # halfwidth + 0xFEE0 = fullwidth
            num += 0xFEE0
        
        n.append(chr(num))

    return ''.join(n)
