
def checkCount(config, dictionary):
    pass
    
def genConfig(dials=3, size=5):
    dial_assign =[a,b,c]
    from itertools import combinations
    print len(list(combinations(range(26),3)))

def bruteForce(dials=3, size=5, dictionary):
    freq =0
    maxconf = None
    conf = genConfig(dials,size)
    current_count = checkCount(conf,dictionary)
    if current_count > freq:
       freq = current_count
       maxconf = conf
    return maxconf
 

def read3LetterWords(path='words.txt'):
    dictionary = set()
    with open(path,'r') as f:
        word = f.readline().rstrip()
        dictionary.add(word)
    return dictionary

if __name__=='__main__':
    dictionary = read3LetterWords()
    conf = bruteForce(3,5,dictionary)
    print conf 
