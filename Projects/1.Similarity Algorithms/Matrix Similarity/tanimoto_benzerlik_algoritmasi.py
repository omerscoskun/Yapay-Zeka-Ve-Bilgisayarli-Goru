# region Imports

# endregion

# region Functions

def tanimoto_similarity(A, B):
    """
    Calculate the Tanimoto similarity between two binary vectors A and B.

    Parameters:
    A (list or array-like): First binary vector.
    B (list or array-like): Second binary vector.

    Returns:
    float: Tanimoto similarity coefficient.
    """
    if len(A) != len(B):
        raise ValueError("Vectors A and B must be of the same length.")

    # Convert inputs to sets of indices where the value is 1
    if all(isinstance(x, str) for x in A) and all(isinstance(x, str) for x in B):
        set_A = set(A)
        set_B = set(B)
    else:
        set_A = set(i for i, val in enumerate(A) if val == 1)
        set_B = set(i for i, val in enumerate(B) if val == 1)

    # Calculate intersection and union
    intersection = len(set_A.intersection(set_B))
    union = len(set_A.union(set_B))

    if union == 0:
        return 0.0  # Avoid division by zero; define similarity as 0

    # Calculate Tanimoto similarity
    similarity = intersection / union
    return similarity

# endregion

# region Main Code

array1 = ["elma", "armut", "muz", "çilek", "kiraz"]
array2 = ["elma", "muz", "kiraz", "karpuz", "üzüm"]

array3 = [1, 1, 1, 1, 1]
array4 = [1, 0, 1, 0, 1]

similarity_score = tanimoto_similarity(array1, array2)
print(f"Tanimoto Similarity for {array1} and {array2}: \n{similarity_score}")

similarity_score_numeric = tanimoto_similarity(array3, array4)
print(f"Tanimoto Similarity for {array3} and {array4}: \n{similarity_score_numeric}")


# endregion


# Example usage