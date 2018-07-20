#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 10:21:43 2018

@author: jbotbol
"""

"""
 The main idea is that you sometimes see in url_image information about a date
 which may be the date where the product were uploaded online or something like
 that. It is an important information regarding the label we want to predict. 
 Late products are more likely to have been sold early since they can be
 evaluated, which means they were sold in a short period. In the case the date is
 present, we can extract it as a floating point.
 We must notice that best solutions generally used this information without 
 knowing it (including me when uploading my model with a loss of 0.89968), 
 because we used LabelEncoding with this feature which begins by alphabetically
 sorting all the categories, which often resulted in putting 
 together urls with close dates next one to the other
 (but not always because of the format of the date and also things that could be
 written before the date information). Thus, url_image happened to be the most 
 important feature in many models, and that's what caught my attention to 
 analyze why it was the case.
 These transformations can help to have a gain of ~0.01 in log-loss.
 However, regarding the objective of the mission of Label Emmaus, the url 
 should not be used this way because it gives information about the label for 
 this data but not for new data where we don't know yet when it will be sold.
 There was also another pattern in the url that was shared by some products 
 which may be linked to the nature of the products (like 56/2994, 56/3044) which
 can also be extracted.
 Finally, the first word of "nom_produit" was generally the most important one,
 and simple preprocessing + stemming could also putting together the same products.
"""
 
from nltk.stem.snowball import FrenchStemmer 

#We perform the transformation of the url in 2 steps
def transfFirst(url):
    if type(url)!=unicode:
        return u"missing"
    url = url.split(u'/')[5:]
    if url[0]==u'56':
        return url[1]
    if url[0]==u'None':
        reste = url[2]
        if '201' in reste:
            indice = reste.index('201')
            reste = reste[indice:(indice+8)]
            try:
                int(reste)
                if int(reste[3])<6:
                    return u'missing'
                return reste
            except:
                return u'missing' 
        elif '16' in reste or '17' in reste or '18' in reste:
            indice = reste.index(u'16') if u'16' in reste else (reste.index(u'17') if u'17' in reste else reste.index(u'18'))
            reste = reste[indice-4:(indice+2)]
            try: 
                int(reste)
                reste = u'20'+reste[-2:] + reste[2:4] + reste[:2]
                return reste
            except: return u"missing"

#final step which call the first step
def transf(url):
    url = transfFirst(url)
    if url is None:
        return u"missing"
    if url==u"missing":
        return u"missing"
    elif len(url)!=8:
        return url
    url = str(url)
    anneeenmois = 12*(int(url[:4]) - 2016)
    mois = int(url[4:6]) - 1
    jourenmois = (float(url[6:8])-1)/31
    if mois>12:
        return u"missing"
    if jourenmois>1:
        return u"missing"
    if int(url[:4])>2018:
        return u"missing"
    if anneeenmois==24 and mois>4:
        return u"missing"
    return anneeenmois + mois + jourenmois
    
        
st = FrenchStemmer()
def transfNameProduct(s):
    if type(s)!=float:
        s= s.lstrip().lower()
        for uselessword in [u'le ', u'les ', u'la ', u'des ', u'de ', u'un ']:
            s = s.replace(uselessword, u'')
        s = s.split(u' ')[0]
        if len(s)>0 and s[-1] in [u'"', u'&', u"'", u',', u'-', u'.', u'/']:
            s = s[:-1]
        return st.stem(s)
    else:
        return u'missing'


# =============================================================================
# Things to add in the transformations of the initial datasets : 
# =============================================================================
#for data in [train, test]:
#    data['url_image'] = data['url_image'].map(transf)
#    data['url_date'] = data['url_image'].map(lambda s: s if type(s) is float else np.nan)
#    data['url_other'] = data['url_image'].map(lambda s: s if type(s) is unicode else u'missing')
#    data['nom_produit'] = data['nom_produit'].map(transfNameProduct)
        
#Finally, url_date and name_produit can be used to replace the url_image and 
#initial nom_produit. The 2 other new features seemed to be less useful.
