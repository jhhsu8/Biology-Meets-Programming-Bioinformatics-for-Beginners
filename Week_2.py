#Exercise 1
# Input:  Strings Genome and symbol
# Output: SymbolArray(Genome, symbol)
def SymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        array[i] = PatternCount(ExtendedGenome[i:i+(n//2)], symbol)
    return array

# Reproduce the PatternCount function here.
def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count

#Exercise 2
# Input:  Strings Genome and symbol
# Output: FasterSymbolArray(Genome, symbol)
def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]

    # look at the first half of Genome to compute first array value
    array[0] = PatternCount(Genome[0:n//2], symbol)

    for i in range(1, n):
        # start by setting the current array value equal to the previous array value
        array[i] = array[i-1]

        # the current array value can differ from the previous array value by at most 1
        if ExtendedGenome[i-1] == symbol:
            array[i] = array[i]-1
        if ExtendedGenome[i+(n//2)-1] == symbol:
            array[i] = array[i]+1
    return array

# Input:  Strings Text and Pattern
# Output: The number of times Pattern appears in Text
# HINT:   This code should be identical to when you last implemented PatternCount
def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count

### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
lines = sys.stdin.read().splitlines()
print(FasterSymbolArray(lines[0],lines[1]))

#Exercise 3
# Input:  A String Genome
# Output: The skew array of Genome as a list.
def SkewArray(Genome):
    # your code here
    array = {}
    array[0] = 0
    for i in range(len(Genome)):
        if Genome[i] == 'A' or 'T':
            array[i+1] = array[i]
        if Genome[i] == 'G':
            array[i+1] = array[i] + 1
        if Genome[i] == 'C':
            array[i+1] = array[i] - 1
    return array.values()

#Exercise 4
# Input:  A DNA string Genome
# Output: A list containing all integers i minimizing Skew(Prefix_i(Text)) over all values of i (from 0 to |Genome|)
def MinimumSkew(Genome):
    positions = [] # output variable
    # generate an empty list positions
    # set a variable equal to SkewArray(Genome)
    skewarray = SkewArray(Genome)
    min_value = min(skewarray)
    array = list(skewarray)
    for i in range(len(skewarray)):
        if array[i] == min_value:
            positions.append(i)
    return positions

# Input:  A String Genome
# Output: SkewArray(Genome)
# HINT:   This code should be taken from the last Code Challenge.
def SkewArray(Genome):
    # your code here
    array = {}
    array[0] = 0
    for i in range(len(Genome)):
        if Genome[i] == 'A' or 'T':
            array[i+1] = array[i]
        if Genome[i] == 'G':
            array[i+1] = array[i] + 1
        if Genome[i] == 'C':
            array[i+1] = array[i] - 1
    return array.values()

#Exercise 5
# Input:  Two strings p and q
# Output: An integer value representing the Hamming Distance between p and q.
def HammingDistance(p, q):
    count = 0
    for i in range(len(p)):
        for j in range(len(q)):
            if i==j:
                if p[i] != q[j]:
                    count = count + 1
    return count

#Exercise 6
# Input:  Strings Pattern and Text along with an integer d
# Output: A list containing all starting positions where Pattern appears
# as a substring of Text with at most d mismatches

def ApproximatePatternMatching(Text, Pattern, d):
    positions = [] # initializing list of positions
    n = len(Text)
    k = len(Pattern)
    for i in range(n-k+1):
        Pattern1 = Text[i:i+k]
        if HammingDistance(Pattern, Pattern1) <= d:
            positions.append(i)
    return positions

# Insert your Hamming distance function on the following line.
def HammingDistance(p, q):
    count = 0
    for i in range(len(p)):
        for j in range(len(q)):
            if i==j:
                if p[i] != q[j]:
                    count = count + 1
    return count

#Exercise 7
# Input:  Strings Pattern and Text, and an integer d
# Output: The number of times Pattern appears in Text with at most d mismatches
def ApproximatePatternCount(Pattern, Text, d):
    count = 0 # initialize count variable
    n = len(Text)
    k = len(Pattern)
    for i in range(n-k+1):
        Pattern1 = Text[i:i+k]
        if HammingDistance(Pattern, Pattern1) <= d:
            count = count + 1
    return count

# Insert your HammingDistance function on the following line.
def HammingDistance(p, q):
    count = 0
    for i in range(len(p)):
        for j in range(len(q)):
            if i==j:
                if p[i] != q[j]:
                    count = count + 1
    return count

### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
lines = sys.stdin.read().splitlines()
print(ApproximatePatternCount(lines[0],lines[1],int(lines[2])))
