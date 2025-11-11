"""
HackBio Internship - Stage 1 Python Task
Team: Glycine

# Task: Write a Python function for calculating the hamming distance between your slack username ('Opemidimeji Osatoyinbo') and twitter/X handle (@opemidimeji_xo)
# Author: Opemidimeji Osatoyinbo
# GitHub: https://github.com/opemidimejiosatoyinbo
# LinkedIn: https://linkedin.com/in/opemidimejiosatoyinbo
"""
def hamming_distance(str1: str, str2: str, pad_char: str = "_") -> int:
    """
    Compute Hamming distance between two strings after normalizing.

    Parameters
    ----------
    str1, str2 : str
        Input strings to compare. Spaces are removed; case is preserved.
    pad_char : str
        Character used to pad the shorter string.

    Returns
    -------
    int
        Count of differing positions.
    """
    # Normalize: remove spaces (user asked for this behavior previously)
    s1 = str1.replace(" ", "")
    s2 = str2.replace(" ", "")
    max_len = max(len(s1), len(s2))
    s1 = s1.ljust(max_len, pad_char)
    s2 = s2.ljust(max_len, pad_char)
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))


if __name__ == "__main__":
    slack = "Opemidimeji Osatoyinbo"
    twitter = "@opemidimeji_xo"
    print("Slack:", slack)
    print("Twitter:", twitter)
    print("Hamming distance:", hamming_distance(slack, twitter))