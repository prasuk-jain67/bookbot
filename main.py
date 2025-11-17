from stats import get_num_words,get_char_count,return_sorted
import sys
def get_book_text(filePath):
    with open(filePath,'r', encoding='utf-8') as f:
        file_contents = f.read()
    return file_contents
def main(book_path):
    text = get_book_text(book_path)
    return text

if __name__ == "__main__":
    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path =sys.argv[1]
    text=main(path)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print(f"Found {get_num_words(text)} total words")
    print("--------- Character Count -------")
    char_frequency= return_sorted(get_char_count(text))
    for dict in char_frequency:
        print(f"{dict["char"]}: {dict["count"]}")
        
    print("============= END ===============")
   
    
   