def words(book_text):
    words=book_text.split()
    word_count=len(words)
    return word_count

def get_letter_count(book_text):
    letter_count={}
    for char in book_text:
        char=char.lower()
        letter_count[char]=letter_count.get(char,0)+1
    return letter_count

def sort_on(letters):
    return letters["num"]

def sort_letter_count(letter_count):
    result=[]
    for char, count in letter_count.items():
        result.append({"char": char,"num":count})
    result.sort(reverse=True, key=sort_on)
    return result