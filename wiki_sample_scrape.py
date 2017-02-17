import requests
import random

consonants = ('b','c','d','f','g','h','j','k','l','m','n','o','p','q','r','s','t','v','w','x','y','z')
vowels = ('a','e','i','o','u')

for cons in consonants:
    for vow in vowels:
        letters = cons + vow 
        r = "https://en.wikipedia.org/w/api.php?action=query&generator=allpages&gaplimit=30&gapfrom=" + letters + "&prop=links&format=json"
        requests.get(r)


# with open(os.path.join(filepath, filename),'a') as gift_file:
#         gift_file.truncate()
#         gift_file.write('\t'.join(t[0] for t in rows[0].cursor_description)+'\n')
#         for row in rows:
#             gift_file.write('\t'.join(str(f) for f in row)+'\n')



"https://en.wikipedia.org/w/api.php?action=query&generator=allpages&gaplimit=50&gapfrom=" + letters + "&prop=links&format=json"