class TextClassification:
    def __init__(self,url):
        data = pd.read_csv(url)
        self.train = data
        self.vocabulary = []
        self.positive_prior = {}
        self.negative_prior = {}
        self.positive_table,self.negative_table = self.divide_sets()
        p,n,v = len(positive_set),len(negative_set),len(self.vocabulary)
    def extract_vocabulary(self):
        for text in self.train['text']:
            text = text.lower()
            words = text.split()
            for word in words:
                if word not in self.vocabulary:
                    self.vocabulary.append(word)
    def divide_sets(self):
        positive_set = self.train[self.train['status']=='pos']
        negative_set = self.train[self.train['status']=='neg']
        #term frequency matrix for positive documents
        positive_data = {}
        for text,index in zip(positive_set['text'],positive_set.index):
            positive_data[index] = []
            terms = text.lower().split()
            for word in self.vocabulary:
                positive_data[index].append(terms.count(word))
        positive_table = pd.DataFrame(positive_data)
        positive_table.index = self.vocabulary
        positive_table = positive_table.T
        positive_table
        #term frequency matrix for negative documents
        negative_data = {}
        for text,index in zip(negative_set['text'],negative_set.index):
            negative_data[index] = []
            terms = text.lower().split()
            for word in self.vocabulary:
                negative_data[index].append(terms.count(word))
        negative_table = pd.DataFrame(negative_data)
        negative_table.index = self.vocabulary
        negative_table = negative_table.T
        negative_table
        return positive_table,negative_table
    def getPrior(self):
        for word in self.vocabulary:
            self.positive_prior[word] = round((sum(self.positive_table[word].to_list())+1)/(p+v),2)
            self.negative_prior[word] = round((sum(self.negative_table[word].to_list())+1)/(n+v),2)
    def predict(self,text):
        terms = text.lower().split()
        (pos,neg) = (1,1)
        for term in terms:
            pos *= positive_prior[term]
            neg *= negative_prior[term]
        if pos>= neg:
            return 'pos'
        return 'neg'
obj = TextClassification(r"C:\Users\exam2\Downloads\text_classification.csv")
result = []
for text in test['text']:
    result.append(obj.predict(text))
print(result)
