import xmltodict

with open ('nvd-rss-analyzed.xml') as raw:
	doc = xmltodict.parse(raw.read())
 
sliced = doc['rdf:RDF']['item']

titles = []
urls = []
descriptions = []

with open ('final_output.csv', 'w') as output:
	output.write('title,link,description\n')

for index, item in enumerate(sliced):
	# if index == 0:
		
	# 		output.write(sliced[index]['title'].replace(',','') +',')
	# 		output.write(sliced[index]['link'].replace(',','')+',')
	# 		output.write(sliced[index]['description'].replace(',','')+',\n')
	# else:
	with open('final_output.csv', 'a') as output:
		output.write(sliced[index]['title'].replace(',','')+',')
		output.write(sliced[index]['link'].replace(',','')+',')
		output.write(sliced[index]['description'].replace(',','')+',\n')



