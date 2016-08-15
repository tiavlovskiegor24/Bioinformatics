# import Python's 'random' module here
import random

# Input:  A string Text, a profile matrix Profile, and an integer k
# Output: ProfileGeneratedString(Text, profile, k)
def ProfileGeneratedString(Text, profile, k):
    # your code here
    probabilities = {}
    n = len(Text)
    for i in range(0,n-k+1):
        probabilities[Text[i:i+k]] = Pr(Text[i:i+k],profile)
    probabilities = Normalize(probabilities)
    return WeightedDie(probabilities)

# Input:  A dictionary Probabilities whose keys are k-mers and whose values are the probabilities of these kmers
# Output: A randomly chosen k-mer with respect to the values in Probabilities
def WeightedDie(Probabilities):
    kmer = '' # output variable
    # your code here
    number = random.uniform(0,1)
    cum_pr = 0
    for k_mer in Probabilities:
        cum_pr += Probabilities[k_mer]
        if cum_pr > number:
            return k_mer
        else:
            pass
    return kmer

# Input: A dictionary Probabilities, where keys are k-mers and values are the probabilities of these k-mers (which do not necessarily sum up to 1)
# Output: A normalized dictionary where the probability of each k-mer was divided by the sum of all k-mers' probabilities
def Normalize(Probabilities):
    # your code here
    pr_sum = sum(Probabilities.values())
    for k_mer in Probabilities:
        Probabilities[k_mer] = Probabilities[k_mer]/pr_sum
    return Probabilities


# Input:  Positive integers k and t, followed by a list of strings Dna
# Output: RandomizedMotifSearch(Dna, k, t)
def RandomizedMotifSearch(Dna, k, t):
    M = RandomMotifs(Dna, k, t)
    BestMotifs = M
    while True:
        Profile = ProfileWithPseudocounts(M)
        M = Motifs(Profile,Dna)
        if Score(M) < Score(BestMotifs):
            BestMotifs = M
        else:
            return BestMotifs


# Input:  A list of strings Dna, and integers k and t
# Output: RandomMotifs(Dna, k, t)

def RandomMotifs(Dna, k, t):
    # place your code here.
    random_motifs = []
    for Text in Dna:
        i = random.randint(0,len(Text)-k)
        random_motifs.append(Text[i:i+k])
    return random_motifs

# Motifs
# Input:  A profile matrix Profile and a list of strings Dna
# Output: Motifs(Profile, Dna)
def Motifs(Profile, Dna):
    # insert your code here
    k = len(Profile["A"])
    Motifs = []
    for Text in Dna:
        Motifs.append(ProfileMostProbablePattern(Text, k, Profile))
    return Motifs

# ProfileWithPseudocounts
# Input:  A set of kmers Motifs
# Output: ProfileWithPseudocounts(Motifs)
def ProfileWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {} # output variable
    count = CountWithPseudocounts(Motifs)
    for symbol in count:
        profile[symbol] = []
        for i in range(k):
            profile[symbol].append(count[symbol][i]*1.0/(t+4))
    return profile


# CountWithPseudocounts
# Input:  A set of kmers Motifs
# Output: CountWithPseudocounts(Motifs)
def CountWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    count = {} # initializing the count dictionary
    
    # initializing the symbol lists to 0s
    for symbol in "ATCG":
        count[symbol] = []
        for i in range(k):
            count[symbol].append(1)
    
    # counting the symbols in each column of Motifs
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count


# Count
# Input:  A set of kmers Motifs
# Output: Count(Motifs)
def Count(Motifs):
    count = {} # initializing the count dictionary
    
    # initializing the symbol lists to 0s
    k = len(Motifs[0])
    for symbol in "ATCG":
        count[symbol] = []
        for i in range(k):
            count[symbol].append(0)
    
    # counting the symbols in each column of Motifs
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count

# Profile    
# Input:  A list of kmers Motifs
# Output: the profile matrix of Motifs, as a dictionary of lists.
def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    count = Count(Motifs)
    for symbol in count:
        profile[symbol] = []
        for i in range(k):
            profile[symbol].append(count[symbol][i]*1.0/t)
    return profile
 
# Consensus    
# Input:  A set of kmers Motifs
# Output: A consensus string of Motifs.
def Consensus(Motifs):
    k = len(Motifs[0])
    print "Using Consensus without pseudocounts"
    count = Count(Motifs)
    #count = CountWithPseudocounts(Motifs)
    consensus = ""
    for i in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in count:
            if count[symbol][i] > m:
                m = count[symbol][i]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus

# Score
# Input:  A set of k-mers Motifs
# Output: The score of these k-mers.
def Score(Motifs):
    consensus = Consensus(Motifs)
    k = len(Motifs[0])
    score = 0
    for kmer in Motifs:
        for i in range(k):
            if kmer[i] != consensus[i]:
                score += 1
    return score
 
# Pr    
# Input:  String Text and profile matrix Profile
# Output: Pr(Text, Profile)
def Pr(Text, profile):
    p = 1.0
    k = len(Text)
    for i in range(k):
        p *= profile[Text[i]][i]
    return p
    

# Input:  String Text, an integer k, and profile matrix Profile
# Output: ProfileMostProbablePattern(Text, k, Profile)
def ProfileMostProbablePattern(Text, k, Profile):
    n = len(Text)
    mp = -1
    mpattern = ""
    for i in range(n-k+1):
        pattern = Text[i:i+k]
        p = Pr(pattern,Profile)
        if p > mp:
            mp = p
            mpattern = pattern
    return mpattern
    
    
# Input:  A list of kmers Dna, and integers k and t (where t is the number of kmers in Dna)
# Output: GreedyMotifSearch(Dna, k, t)
def GreedyMotifSearch(Dna, k, t):
    BestMotifs = []
    for i in range(0,t):
        BestMotifs.append(Dna[i][0:k])
    BestScore = Score(BestMotifs)
    n = len(Dna[0])
    for i in range(0,n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1,t):
            P = Profile(Motifs[0:j])
            Motifs.append(ProfileMostProbablePattern(Dna[j], k, P))
        score = Score(Motifs)
        if score < BestScore:
            BestMotifs = Motifs
            BestScore = score
    return BestMotifs    
    
# Input:  A list of kmers Dna, and integers k and t (where t is the number of kmers in Dna)
# Output: GreedyMotifSearch(Dna, k, t)
def GreedyMotifSearchWithPseudocounts(Dna, k, t):
    BestMotifs = []
    for i in range(0,t):
        BestMotifs.append(Dna[i][0:k])
    BestScore = Score(BestMotifs)
    n = len(Dna[0])
    for i in range(0,n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1,t):
            P = ProfileWithPseudocounts(Motifs[0:j])
            Motifs.append(ProfileMostProbablePattern(Dna[j], k, P))
        score = Score(Motifs)
        if score < BestScore:
            BestMotifs = Motifs
            BestScore = score
    return BestMotifs    
    

# Input:  Integers k, t, and N, followed by a collection of strings Dna
# Output: GibbsSampler(Dna, k, t, N)
def GibbsSampler(Dna, k, t, N):
    BestMotifs = [] # output variable
    # your code here
    M = RandomMotifs(Dna, k, t)
    BestMotifs = M
    BestScore = Score(BestMotifs)
    for i in range(0,N):
        j = random.randint(0,t-1)
        profile = ProfileWithPseudocounts(BestMotifs[0:j] + BestMotifs[j+1:t])
        motif = ProfileGeneratedString(Dna[j], profile, k)
        M = BestMotifs[0:j] + [motif] + BestMotifs[j+1:t]
        if Score(M) < BestScore:
            BestMotifs = M
            BestScore = Score(M)
    return BestMotifs

  

Dna = ["AAGCCAAA",
"AATCCTGG",
"GCTACTTG",
"ATGTTTTG"]

motifs = ["CCA",
"CCT",
"CTT",
"TTG"]

print Motifs(Profile(motifs),Dna)


''' simulations
  
Motifs = ["GTACAACTGT",
"CAACTATGAA",
"TCCTACAGGA",
"AAGCAAGGGT",
"GCGTACGACC",
"TCGTCAGCGT",
"AACAAGGTCA",
"CTCAGGCGTC",
"GGATCCAGGT",
"GGCAAGTACC"]  

Motifs0 = [ "AACGTA",
    "CCCGTT",
    "CACCTT",
    "GGATTA",
    "TTCCGG"]
   
print ProfileWithPseudocounts(Motifs0)   
  
 
count = {"A": [2, 2, 0, 0, 0, 0, 9, 1, 1, 1, 3, 0],
        "C": [1, 6, 0, 0, 0, 0, 0, 4, 1, 2, 4, 6], 
        "G": [0, 0,10,10, 9, 9, 1, 0, 0, 0, 0, 0],
        "T": [7, 2, 0, 0, 1, 1, 0, 5, 8, 7, 3, 4]}

profile = {}

t = 0 
for symbol in count: 
    t += count[symbol][0]

k = len(count["A"])
for symbol in count:
    profile[symbol] = []
    for i in range(k):
        profile[symbol].append(count[symbol][i]*1.0/t)
        
    
print Pr("ACGGGGATTACC",profile)

print type("ACGGGGATTACC"[0:5])'''
        
    
    