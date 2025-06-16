#clean_title.py
cuss_words = ["hell", "shit", "fuck", "ass"]

def main():
#Ask user for book title
    while True:
        title = input("Insert the title of your book: ")
#Attach check()
        result = check(title)
#Print book title if cleaned
        if result is True:
            print("Oh no! Your book contains illicit language. Please try again.")
        else:
            print("Here is your updated book title: " + result)
            print("Enjoy the rest of your day!")
            break



def check(phrase):
#If book title contains bad words, ask for another book title
    phrase = phrase.strip().lower()
    words = phrase.split()
    if any(word in cuss_words for word in words):
        return True
#If book title clean then print updated book title
    else:
        return phrase.strip().title()

    
main()
