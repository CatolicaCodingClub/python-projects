def sencode(alphabet, inp, numb):
    lengthOfAlpha = len(alphabet)
    letterat = alphabet.index(inp,0,lengthOfAlpha)
    incrementOf = numb
    indw = (lengthOfAlpha-1) - (letterat+incrementOf)
    if indw < 0:
        return (alphabet[abs(indw+1)])
    else:
        return (alphabet[letterat+incrementOf])
