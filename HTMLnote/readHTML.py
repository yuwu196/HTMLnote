
# coding: utf-8

# In[1]:

# !ipython nbconvert --to=python readHTML.ipynb


# In[1]:

from bs4 import BeautifulSoup


# In[2]:

class mapHTML:
    def __init__(self, filename,size=30,fold_path='/Users/yuwu/Desktop/UIUC/MP/RunningPlatform/zoom13'):
        self.filename=filename
        self.fold_path=fold_path
        self.size=size
        self.soup=makesoup(filename,self.fold_path)
        self.style=get_style(self.soup,self.size)
        self.div=get_div(self.soup)
        self.mapname, self.var = get_varnname(self.soup)


# In[3]:



#class readH:
    
def makesoup(filename,fold_path):
    #filename="relative27_172.html"
    pathforfile = fold_path+"/{}"
    file = open(pathforfile.format(filename))
    print ("soup is done!")
    return BeautifulSoup(file,"lxml")

def get_div(soup):
    get_div = soup.find_all("div")
    div = str(get_div)
    return div[1:len(div)-1]

def get_varnname(soup):
    get_scriptvar = soup.find_all('script')
    temp = str(get_scriptvar)
    start=temp.index("var map")
    temp=temp[start:]
    allvar = temp.split("</script")[0]
    mapname = allvar.split(' ')[1]
    return mapname,allvar





# In[4]:

def get_style(soup,size):
    get_style = soup.find_all('style')
    temp =str(get_style)
    temp = temp.split('style> ')[1]
    temp = '<style> '+temp
    temp = temp.split('100.')
    style = temp[0]+str(size)+'.'+temp[1]+str(size)+'.'+temp[2]
    style = style.replace(']','')
    return style


# In[11]:

'''

s=mapHTML("relative27_168.html")
s.style
'''


# In[6]:

'''
s=get_style(makesoup(''))
s
'''


# In[7]:

'''
for city in soup.find_all('span', {'class' : 'script'}):
    print(city
    '''

