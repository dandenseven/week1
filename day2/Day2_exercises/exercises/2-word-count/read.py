import re
from collections import Counter
with open("article.txt") as f:
    text = f.read()

    words = re.compile(r"[\w']+", re.U).findall(text)  
    counts = Counter(words)
    for word, count in counts.most_common(10):
        print (word, ": ", count)

