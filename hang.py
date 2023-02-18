import requests
from bs4 import BeautifulSoup
import random

response = requests.get('https://www.ef.com/wwen/english-resources/english-vocabulary/top-3000-words/')

soup = BeautifulSoup(response.content, 'html.parser')
tag = soup.find('div', {'class':'field-item even'})
words = tag.find('p')

words_list = [i for i in words if "" in i]
words_list.pop(0)


with open('hangman.txt', 'r') as image:
    emojis = image.read().splitlines()

def game():
    word = str(random.choice(words_list)).lower()
    word_len = ('_,' * len(word)).split(',')
    count = 8

    while '_' in word_len: 
        if count == 0:
            print(f"You're out of tries. GAME OVER.\nYour word was: {word}")
            break

        print(''.join(word_len)) 
        
        print('would you like to guess a single letter (n) or the entire word (y)?')
        answer = input('type "n" for single letter, "y" for an entire word. (an anomaly will be treated as "n"): ').lower()
        print('\n')
        if answer not in ['y','n']:
            answer = 'n'
        if answer == 'n':    
            letter = input('Guess a single letter: ').lower()
            while len(letter) != 1 or letter.isalpha == False:
                letter = input('Input is invalid. please make sure you input a single alphanumeric character: ').lower()

            if letter in word:
                ind = 0
                for l in word:
                    if l == letter:
                        word_len[ind] = letter
                    ind += 1 
                print(f'Good job! Your guess ("{letter}") was correct.') 
            else:
                count -= 1
                print(f'Your guess ("{letter}") was incorrect!')
                if count == 1:
                    print ('This is your last try. Make it count!')
                else:
                    print(f'{count} tries left...')        
                for ind in range(23):
                    print(emojis[0])
                    emojis.pop(0)
        else:
            word_input = input('Guess your word: ').lower()  
            if word_input == word:
                break
            else:  
                count -= 1
                print(f'Your guess ("{word_input}") was incorrect!')       
                if count == 1:
                    print ('This is your last try. Make it count!')
                else:
                    print(f'{count} tries left...')    
                for ind in range(23):
                    print(emojis[0])
                    emojis.pop(0)   
    if count != 0:
        print(f'You win! your word was "{word}"')       

if __name__ == '__main__':
    game()         
