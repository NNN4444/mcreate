#coding=utf8
import sys
sys.path.append('/usr/local/bin/python3/site-packages')
from urllib import request, response
from bs4 import BeautifulSoup
import markovify
import MeCab
import re


url = 'https://bloodborne.swiki.jp/index.php?%E3%82%A2%E3%82%A4%E3%83%86%E3%83%A0'
response = request.urlopen(url)
soup = BeautifulSoup(response,features="lxml")
response.close()
for script in soup(["script", "style"]):
    script.decompose()
text1 =soup.find_all('td',style="background-color:white; width:380px;",text='')
textlist =[x.text.replace("\u3000",",") for x in text1]
text = "".join(textlist)
# Parse text using MeCab
#text formatting
parsed_text = MeCab.Tagger('-Owakati').parse(text)
parsed_text = parsed_text.replace('　', ' ')
parsed_text = re.sub(r'(.+。) (.+。)', r'\1 \2\n', parsed_text)
parsed_text = re.sub(r'\n +', '\n', parsed_text)  # Spaces
parsed_text = re.sub(r'([。．！？…])\n」', r'\1」 \n', parsed_text)  # \n before 」
parsed_text = re.sub(r'\n +', '\n', parsed_text)  # Spaces
parsed_text = re.sub(r'\n+', r'\n', parsed_text).rstrip('\n')  # Empty lines
parsed_text = re.sub(r'\n +', '\n', parsed_text)  # Spaces
parsed_text = parsed_text.replace('。','\n')
# Build model
text_model = markovify.NewlineText(parsed_text, state_size=3,well_formed=False)

#make text
#Determine errors
for _ in range(1):
 lasttext=text_model.make_short_sentence(100, 0, tries=100)
 if (lasttext != None):
  lasttext=lasttext.replace(' ', '')
  print(lasttext)
 else:
    print('生成失敗')


