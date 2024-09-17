# Palindrome

def main():
    def palindrome_check(sentence):

        lower_sentence = sentence.lower()

        if lower_sentence == lower_sentence [::-1]:
            print(f'True')
        else: 
            print('False')

    sentence = input("")
    palindrome_check(sentence)

if __name__ == "__main__":
    main()
