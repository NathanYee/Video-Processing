
# coding: utf-8

# This is a one time use notebook to count an process result data to make nice graphs of my results

# In[1]:

test_imgs ={'BENTHOCODON': 286,
 'CYSTECHINUS_LOVENI': 40,
 'ECHINOCREPIS': 26,
 'ELPIDIA': 13,
 'FUNGIACYATHUS_MARENZELLERI': 13,
 'LONG_WHITE': 3,
 'ONEIROPHANTA_MUTABILIS_COMPLEX': 3,
 'PENIAGONE_PAPILLATA': 10,
 'PENIAGONE_SP_1': 2,
 'PENIAGONE_SP_2': 1,
 'PENIAGONE_SP_A': 453,
 'PENIAGONE_VITRAE': 93,
 'SCOTOPLANES_GLOBOSA': 63,
 'SYNALLACTIDAE': 5,
 'TJALFIELLA': 66,
 'bg': 0}


# In[2]:

train_imgs = {'BENTHOCODON': 569,
 'CYSTECHINUS_LOVENI': 174,
 'ECHINOCREPIS': 82,
 'ELPIDIA': 493,
 'FISH': 8,
 'FUNGIACYATHUS_MARENZELLERI': 64,
 'LONG_WHITE': 8,
 'ONEIROPHANTA_MUTABILIS_COMPLEX': 6,
 'PENIAGONE_PAPILLATA': 14,
 'PENIAGONE_SP_1': 111,
 'PENIAGONE_SP_2': 12,
 'PENIAGONE_SP_A': 1108,
 'PENIAGONE_VITRAE': 360,
 'SCOTOPLANES_GLOBOSA': 365,
 'SYNALLACTIDAE': 30,
 'TJALFIELLA': 230,
 'bg': 0}


# In[13]:

sum([train_imgs[key] for key in train_imgs.keys()])


# In[3]:

imagenet_ap = {'BENTHOCODON': 0.805137016516,
'ONEIROPHANTA_MUTABILIS_COMPLEX': 0.458815192744,
'SCOTOPLANES_GLOBOSA': 0.899604662246,
'PENIAGONE_PAPILLATA': 0.7725,
'PENIAGONE_SP_1': 0.0206598918637,
'ELPIDIA': 0.0442176870748,
'ECHINOCREPIS': 0.42133689736,
'LONG_WHITE': 0.2,
'CYSTECHINUS_LOVENI': 0.590778912159,
'TJALFIELLA': 0.494639502854,
'PENIAGONE_VITRAE': 0.292665667963,
'PENIAGONE_SP_2': 0.166666666667,
'SYNALLACTIDAE': 0.821111111111,
'PENIAGONE_SP_A': 0.978279800281,
'FUNGIACYATHUS_MARENZELLERI': 0.386287047543}


# In[4]:

most_epoch_ap = {'CYSTECHINUS_LOVENI': 0.643499906799,
'ONEIROPHANTA_MUTABILIS_COMPLEX': 0.248599910394,
'SCOTOPLANES_GLOBOSA': 0.948805921186,
'PENIAGONE_PAPILLATA': 1.0,
'PENIAGONE_SP_1': 0.0500641025641,
'ELPIDIA': 0.102745995423,
'ECHINOCREPIS': 0.786982162631,
'LONG_WHITE': 0.183501683502,
'BENTHOCODON': 0.757451612353,
'TJALFIELLA': 0.389716451493,
'FUNGIACYATHUS_MARENZELLERI': 0.424597600764,
'PENIAGONE_SP_2': 0.166666666667,
'SYNALLACTIDAE': 0.627380952381,
'PENIAGONE_SP_A': 0.987186066252,
'PENIAGONE_VITRAE': 0.376280487988}


# In[5]:

keys = set(most_epoch_ap.keys()) & set(imagenet_ap.keys()) & set(test_imgs.keys()) & set(train_imgs.keys())


# In[6]:

print(" ,Number of Training Images, Number of Testing Images, Imagenet AP, Most Epoch AP")
for key in keys:
    num_train = train_imgs[key]
    num_test  = test_imgs[key]
    imgnet_ap = imagenet_ap[key]
    max_epch_ap = most_epoch_ap[key]
    print("{},{},{},{},{}".format(key, num_train, num_test, imgnet_ap, max_epch_ap))


# In[7]:

all_keys = set(most_epoch_ap.keys()) | set(imagenet_ap.keys()) | set(test_imgs.keys()) | set(train_imgs.keys())


# In[8]:

all_keys.remove('bg')


# In[9]:

list(all_keys)


# In[ ]:



