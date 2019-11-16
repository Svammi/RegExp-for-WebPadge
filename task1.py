import requests
import re

url = 'https://www.labnol.org/internet/duplicate-gmail-draft-emails/29124/'

response = requests.get(url)
doc = response.content.decode('utf-8')

headers = '<h1.*?>(.*?)</h1>|<h2.*?>(.*?)</h2>|<h3.*?>(.*?)</h3>|<h4.*?>(.*?)</h4>|<h5.*?>(.*?)</h5>?|<h6.*?>(.*?)</h6>'
headers_res = re.findall(headers, doc)
tup = []
for i in headers_res:
    for j in i:
        if len(j)>0:
            tup.append(j)

print("HEADERS: ",tup)


image = '<img.*?>'
image2 = 'src=\"(http(s)?.*?)?\"'
image_res = re.findall(image, doc)
image_res2 = []
for i in range(len(image_res)):
    image_res2.append(re.search(image2, image_res[i]).group())

print("IMAGE: ", image_res2)

article = '<article>((.|\s)*?)</article>'
article2 = '(<p>|<li>)(.|\s)*?(</p>|</li>)'
article_res = re.findall(article, doc)
article_res2 = re.search(article2, article_res[0][0]).group()
matches = re.finditer(article2, article_res[0][0])
text = []
for matchNum, match in enumerate(matches, start=1):
    text.append(match.group())
print("ARTICLE: ",text)





