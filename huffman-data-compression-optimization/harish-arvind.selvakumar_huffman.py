__license__ = 'Junior (c) Student'
__docformat__ = 'reStructuredText'
__revision__ = '$Id: huffman.py 2022-04-17'

"""
Huffman Project
2022
@author: harish-arvind.selvakumar
"""
import bintree
# from algopy import bintree
# from algopy import heap

###############################################################################
# Do not change anything above this line, except your login!
# Do not add any import

###############################################################################
# COMPRESSION


def buildfrequencylist(dataIN):
    """
    Builds a tuple list of the character frequencies in the input.
    """
    result = []
    i = 0
    l = len(dataIN)
    L = []
    available = False
    while i < l:
        available = False
        for j in range(len(result)):
            if not available:
                if result[j][1] == dataIN[i]:
                    available = True
        if not available:
            num = 0
            for k in range(i, l):
                if dataIN[k] == dataIN[i]:
                    num += 1
                else:
                    L.append(dataIN[k])
            result.append((num, dataIN[i]))
        i += 1

    return result


def buildHuffmantree(inputList):
    """
    Processes the frequency list into a Huffman tree according to the algorithm.   

    """
    temp = []
    for i in range(len(inputList)):
        temp.append(inputList[i])
    for i in range(len(temp)):
        temp[i] = temp[i][0], bintree.BinTree(temp[i][1], None, None)
    while len(temp) > 1:
        n = len(temp)
        swapped = True
        start = 0
        end = n-1
        while swapped:
            swapped = False
            for i in range(start, end):
                if (temp[i][0] < temp[i+1][0]):
                    temp[i], temp[i+1] = temp[i+1], temp[i]
                    swapped = True
            if swapped:
                swapped = False
                end = end-1
                for i in range(end-1, start-1, -1):
                    if (temp[i][0] < temp[i+1][0]):
                        temp[i], temp[i+1] = temp[i+1], temp[i]
                        swapped = True
                start = start+1
        r, rT = temp.pop()
        l, lT = temp.pop()
        temp.append((r+l, bintree.BinTree(None, lT, rT)))
    (a, b) = temp[0]
    return b


def encodedata(huffmanTree, dataIN):
    """
    Encodes the input string to its binary string representation.      
    """
    result = ""
    l = []
    __cftuple(huffmanTree, result, l)
    maxi = len(l)
    for i in dataIN:
        for n in range(maxi):
            if i == l[n][0]:
                result += l[n][1]
    return result


def __cftuple(huffman, letter, List):
    '''
    char,new huffman code
    l=[tuple (char,01000....)]
    changes the L value 
    '''
    if huffman != None:
        __cftuple(huffman.left, letter + '0', List)
        if huffman.left == None and huffman.right == None:
            List.append((huffman.key, letter))
        __cftuple(huffman.right,  letter + '1', List)


def encodetree(huffmanTree):
    """
    Encodes a huffman tree to its binary representation using a preOrder traversal:
        * each leaf key is encoded into its binary representation on 8 bits preceded by '1'
        * each time we go left we add a '0' to the result
    """
    string = ""
    if huffmanTree.key == None:
        return '0' + encodetree(huffmanTree.left) + encodetree(huffmanTree.right)
    else:
        unicode = ord(huffmanTree.key)
        o = '1'
        while unicode > 0:
            if unicode % 2 == 0:
                string = '0' + string
            else:
                string = '1' + string
            unicode //= 2
        for i in range(len(string), 8):
            string = '0' + string
        return o + string


def tobinary(dataIN):
    """
    Compresses a string containing binary code to its real binary value.
    """
    lth = len(dataIN)
    base = 0
    ok = True
    stri = ""
    while ok and base >= 0:
        while base < lth:
            if base+lth < 0:
                L = []
                temp = base
                while base != 0:
                    L.append(dataIN[0])
                    base -= 1
                base = temp
            elif base < lth-7:
                res = 1
                n = res-1
                i = base + 7
                while i >= base:
                    n += int(dataIN[i]) * res
                    res *= 2
                    i -= 1
            else:
                res = 1
                n = res-1
                i = lth - 1
                while i >= base:
                    n += int(dataIN[i])*res
                    i -= 1
                    res *= 2
            stri = stri + chr(n)
            base += 8
        ok = base < lth

    return (stri, base - lth)


def compress(dataIn):
    """
    The main function that makes the whole compression process.
    """

    freq = buildfrequencylist(dataIn)
    A = buildHuffmantree(freq)
    datta = encodedata(A, dataIn)
    Tree = encodetree(A)
    return (tobinary(datta), tobinary(Tree))


################################################################################
# DECOMPRESSION

def decodedata(huffmanTree, dataIN):
    """
    Decode a string using the corresponding huffman tree into something more readable.
    """
    L = []
    __cftuple(huffmanTree, " ", L)
    string = " "
    result = ""
    for numb in dataIN:
        string += numb
        for letter in L:
            if string == letter[1]:
                result += letter[0]
                string = " "
    return result


def __Decodetree(dataIN, i=0):
    """
    recursive version of decode tree with the same rules taking two parameters
    """
    B = bintree.BinTree(None, None, None)
    if dataIN[i] == '0':
        (B.left, i) = __Decodetree(dataIN, i + 1)
        (B.right, i) = __Decodetree(dataIN, i + 1)
        return (B, i)
    else:
        x = i+1
        result = ""
        k = 0
        while k < 8:
            result += dataIN[x + k]
            k += 1
        j = int(result, 2)
        B.key = chr(j)
        return (B, i + 8)


def decodetree(dataIN):
    """
    Decodes a huffman tree from its binary representation:
        * a '0' means we add a new internal node and go to its left node
        * a '1' means the next 8 values are the encoded character of the current leaf         
    """
    return __Decodetree(dataIN)[0]


def __toBinary(n):
    L = [0]
    i = 0
    while i < 7:
        L.append(0)
        i += 1
    res = ""
    while (n > 0 and i >= 0):
        L[i] = n % 2
        n = n//2
        i -= 1
    for i in L:
        res += str(i)
    return res


def frombinary(dataIN, align):
    """
    Retrieve a string containing binary code from its real binary value (inverse of :func:`toBinary`).
    """

    if (len(dataIN) != 0):
        res = ""
        for i in range(len(dataIN)-1):
            res += __toBinary(ord(dataIN[i]))
        last = __toBinary(ord(dataIN[len(dataIN)-1]))
        for j in range(align, 8):
            res += last[j]
    return res


data = "um ah human huffman is fun i am a fan ha ha ha ha ha ha"
freqList = buildfrequencylist(data)
HT = buildHuffmantree(freqList)

encTree = encodetree(HT)
print(decodedata(HT, encodedata(HT, data)))
# print(decodetree(encTree))
data = "um ah human huffman is fun i am a fan ha ha ha ha ha ha"

encData = encodedata(HT, data)
# print(encData)
print(encodetree(decodetree(encTree)) == encTree)
print(tobinary(encData) == ('1>æ\x1c¹î\x87"\x92ÓÈ²&×.Ý»ví\r', 4))
(dataComp, align) = tobinary(encData)
print((len(data), len(dataComp)) == (55, 20))
(treeComp, alignTree) = tobinary(
    "00010110110100101110011101101001101110101101100001010010000000101101110101100110101101000")


print((treeComp, alignTree) == ('\x16ÒçiºØR\x02Ýf´\x00', 7))
encTree = "00010110110100101110011101101001101110101101100001010010000000101101110101100110101101000"
print(frombinary(dataComp, align) == encData)
print(frombinary(dataComp, align) == encData)

print(frombinary(treeComp, alignTree) == encTree)
# print(tobinary("00111001110101111011001110010100011011001100100010100101000110100010111001000110001101001110110011101110010101000110111011101110111011101110111011101110111011101"))
#


def decompress(data, dataAlign, tree, treeAlign):
    """
    The whole decompression process.
    """
    huftree = frombinary(tree, treeAlign)
    datares = frombinary(data, dataAlign)
    resultree = decodetree(huftree)
    return decodedata(resultree, datares)


print("all good")
((dataComp, align), (treeComp, alignTree)) = compress(data)
print(decompress(dataComp, align, treeComp, alignTree) ==
      'um ah human huffman is fun i am a fan ha ha ha ha ha ha')
print(compress('bbaabtttaabtctce'))
