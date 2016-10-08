import json

with open('repos.json') as data_file:
    data = data_file.read()
jdata=json.loads(data)

url_list=[]
name_list=[]
for repo in jdata:
    url_list.append(repo['html_url']+'.git')
    name_list.append(repo['name']+'.git')
#print(url_list)
urlfile = open('url_list.txt','w')
#namefile=open('name_list.txt','w')
for u,n in zip(url_list, name_list):
#print(u,n)
#for url in url_list:
    urlfile.write(u+' '+n+'\n')

#for name in name_list:
 #   namefile.write("%s\n" % name)

    
