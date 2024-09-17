def dna_match_topdown(DNA1, DNA2):
    print("TOPDOWN")
    
    if len(DNA1) == 0 or len(DNA2) == 0:
        return 0

    cache = [[-1 for x in range(len(DNA2) + 1)] for x in range(len(DNA1) + 1)]
    
    def lcs(i, j):
        if i == 0 or j == 0:
            return 0

        if cache[i][j] != -1:
            return cache[i][j]
        
        if DNA1[i - 1] == DNA2[j - 1]:
            cache[i][j] = 1 + lcs(i - 1, j - 1)
        
        else:
            cache[i][j] = max(lcs(i, j - 1), lcs(i - 1, j))

        return cache[i][j]

    return lcs(len(DNA1), len(DNA2))

def dna_match_bottomup(DNA1, DNA2):
    print("BOTTOMUP")
    rows = len(DNA1) 
    cols = len(DNA2)

    if len(DNA1) == 0 or len(DNA2) == 0:
        return 0

    cache = [[0 for x in range(len(DNA2) + 1)] for x in range(len(DNA1) + 1)]

    for i in range(len(DNA1) + 1):
        for j in range(len(DNA2) + 1):
            if i == 0 or j == 0:
                cache[i][j] = 0
            elif DNA1[i - 1] == DNA2[j - 1]:
                cache[i][j] = cache[i -1][j - 1] + 1
            else:
                cache[i][j] = max(cache[i][j - 1], cache[i - 1][j])

    return cache[rows][cols]
    

def main():

    DNA1 = "XXXXXXXXXX"
    DNA2 = "GTGTTCCCGTCAAA"

    result1 = dna_match_topdown(DNA1, DNA2)
    # result2 = dna_match_bottomup(DNA1, DNA2)
    print(f"Top Down: {result1}")
    # print(f"Bottom Up: {result2}")
main()