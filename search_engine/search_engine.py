import numpy as np

#TODO
#Less articles, memory error at termbydocument
def readDataSet(filePath, numOfArticles):

    with open(filePath, "r") as file:
        content = file.read()

        print("Replacing special characters")
        content = content.replace(',', '').replace('.', '').replace(':', '').replace('"', '').replace('-', ' ').replace('?', '').replace('!', '').replace('(', '').replace(')', '').replace('\'s', '').lower()

        #Getting only limited amount of documents
        content = content.split('\n\n')
        content = content[:numOfArticles]
        content = "\n\n".join(content)

        bagOfWords = {}
        articles = {}

        # Get the words counter
        index = 0
        words = content.split()

        for word in words:

            bagOfWords.setdefault(word, {
                "counter": 0,
                "index": 0
            })

            bagOfWords[word]["counter"] += 1
            if bagOfWords[word]["counter"] == 1:
                bagOfWords[word]["index"] = index
                index += 1

        # Getting separate articles
        index = 0
        content = content.split('\n\n')

        for article in content:
            
            article = article.split('\n')

            # Getting the title and removing it from article data
            title = article[0]
            article = "\n".join(article[1:])

            if title not in articles:
                articles[title] = {
                    "article": article,
                    "index": index
                }
                index += 1
            
    return articles, bagOfWords
            
def getTermByDocumentMatrix(bagOfWords, articles):
    result = np.zeros((len(bagOfWords), len(articles)))

    for key, value in articles.items():
        words = value['article'].split()
        words.extend(key.split())

        for word in words:
            result[bagOfWords[word]["index"]][value['index']] += 1
    
    return result

def IDF(articles, termByDocument):
    for wordIndex in range(len(termByDocument)):
        counter = 0
        for docIndex in range(len(termByDocument[wordIndex])):
            if termByDocument[wordIndex][docIndex] > 0:
                counter += 1
    
        idf = np.log(len(articles)/counter)
        termByDocument[wordIndex,:] *= idf

def search(words, termByDocument, bagOfWords):
    q = np.zeros((len(termByDocument)))
    words = words.split()

    for word in words:
        if word in bagOfWords:
            q[bagOfWords[word]['index']] += 1
    
    q /= np.linalg.norm(q)

    result = []
    for docIndex in range(len(termByDocument[0])):
        column = termByDocument[:,docIndex]
        result.append(q.dot(column)/np.linalg.norm(column))
    
    result = [[index, value] for index, value in enumerate(result)]
    result.sort(key = lambda x: x[1], reverse=True)

    return np.array(result[:3])

def getResultArticles(results, articles):
    result = ''
    temp = list(articles.items())
    for title, data in temp:
        if data['index'] in results[:,0]:
            result += title + '\n'
            result += data['article'] + '\n\n'
    return result

# if __name__ == "__main__":
#     articles, bagOfWords = readDataSet('corpus.txt', 1000)

#     termByDocument = getTermByDocumentMatrix(bagOfWords, articles)

#     IDF(articles, termByDocument)

#     result = search("mathematics", termByDocument, bagOfWords)
#     print(result)
#     printResultArticles(result, articles)
