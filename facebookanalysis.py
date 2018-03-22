from textblob import TextBlob
f = open('D:/vit/web mining/project11/abc.txt')
a=[]
for word in f.read().split():
    a.append(word)
print("reading of words done..\n")
stp=['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', '.' , ',' , '!', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than', 'this' , 'that']
fltrd=[]
for w in a:
    if w not in stp:
        fltrd.append(w) #eliminating stop words
print("stemming of words done..\n")
positive=0
negative=0

for f in fltrd:
	analysis = TextBlob(f)
	if(analysis.sentiment.polarity > 0): #sentiment analysis
		positive=positive+1
	elif(analysis.sentiment.polarity < 0):
		negative=negative+1
positivity=(positive/(positive+negative))*100
negativity=(negative/(positive+negative))*100
print("Number of positive responses are:")
print(positive)
print("\nNumber of negative responses are:")
print(negative)
print(" \nPositive comments percentage is: ")
print(positivity)
print("\n Negative comments percentage is: ")
print(negativity)