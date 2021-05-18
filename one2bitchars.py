def isOneBitCharacter(self, bits: List[int]) -> bool:
    i = 0
    sk = 0
    while i in range(len(bits)):
        if bits[i] == 1:
            sk = 2
            i +=2
        else:
            sk = 1
            i +=1
    if sk == 1 and bits[i-1] == 0:
        return True
    return False
