s1 = "Sahixl"
s2 = "lihasl"


def anagramCheck(s1, s2):
    if len(s1) != len(s2):
        print("Strings are not Anagrams :(")
        return

    if set(s1.lower()) != set(s2.lower()):
        print("Strings are not Anagrams !")
    else:
        print("Strings are Anagrams :)")


anagramCheck(s2, s1)
