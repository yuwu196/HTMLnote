
# coding: utf-8

# In[96]:

#run this cell: updating py file
#!ipython nbconvert --to=python NoteTemplate.ipynb


# In[97]:

# 3 path here!!
#    %reset


# In[98]:

# FOR IMPORT IPYTHON
import sys
import ImportIpython as II
sys.meta_path.append(II.NotebookFinder())


# In[99]:

from readHTML import mapHTML


# In[100]:

#time upodated
import datetime
import time #delay for save template

def currenttime(): 
    t=datetime.datetime.now()
    return str(t.year)+'/'+str(t.month)+'/'+str(t.day)+'   '+str(t.hour)+':'+str(t.minute)+':'+str(t.second)


# In[101]:

def deepcopystr(b):
    return (b + '.')[:-1]


# In[102]:

import os
from jinja2 import Environment, FileSystemLoader

__file__='/Users/yuwu/Desktop/UIUC/HTMLnote_pkg/HTMLnote/templates/'
PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False)


global savename_ 
#savename_ = 'new_HTMLnote.html'
global author_



def newHTMLnote(author='{Please add author by newHTMLnote(author=\'\') }', savename='new_HTMLnote.html'):
    global savename_ 
    savename_=deepcopystr(savename)
    global author_
    author_=deepcopystr(author)
    
 


def render_template(template_filename, context):
    t = TEMPLATE_ENVIRONMENT.get_template(template_filename)
    return t.render(context)
 
 
def create_index_html( new, savename, text='', mapset=[]):
    #the name of the note file
    fname = savename
    
    if new: 
        templatefile='note_template.html'
    else: 
        templatefile='pre_template.html'
        #templatefile='new_template.html'
    
    
    
    title = savename.replace('.html','')
    print (title)
    title = '<h1>'+title+'</h1>'
    
    global author_
    footnote='<p><br><br><br><br><br></p><p>'+'Last Update: '+currenttime()+' by '+author_+'<br></p>'
    footnote=footnote+'<mark>HTMLnote is supported by Yu Wu</mark>'
    
    filenameset=[ '<h3>'+mapset[i].filename+'</h3>' for i in range(len(mapset)) ]
    styleset=[ mapset[i].style for i in range(len(mapset)) ]
    divset=[ mapset[i].div for i in range(len(mapset)) ]
    varset=[ mapset[i].var for i in range(len(mapset)) ]
    
    context = {
        'title': title,
        'filenames': filenameset,
        'styles': styleset,
        'divs': divset,
        'vars': varset,
        'footnote': footnote
              }
    
    if len(text)!=0: 
        paragraph= '<p>'+text+'</p>'
        context.update({'paragraph': paragraph})

    
    #
    path_note='/Users/yuwu/Desktop/UIUC/HTMLnote_pkg/yourHTMLnote/'
    with open(os.path.join(path_note, fname), 'w') as f:
        html = render_template(templatefile, context)
        f.write(html)

        
    #brilliant    
    continue1 = "{% for style in styles %} \n            {{ style }} \n            {% endfor %} \n            {{continue1}}\n"
    continue3 = "{% for var_ in vars %}\n            {{ var_ }} \n            {% endfor %} \n            {{continue3}}\n"
    continue0 = "{% for i in range(divs|length) %} \n            <h2> {{ filenames[i] }} </h2> \n            {{ divs[i] }} \n            {% endfor %} \n            {{ paragraph }}\n            {{ continue0 }} \n"
    continue_title = "{{ title }}\n"
    footnote="{{ footnote }}"
    
    context.update({
            'title': continue_title,
        'continue1': continue1,
        'continue3': continue3,
        'continue0': continue0,
         'footnote': footnote
              })
    
    #
    path_templates='/Users/yuwu/Desktop/UIUC/HTMLnote_pkg/HTMLnote/templates/'
    with open(os.path.join(path_templates, 'new_template.html'),'w') as c:
        cw_html = render_template(templatefile, context)
        c.write(cw_html)
        time.sleep(2)
        newtemp=os.path.join(path_templates, 'new_template.html')
        pretemp=os.path.join(path_templates, 'pre_template.html')
        os.rename(newtemp,pretemp)
        #os.rename('new_template.html','pre_template.html')
    
 
'''
FOR ALL ADDING OPERATION
-para: new = boolean
-para: savename = string 
#DO NOT FORGET '.html'
'''

 
def addmaps(mapset, new=False, savename='new_HTMLnote.html'):
    global savename_
    b0=(savename in 'new_HTMLnote.html')
    b1=(savename_ in savename)
    if not b0 and not b1:
        savename_=deepcopystr(savename)
        
    create_index_html(mapset=mapset,new=new, savename=savename_)
    print('#mapset is added!\n')
    
def addonemap(onemap, new=False, savename='new_HTMLnote.html'):
    global savename_
    b0=(savename in 'new_HTMLnote.html')
    b1=(savename_ in savename)
    if not b0 and not b1:
        savename_=deepcopystr(savename)
        
    mapset=[onemap]
    create_index_html(mapset=mapset,new=new, savename=savename_)
    print('\n#map is added!\n')
    
def addmarkdown(text, wordsperline=16, new=False, savename='new_HTMLnote.html'):
    '''
    -para: text = string
    -para: wordsperline = int
    -para: new =boolean
    -para: savename= string 
    #use /n to break manually OR adjust antomatically
    #savename: save the most updated version in the new file name(as savename)
    '''
    global savename_
    b0=(savename in 'new_HTMLnote.html')
    b1=(savename_ in savename)
    if not b0 and not b1:
        savename_=deepcopystr(savename)
        #print('CAHNGED TO '+savename_)
        
    #print ('!!!!! savename_  '+savename_)
    text=adjust(text,width=wordsperline*5)
    create_index_html(text=text,new=new, savename=savename_)
    print('#text is added!\n')
    
def latestnote():
    global savename_
    print('the latest HTMLnote is saved as '+ savename_)
    
########################################
 

    

    
    


# In[103]:


import textwrap
sample_text = 'Relative error of traffic density for a typical week. Error is between low-rank approximation and observed traffic, normalized by observed traffic. Black links are small error, red lines are moderately large error, and thick red lines are large error. Work by Yu Wu.'
sample_n    = 'Relative error of traffic density for a typical week. ' + '\n' +'Error is between low-rank ' + '\n'+'approximation and observed traffic, normalized by ' + '\n'+'observed ' + '\n'+'traffic. Black links are small error, red lines are moderately large error, and thick ' + '\n'+'red lines are large error. Work by Yu Wu.'



def adjust(text,width=80):
    dedented_text = textwrap.dedent(text).strip()
    result = dedented_text
    if '\n' not in text: 
        result = textwrap.fill(dedented_text, width=width)
    result= result.replace("\n",'<br>')
    #print(result)
    return result

#adjust(sample_text)


# In[104]:


'''

map0=mapHTML("relative27_180.html")
map1=mapHTML("relative27_182.html")
mapset=[map0,map1]
#addmaps(mapset,new=True)
#addmarkdown('Oh yeah!\n Is this the next line?')
#addmarkdown('what about another markdown?')
'''





# In[105]:



########################################
#if __name__ == "__main__":
#   main(mapHTML)


# In[106]:

'''
map3=mapHTML("relative27_250.html")
map4=mapHTML("relative27_300.html")
addonemap(map3,new=False)
'''


# In[107]:

'''
addonemap(map4,new=False)
'''


# In[108]:

#重复加一个图？


# In[109]:

'''

addmarkdown('wordsperline: DEFAULT   '+sample_text,new=True)
addmarkdown('wordsperline: 20   '+sample_text, wordsperline=20)


'''


# In[110]:

''' combination test'''
'''
map0=mapHTML("relative27_180.html")
map1=mapHTML("relative27_182.html",size=50)

newHTMLnote()
addmarkdown(text="11111111111",new=True)
latestnote()


addmarkdown(text="22222222222",savename='2nd.html')
latestnote()

addonemap(map0)
addmarkdown(text="33333333333")   #,savename='3rd.html'
addmaps([map1])
addmarkdown(text="44444444444")
latestnote()



'''


# In[ ]:




# In[111]:

'''
<h1> ~ <h6>
big  ~ samll


<b> - Bold text
<strong> - Important text
<i> - Italic text
<em> - Emphasized text
<mark> - Marked text
<small> - Small text
<del> - Deleted text
<ins> - Inserted text
<sub> - Subscript text
<sup> - Superscript text
'''

