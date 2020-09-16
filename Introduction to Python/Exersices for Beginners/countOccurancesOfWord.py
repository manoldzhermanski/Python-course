def countOccurances(text,word):
    result = text.count(word)
    return result

print("Number of occurances:",countOccurances("Emma is good developer. Emma is a writer","Emma"))

def countOccurances2(text,word):
    print("Given String: ", text)
    count = 0
    for i in range(len(text) - 1):
        count += text[i: i + len(word)] == word
    return count

count = countOccurances2("Emma is good developer. Emma is a writer","Emma")
print("Emma appeared ", count, "times")
