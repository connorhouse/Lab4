stringOne = 'The quick brown fox jumps over the lazy dog'
print(stringOne.lower())

def getMostFrequent(str):
    NO_OF_CHARS = 256

    count = [0] * NO_OF_CHARS

    for i in range(len(str)):
        count[ord(str[i])] += 1

    first, second = 0, 0

    for i in range(NO_OF_CHARS):

        if count[i] < count[first]:

            second = first
            first = i

        elif (count[i] > count[second] and
              count[i] != count[first]):

            second = i

            # return character
    return chr(second)

if __name__ == "__main__":

    str = "The" "quick" "brown" "fox" "jumps" "over" "the" "lazy" "dog"

    res = getMostFrequent(str)
    if res != '\0':
        print("The most frequent character is:", res)
    else:
        print("No most frequent character")


def uniqueLetters(stringOne):
    y = []
    for b in stringOne:
        if b not in y:
            y.append(b)
    return y
print(uniqueLetters(stringOne))

                                                        # Create a file called lists.py. Complete the following in lists.py:
                                                        # Create a list by calling the list() function with the following string "The quick brown fox jumps over the lazy dog." Convert all letters to lowercase before calling the list() function.
                                                        # Sort the list.
                                                        # Create a function called getMostFrequent() that outputs which letter(s) (excluding spaces) occurs the most often in the sentence. Indicate which letter and the in README.md.
                                                        # Create another function called uniqueLetters() that creates a list of all unique characters in the string/list. Then it should ouput each unique character in order.