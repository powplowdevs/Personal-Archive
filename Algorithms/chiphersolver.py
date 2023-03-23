import random
#from nltk.corpus import words

chiper = "shv oiwikbke nf khx vpwkdam ij tal fslk mzn: z cklulxu hhm rt moy ktde side ppnz myas. emekfnzbeg rugekooete aopvakz ng frn zs zleuykl rnc mrdgImk. rfu game mv vw t jez tf auziju r dhrky lalwtd whtyona awmkimg uikas."
                                                                                                                                                                                                                                                
ans = ""         
            
alphabet = "abcdefghijklmnopqrstuvwxyz"
free_letters = alphabet
key = ""

atempt = 0

#create key
def create_key():
    global chiper, alphabet, free_letters, key
    for i in range(len(alphabet)):
        while True:
            #get a random letter
            place = random.randint(0,len(alphabet)-1)
            letter = alphabet[place]
            
            #check if letter is free
            if letter in free_letters:
                break
        
        #letter is no longer free    
        free_letters = free_letters.replace(letter, "")
        key = key + letter

#unscramble
def unscramble():
    global chiper, alphabet, free_letters, key, ans
    for i in range(len(chiper)):
        chiper_letter = chiper[i]
        try:
            if chiper_letter in alphabet:
                index = alphabet.index(chiper_letter)
                ans = ans + key[index]
            else:
                ans = ans + " "
        except:
            print("Error, i:",i,"index:",index)
 
#reset
def reset():
    global chiper, free_letters, key, ans
    chiper = "shv oiwikbke nf khx vpwkdam ij tal fslk mzn: z cklulxu hhm rt moy ktde side ppnz myas. emekfnzbeg rugekooete aopvakz ng frn zs zleuykl rnc mrdgImk. rfu game mv vw t jez tf auziju r dhrky lalwtd whtyona awmkimg uikas."
    ans = ""              
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    free_letters = alphabet
    key = ""
    
while True:  
    create_key()
    unscramble()    
     
    if("friedrich nietzsche" in ans or "friedrich" in ans or "nietzsche" in ans or " friedrich nietzsche " in ans):
        print("Key: " + key + "\nans: " + ans + "\nAtempt: " + str(atempt) + "\n\n")
        
    atempt+=1
    
    reset()
    
