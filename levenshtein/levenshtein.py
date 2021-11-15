import numpy as np
def levenshteinDistanceDP(token1, token2):
    distances_matrix = np.zeros((len(token1) + 1, len(token2) + 1))

    for s1 in range(len(token1) + 1):
        distances_matrix[s1][0] = s1

    for s2 in range(len(token2) + 1):
        distances_matrix[0][s2] = s2

    for s1 in range(1, len(token1) + 1):
        for s2 in range(1, len(token2) + 1):
            if (token1[s1 - 1] == token2[s2 - 1]):
                distances_matrix[s1][s2] = distances_matrix[s1 - 1][s2 - 1]
            else:
                lev1 = distances_matrix[s1][s2 - 1]
                lev2 = distances_matrix[s1 - 1][s2]
                lev3 = distances_matrix[s1 - 1][s2 - 1]

                if (lev1 <= lev2 and lev1 <= lev3):
                    distances_matrix[s1][s2] = lev1 + 1
                elif (lev2 <= lev1 and lev2 <= lev3):
                    distances_matrix[s1][s2] = lev2 + 1
                else:
                    distances_matrix[s1][s2] = lev3 + 1
    distance = distances_matrix[-1][-1]
    return distances_matrix, distance