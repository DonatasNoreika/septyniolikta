def kmi(svoris, ugis):
    if svoris < 30 and ugis > 1.30:
        raise ValueError
    if svoris > 230 and ugis < 1.50:
        raise ValueError
    if svoris > 70 and ugis < 0.50:
        raise ValueError
    if svoris < 90 and ugis > 3.30:
        raise ValueError
    return svoris / ugis ** 2
