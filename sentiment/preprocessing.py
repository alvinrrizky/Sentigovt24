import string
import re
import nltk 
from nltk.tokenize import word_tokenize
from nltk.tag import CRFTagger
from nltk.corpus import stopwords
import os


nltk.download('punkt')
nltk.download('stopwords')
utils_path = os.path.join(os.path.dirname(__file__), '../utils/')

class TextPreprocessing():

    def removeIrrelevantTweet(self, tweets):
        file_path = os.path.join(os.path.dirname(__file__), '../utils/dictionaries/blacklist_words.txt')
        blacklist_words=[line.rstrip() for line in open(file_path)]
        results1 = [item for item in tweets if any(keyword.lower() in item.get('text').lower() for keyword in re.split("|".join(map(re.escape, [";", " "])), item.get('keyword')))]
        results2 = [item for item in results1 if all(bl_word.lower() not in item.get('text').lower() for bl_word in blacklist_words)]
        return results2

    def removeNoiseText(self, text):
        text = str(text)
        
        # removeHastagsMentionsUrl
        text = ' '.join(re.sub("(\B[#@][\w.]+)|(\w+:\/\/\S+)|(\w+.co/\w+)"," ", text).split());
        # incomplete url
        text = text.replace("http://", " ").replace("https://", " ").replace("http", " ").replace("http", " ")

        #removeHtmlTags
        text = ' '.join(re.sub("\B(<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6}))"," ", text).split());

        # removeNonAscii
        text = text.encode('ascii', 'replace').decode('ascii')
        # text.encode('ascii', 'replace')

        # removeNumber
        text = re.sub(r"\d+", "", text)

        # handleReduplicationWord
        re.sub(r'\b(\w+)-\1\b', r'\1', text, flags=re.IGNORECASE)

        # removePunctuation
        text = text.translate(str.maketrans(string.punctuation, " " * len(string.punctuation)))

        # removeMultipleChar
        full_capital_words = re.findall(r'\b[A-Z]+\b', text)
        for word in text.split(" "):
            if word not in full_capital_words:
                removed_mulchar_word = re.sub(r'(.)\1{2,}', r'\1\1', word, flags=re.IGNORECASE)
                removed_mulchar_word = re.sub(r'(.)\1+$', r'\1', removed_mulchar_word, flags=re.IGNORECASE)
                removed_mulchar_word = re.sub(r'^(.)\1+', r'\1', removed_mulchar_word, flags=re.IGNORECASE)
                text = re.sub(r'\b' + word + r'\b', removed_mulchar_word, text)

        # removeSingleChar
        text = re.sub(r"\b[a-zA-Z]\b", "", text)

        # removeLaughText
        for word in text.split(" "):
            if ''.join(sorted(set(word.casefold()))) in ['ah', 'eh', 'hi', 'ck', 'ix', 'akow', 'akw','kw'] and len(word) >= 4:
                text = re.sub(word, "", text)

        #removeWhitespaceLT
        text = text.strip()

        #removeWhitespaceMultiple
        text = re.sub('\s+',' ',text)

        return text
    
    def caseFolding(self, text):
        return text.lower()
   
    def wordRetokenize(self, document):
        document = ' '.join(document)
        return word_tokenize(document)

    def wordTokenize(self, document):
        return word_tokenize(document)
       
    def normalizeSlangWords(self, document):
        file_path = os.path.join(os.path.dirname(__file__), '../utils/dictionaries/normalize_dictionary.txt')
        slang_word_source=[line.strip('\n').strip('\r') for line in open(file_path)]
        slang_word_dict={}

        for i in slang_word_source: 
            (key,val)=i.split('\t')
            slang_word_dict[key]=val

        return [slang_word_dict[term] if term in slang_word_dict else term for term in document]
    
    def negationHandlingPOS(self, document):
        ct = CRFTagger()
        file_path = os.path.join(os.path.dirname(__file__), '../utils/models/all_indo_man_tag_corpus_model.crf.tagger')
        ct.set_model_file(file_path)
        pos_tagged_document = ct.tag_sents([document])

        words = []

        for tup in pos_tagged_document[0]:
            words.append(list(tup))

        flag = False
        neg_word = 0
        for i in range(len(words)):
            if words[i][1] == "NEG":
                flag = not flag
                if words[i][0] in ["tidak", "tak"]:
                    neg_word = 1
                if words[i][0] in ["bukan"]:
                    neg_word = 2
                if words[i][0] in ["belum", "jangan"]:
                    neg_word = 3
                continue
            if flag:
                if  neg_word == 1 and words[i][1] in ["JJ", "VB", "NN", "NNP", "CD", "RB", "MD"]:
                    words[i][0] = "NEG_"+words[i][0]
                if  neg_word == 2 and words[i][1] in ["JJ", "NN", "NNP", "CD"]:
                    words[i][0] = "NEG_"+words[i][0]
                if  neg_word == 3 and words[i][1] in ["JJ", "VB", "RB", "MD"]:
                    words[i][0] = "NEG_"+words[i][0]
                flag = False
            neg_word = 0
        return [words[i][0] for i in range(len(words))]
    
    def removeStopWords(self, words):
        file_path = os.path.join(os.path.dirname(__file__), '../utils/dictionaries/stopword_add_dictionary.txt')
        additional_stopwords = [line.rstrip() for line in open(file_path)]
        list_stopwords = stopwords.words('indonesian')
        list_stopwords.extend(additional_stopwords)
        list_stopwords = set(list_stopwords) 
        return [word for word in words if word not in list_stopwords]
    
    def getFinalPreprocessingResult(self, document):
        document = str(document)
        cleaned_data = self.removeNoiseText(document)        
        casefolded_data = self.caseFolding(cleaned_data)
        tokenized_data = self.wordTokenize(casefolded_data)
        normalized_text = self.normalizeSlangWords(tokenized_data)
        normalized_text =self.wordRetokenize(normalized_text)
        negHandling_text = self.negationHandlingPOS(normalized_text)
        filtered_text = self.removeStopWords(negHandling_text)
        return ' '.join(filtered_text)
