def get_num_words(text):
    words= text.split()
    return len(words)
def get_char_count(text):
    char_frequency = {}
    for symbol in text:
        if symbol.lower() in char_frequency:
            char_frequency[symbol.lower()]+=1
        else:
            char_frequency[symbol.lower()]=1
    return char_frequency
def sort_on(freq):
    return freq["count"]
def return_sorted(freq):
    lst=[]
    for val in freq:
        lst.append({"char":val ,"count":freq[val]})
    lst.sort(reverse=True,key=sort_on) 
    return lst
        
        