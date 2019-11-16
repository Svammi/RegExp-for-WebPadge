import re

sentense = 'https://www.labnol.org/internet/duplicate-gmail-draft-emails/29124/'

reg = '(?:[-\w*\d*]{1,}[\/]?){2}$'

res = re.search(reg, sentense).group()
if res[-1] == '/':
    res = res[:-1].replace('/','-')
else:
    res = res.replace('/','-')

print(res)
