import json

with open('repos.json') as data_file:
    data = data_file.read()
jdata=json.loads(data)

url_list=[]
for repo in jdata:
    url_list.append(repo['html_url']+'.git')
#print(url_list)
thefile = open('list.txt','w')
for url in url_list:
    thefile.write("%s\n" % url)

    
