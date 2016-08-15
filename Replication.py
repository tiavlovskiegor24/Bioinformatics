# ApproximatePatternCount
# Input:  Strings Pattern and Text, and an integer d
# Output: The number of times Pattern appears in Text with at most d mismatches
def ApproximatePatternCount(Pattern, Text, d):
    count = 0 # initialize count variable
    for i in range(len(Text) - len(Pattern) + 1):
        if HammingDistance(Pattern,Text[i:i + len(Pattern)]) <= d:
            count = count + 1
    return count

# ApproximatePatternMatching
# Input:  Strings Pattern and Text along with an integer d
# Output: A list containing all starting positions where Pattern appears
# as a substring of Text with at most d mismatches
def ApproximatePatternMatching(Pattern, Text, d):
    positions = [] # initializing list of positions
    for i in range(len(Text) - len(Pattern) + 1):
        if HammingDistance(Pattern, Text[i:i + len(Pattern)]) <= d:
            positions.append(i)
    return positions

# HammingDistance
# Input:  Two strings p and q
# Output: An integer value representing the Hamming Distance between p and q.
def HammingDistance(p, q):
    n = len(p)
    d = 0
    for i in range(n):
        if p[i] != q[i]:
            d += 1
    return d

# Input:  A DNA string Genome
# Output: A list containing all integers i minimizing Skew(Prefix_i(Text)) over all values of i (from 0 to |Genome|)
def MinimumSkew(Genome):
    positions = [] # output variable
    skew = Skew(Genome)
    m = max(skew.values()) #!!!!!!! change to min
    for i in range(len(skew)):
        if skew[i] == m:
            positions.append(i) 
    return positions

# Skew
# Input:  A String Genome
# Output: Skew(Genome)
def Skew(Genome):
    skew = {} #initializing the dictionary
    n = len(Genome)
    skew[0] = 0
    for i in range(n):
        if Genome[i] == "G":
            skew[i+1] = skew[i]+1
        elif Genome[i] == "C":
            skew[i+1] = skew[i]-1
        else:
            skew[i+1] = skew[i]
    return skew

# FasterSymbolArray
# Input:  Strings Genome and symbol
# Output: FasterSymbolArray(Genome, symbol)
def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    array[0] = PatternCount(symbol,Genome[0:n//2])
    for i in range(1,n):
        array[i] = array[i-1]
        if ExtendedGenome[i-1] == symbol:
            array[i] = array[i] - 1
        if ExtendedGenome[i+(n//2)-1] == symbol:
            array[i] = array[i] + 1            
    return array

# SymbolArray
# Input:  Strings Genome and symbol
# Output: SymbolArray(Genome, symbol)
def SymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        array[i] = PatternCount(symbol,ExtendedGenome[i:i+n//2])
    return array

# FrequentWords
# Input:  A string Text and an integer k
# Output: A list containing all most frequent k-mers in Text
def FrequentWords(Text, k):
    FrequentPatterns = []
    Count = CountDict(Text, k)
    m = max(Count.values())
    for i in Count:
        if Count[i] == m:
            FrequentPatterns.append(Text[i:i + k])
    FrequentPatternsNoDuplicates = remove_duplicates(FrequentPatterns)
    return FrequentPatternsNoDuplicates

# CountDict
# Input:  A string Text and an integer k
# Output: CountDict(Text, k)
def CountDict(Text, k):
    Count = {} # output variable
    for i in range(len(Text) - k + 1):
        Pattern = Text[i:i+k]
        Count[i] = PatternCount(Pattern, Text)
    return Count

# PatternCount
# Input:  Strings Pattern and Text
# Output: The number of times Pattern appears in Text
def PatternCount(Pattern, Text):
    count = 0 # output variable
    for i in range(len(Text) - len(Pattern) + 1):
        if Text[i:i + len(Pattern)] == Pattern:
            count = count + 1
    return count

# remove_duplicates
# Input: List of items
# Output List of items without duplicates
def remove_duplicates(x):
    out = []
    for i in x:
        if i not in out:
            out.append(i)
    return out

# ReverseComplement
# Input:  A DNA string Pattern
# Output: The reverse complement of Pattern
def ReverseComplement(Pattern):
    revComp = '' # output variable
    Comp = ''
    for Nucleotide in Pattern:
        Comp = Comp + complement(Nucleotide)
    revComp = reverse(Comp)
    return revComp

# reverse
# Input: A character text
# Output: A character reversed of text
def reverse(text):
    out = ''
    for c in text:
        out = c + out
    return out

# complement
# Input:  A character Nucleotide
# Output: The complement of Nucleotide
def complement(Nucleotide):
    comp = '' # output variable
    c = {"A":"T","T":"A","C":"G","G":"C"}
    comp = c[Nucleotide]
    return comp
  
# PatternMatching    
# Input:  Two strings, Pattern and Genome
# Output: A list containing all starting positions where Pattern appears as a substring of Genome
def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    for i in range(len(Genome) - len(Pattern) + 1):
        if Genome[i:i + len(Pattern)] == Pattern:
            positions.append(i)
    return positions    
    
    
    
Text = "ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC"
    
print MinimumSkew("CATTCCAGTACTTCGATGATGGCGTGAAGA")

print "Hello", HammingDistance("CTACAGCAATACGATCATATGCGGATCCGCAGTGGCCGGTAGACACACGT", "CTACCCCGCTGCTCAATGACCGGGACTAAAGAGGCGAAGATTATGGTGTG")

a = list(range(5))
b = a
a[2]=12

print a
print b

### DO NOT MODIFY THE CODE BELOW THIS LINE ###
#import sys
#lines = sys.stdin.read().splitlines()
#print(' '.join(FrequentWords(lines[0],int(lines[1]))))    
            