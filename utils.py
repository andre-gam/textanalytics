import nltk
import string

class PreProcessamento():

    def tokenize(self,X):
        for i in range(0,len(X)):
            X[i] = X[i].lower()
            X[i] = ''.join([p for p in X[i] if p not in string.punctuation])
            X[i] = nltk.word_tokenize(X[i])
        return X


    def remove_stopwords(self, X, stopword_list):
        ls = []

        for tk_line in X:
            new_tokens = []
            
            for word in tk_line:
                if word.lower() not in stopword_list:
                    new_tokens.append(word) 
                
            ls.append(new_tokens)
        
        return ls
    
    def apply_standardization(self, tokens, std_list):
        ls = []

        for tk_line in tokens:
            new_tokens = []
            
            for word in tk_line:
                if word.lower() in std_list:
                    word = std_list[word.lower()]
                    
                new_tokens.append(word) 
                
            ls.append(new_tokens)

        return ls

    def apply_stemmer(self,tokens):
        ls = []
        stemmer = nltk.stem.RSLPStemmer()

        for tk_line in tokens:
            new_tokens = []
            
            for word in tk_line:
                word = str(stemmer.stem(word))
                new_tokens.append(word) 
                
            ls.append(new_tokens)
            
        return ls
    
    def generate_N_grams(self,text,ngram=1):
        ##words=[word for word in text.split(" ") if word not in set(stopwords.words('english'))]  
        ##print("Sentence after removing stopwords:",words)
        ls = []
        for tokens in text:
            temp=zip(*[tokens[i:] for i in range(0,ngram)])
            ans=[' '.join(ngram) for ngram in temp]
            ls.append(ans)
        return ls

    def untokenize_text(self, tokens):
        ls = []

        for tk_line in tokens:
            new_line = ''
            
            for word in tk_line:
                new_line += word + ' '
                
            ls.append(new_line)
            
        return ls

class Evaluation():

    ##def __init__(self):
          
    def get_accuracy(self,matrix):
        acc = 0
        n = 0
        total = 0
        
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix)):
                if(i == j): 
                    n += matrix[i,j]
                
                total += matrix[i,j]
                
        acc = n / total
        return acc

    def f_score(self,matrix):
        tp = 0
        fp = 0
        fn = 0
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix)):
                if(i == 0 and j==0): 
                    tp += matrix[i,j]
                if(i==0 and j==1):
                    fn += matrix[i,j]
                if (i==1 and j==0):
                    fp += matrix[i,j]
        precision = tp / (tp+fp)
        recall = tp / (tp+fn) 
        f_score = (2 * precision * recall)/(precision + recall)
        return f_score

