
# coding: utf-8

# In[5]:

#!ipython nbconvert --to=python __init__.ipynb


# In[4]:

import ImportIpython as II
from readHTML import makesoup,get_div,get_varnname,get_style
from NoteTemplate import newHTMLnote, addmaps, addonemap, addmarkdown, currenttime, latestnote

__version__='0.9.0'

__all__=['makesoup',
         'get_div',
         'get_varnname',
         'get_style',
         'newHTMLnote',
         'addmaps',
         'addonemap',
         'addmarkdown',
         'currenttime',
         'latestnote']


# In[ ]:



