#Exercise 1
# First, create a string variable called ori that is equal to the Vibrio cholerae ori. Don't forget to enclose your string in quotes!
ori = "ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC"

# Then, print the length of ori
print (len(ori))

#Exercise 2
#Implement PatternCount
def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count 

PatternCount("GCGCG", "GCG")

#Exercise 3
# Copy your PatternCount function from the previous step below this line
def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text) - len(Pattern) + 1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count + 1
    return count
            
# Now, set Text equal to the ori of Vibrio cholerae and Pattern equal to "TGATCA"
Text = "ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC"
Pattern = "TGATCA"

# Finally, print the result of calling PatternCount on Text and Pattern.
# Don't forget to use the notation print() with parentheses included!
print(PatternCount(Text, Pattern))

# Insert your completed FrequencyMap() function here.
def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range (n - k + 1):
        Pattern = Text[i:i+k]
        freq[Pattern] = 0
        for i in range (n - k + 1):
            if Text[i:i+k] == Pattern:
                freq[Pattern] = freq[Pattern] + 1
    return freq

#Exercise 4
# Input:  A string Text and an integer k
# Output: A list containing all most frequent k-mers in Text
def FrequentWords(Text, k):
    words = []
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    for key, value in freq.items():
        if value == m:
            words.append(key)# add each key to words whose corresponding frequency value is equal to m
    return words

# Exercise 5
# Copy your FrequencyMap() function here.
def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range (n - k + 1):
        Pattern = Text[i:i+k]
        freq[Pattern] = 0
        for i in range (n - k + 1):
            if Text[i:i+k] == Pattern:
                freq[Pattern] = freq[Pattern] + 1
    return freq 
    
#Exercise 6
def FrequentWords(Text, k):
    words = []
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    for key, value in freq.items():
        if value == m:
            words.append(key) # add each key to words whose corresponding frequency value is equal to m
    return words

def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range (n - k + 1):
        Pattern = Text[i:i+k]
        freq[Pattern] = 0
        for i in range (n - k + 1):
            if Text[i:i+k] == Pattern:
                freq[Pattern] = freq[Pattern] + 1
    return freq 

# Now set Text equal to the Vibrio cholerae oriC and k equal to 10
Text = "ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC"
k = 10

# Finally, print the result of calling FrequentWords on Text and k.
print(FrequentWords(Text,k))

#Exercise 7
# Input:  A string Pattern
# Output: The reverse of Pattern
def Reverse(Pattern):
    # your code here
    index = len(Pattern) - 1
    reversed_string = ''
    
    for i in Pattern:
        reversed_string = reversed_string + Pattern[index]
        index = index - 1
    return reversed_string

#Exercise 8
 Input:  A DNA string Pattern
# Output: The complementary string of Pattern (with every nucleotide replaced by its complement).
def Complement(Pattern):
    # your code here
    index = 0
    string = ''
    Pattern = Pattern.lower()
    for i in Pattern:
    
        if Pattern[index] == 'a':
            string = string + 'T'
        elif Pattern[index] == 'g':
            string = string + 'C'
        elif Pattern[index] == 'c':
            string = string + 'G'
        else:
            string = string + 'A'
        
        index = index + 1
    
    return string

# Input:  A DNA string Pattern
# Output: The reverse complement of Pattern
def ReverseComplement(Pattern):   
    # your code here
    return Reverse(Complement(Pattern))

# Copy your Reverse() function here.
def Reverse(Pattern):
    # your code here
    index = len(Pattern) - 1
    reversed_string = ''
    for i in Pattern:
        reversed_string = reversed_string + Pattern[index]
        index = index - 1
    return reversed_string

# Copy your Complement() function here.
def Complement(Pattern):
    # your code here
    index = 0
    string = ''
    Pattern = Pattern.lower()
    for i in Pattern:
        if Pattern[index] == 'a':
            string = string + 'T'
        elif Pattern[index] == 'g':
            string = string + 'C'
        elif Pattern[index] == 'c':
            string = string + 'G'
        else:
            string = string + 'A'
        index = index + 1
    return string

#Exercise 9
# fill in your PatternMatching() function along with any subroutines that you need.
def PatternMatching(Pattern, Genome):
    positions = []
    index = 0  
    for i in Genome:
        if Genome[index:len(Pattern)+index] == Pattern:
            positions.append(index)
        index = index + 1
    return positions

#Exercise 10
# Copy your PatternMatching function below this line.
def PatternMatching(Pattern, Genome):
    positions = []
    index = 0  
    for i in Genome:
        if Genome[index:len(Pattern)+index] == Pattern:
            positions.append(index)
        index = index + 1
    return positions
# The following lines will automatically read in the Vibrio cholerae genome for you and store it in a variable named v_cholerae
import sys                              # needed to read the genome
input = sys.stdin.read().splitlines()   #
v_cholerae = input[1]                   # store the genome as 'v_cholerae'


# Call PatternMatching with Pattern equal to "CTTGATCAT" and Genome equal to v_cholerae,
# and store the output as a variable called positions
Pattern = 'CTTGATCAT'
Genome = v_cholerae 
positions = PatternMatching(Pattern, Genome)
# print the positions variable
print(positions)

#Exercise 11
# Copy your PatternCount function below here
def PatternCount(Text, Pattern):
    Pattern = Pattern.lower()
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count 

# On the following line, create a variable called Text that is equal to the oriC region from T petrophila
Text = 'aactctatacctcctttttgtcgaatttgtgtgatttatagagaaaatcttattaactgaaactaaaatggtaggtttggtggtaggttttgtgtacattttgtagtatctgatttttaattacataccgtatattgtattaaattgacgaacaattgcatggaattgaatatatgcaaaacaaacctaccaccaaactctgtattgaccattttaggacaacttcagggtggtaggtttctgaagctctcatcaatagactattttagtctttacaaacaatattaccgttcagattcaagattctacaacgctgttttaatgggcgttgcagaaaacttaccacctaaaatccagtatccaagccgatttcagagaaacctaccacttacctaccacttacctaccacccgggtggtaagttgcagacattattaaaaacctcatcagaagcttgttcaaaaatttcaatactcgaaacctaccacctgcgtcccctattatttactactactaataatagcagtataattgatctga'

# On the following line, create a variable called count_1 that is equal to the number of times
# that "ATGATCAAG" occurs in Text.

Pattern1 = "ATGATCAAG"
count_1 = PatternCount(Text, Pattern1)

# On the following line, create a variable called count_2 that is equal to the number of times
# that "CTTGATCAT" occurs in Text. 
Pattern2 = "CTTGATCAT"
count_2 = PatternCount(Text, Pattern2)

# Finally, print the sum of count_1 and count_2
print(count_1 + count_2)
