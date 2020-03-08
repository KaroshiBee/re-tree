#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import sys


# In[2]:


from py_mini_racer import py_mini_racer as mr


# In[3]:


def babel_transform(es_string):
    """ Transform the provided string using babel.transform """

    path_to_babel = os.path.join('/home/wyn/dev/PyMiniRacer', 'tests',
                                 'fixtures', 'babel.js')

    es6 = '[1,2,3].map(n => n + 1);'

    babel_source = open(path_to_babel, "r").read()

    # Initializes PyMiniRacer
    ctx = mr.MiniRacer()

    # Parse babel
    ctx.eval("""var self = this; %s """ % babel_source)

    # Transform stuff :)
    val = "babel.transform(`%s`)['code']" % es_string
    res = ctx.eval(val)
    return res


# In[4]:


# In[5]:



# In[6]:



# In[7]:


def evalJsBabel(ctx, js):
    js = babel_transform(js)
    # print(js)
    return ctx.eval(js)    


# In[8]:


def evalJs(ctx, js):
    #print(js)
    return ctx.eval(js)


# In[9]:


def evalJsFile(ctx, fname):
    with open(fname) as f:
        return evalJs(ctx, f.read())


# In[10]:




# In[11]:





if __name__ == "__main__":
    import pudb; pu.db
    ctx = mr.MiniRacer()
    ctx.heap_stats()

    ctx.eval("var x = {company: 'Sqreen'}; x.company")

    ctx.eval('x.company')

    evalJsFile(ctx, "./Path.bundle.js")


    ctx.eval("T")

    ctx.heap_stats()

