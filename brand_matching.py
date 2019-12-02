#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import os, glob
import datetime

from difflib import SequenceMatcher

import jellyfish as jf

import logging


# In[18]:


#Functions to calculate matching score. Scores are normalized to [0,1] for comparison
def matchscoreRatcliff(str1, str2):
    return 0.0 if (pd.isnull(str1) | pd.isnull(str2)) else format(SequenceMatcher(None, str1, str2).ratio(), '.3f') 
#convert Damerau distance to similarity
def matchscoreDamerau_levenshtein(str1, str2):
    return 0.0 if (pd.isnull(str1) | pd.isnull(str2)) else format(1.0 - jf.damerau_levenshtein_distance(str1, str2), '.3f')

#Jaro_w is similarity
def matchscoreJaro_winkler(str1, str2):
    return 0.0 if (pd.isnull(str1) | pd.isnull(str2)) else format(jf.jaro_winkler(str1, str2), '.3f') 

#customized Hamming to be similarity in [0,1]
def matchscoreHamming(str1, str2):
    return 0.0 if (pd.isnull(str1) | pd.isnull(str2)) else format(1.0 - abs(jf.hamming_distance(str1, str2))/max(len(str1), len(str2)), '.3f') 
    
def matchlist(matchfunc, instr, strlist):
    return list(map(lambda x: matchfunc(instr, x), strlist))

#determining best match from article description match and subbrand description match 
def best_match(desc_match_score, subbrand_match_score) :
    if (((desc_match_score is None) | (len(desc_match_score) == 0)) & ((subbrand_match_score is None) | (len(subbrand_match_score) == 0))):
        return ("", 0.0, "No match")
    #desc_match is missing or no element
    if ((desc_match_score is None) | (len(desc_match_score) == 0)):
        return (subbrand_match_score.iloc[0].subbrand, subbrand_match_score.iloc[0].subbrand_score, "No desc match, use subbrand match")
    #subbrand_match is missing or no element
    if ((subbrand_match_score is None )| (len(subbrand_match_score) == 0)):
        return (desc_match_score.iloc[0].subbrand, desc_match_score.iloc[0].desc_score, "No subbrand desc match, use desc match")
    
    #top match for each matching type
    best_subbrand_match = subbrand_match_score.iloc[0]
    best_desc_match = desc_match_score.iloc[0]

    if (not pd.isnull(best_desc_match.subbrand)): #& (best_desc_match.desc_score >= best_subbrand_match.subbrand_score)) :
        return (best_desc_match.subbrand, best_desc_match.desc_score, best_desc_match.desc, "Desc match")
    else :
        return (best_subbrand_match.subbrand, best_subbrand_match.subbrand_score, "Subbrand desc match")

##retrieve top match for each matching method
##inputs: 
#match_score : match_score data frame, storing all scores of source desc with other desc
#subbrand_col : column in match_score indicating subbrand result
#score_col : column in match_score indicating score
#desc_col : column in match_score indicating description used for calculating score
def get_top_match(match_score, rank_col, subbrand_col, score_col, desc_col):
    if ((match_score is None) | (len(match_score) == 0)):
        return "No top match"
    else :
        top_match = match_score[match_score[rank_col] == 1]
        return (top_match.iloc[0][subbrand_col], top_match.iloc[0][score_col], top_match.iloc[0][desc_col])

##revision 2 logic : return match if both top match from desc_match and subbrand_match are the same
#check if 2 top_match tuples returned by get_top_match points to the same subbrand
def check_match_agreement(top_match_desc, top_match_subbrand) :
    if (((top_match_desc is None) | (len(top_match_desc) == 0)) | ((top_match_subbrand is None) | (len(top_match_subbrand) == 0))):
        return 'False'
    #if match result is not in form of combination (subbrand_col, score_col, desc_col)
    if ( (type(top_match_desc) != type(())) | (type(top_match_subbrand) != type(()))):
        return 'False'
    try:
        return top_match_desc[0] if (top_match_desc[0] == top_match_subbrand[0]) else "False"
    except :
        return 'False'
    
class Article:
    def __init__(self, idx, brand, desc, desc_match_score, subbrand_match_score):
        self.idx = idx
        self.brand = brand
        self.desc = desc
        self.desc_match_score = desc_match_score
        self.subbrand_match_score = subbrand_match_score
        self.subbrand_res = None
        self.subbrand_text = None
        self.desc_subbrand_agreement_Ratcliff = None
        self.desc_subbrand_agreement_Jaro_winkler = None
        self.match_desc_Ratcliff = None
        self.match_subbrand_Ratcliff = None
        #self.match_desc_Damerau_levenshtein = None
        #self.match_subbrand_Damerau_levenshtein = None
        self.match_desc_Jaro_winkler = None
        self.match_subbrand_Jaro_winkler = None
        self.match_desc_Hamming = None
        self.match_subbrand_Hamming = None


# In[19]:


PROJECT_PATH = '/data/data1/brand_poc/'
OUTPUT_FILENAME = 'output/' + 'subbrand_out_full' + datetime.datetime.now().strftime("%Y%m%d-%H") + '.xlsx'


# In[41]:


# Added by Parakram
# Feedback Logic implementation
# Creating empty dataframe
df_all = pd.DataFrame()

#read all the files in the feedback folder; all the files should have same layout
for f in glob.glob(os.path.join(PROJECT_PATH,"feedback/*.xlsx")):
    df = pd.read_excel(f, 'Sheet1')
    df_all = df_all.append(df)
#print(df_all.head())


# In[44]:


# Added by Parakram
# Feedback Logic implementation - (Contd..)
# Get only the records with feedback value RN ("Rejected Not needed")
df_filtered = df_all[df_all['Feedback'] == 'RN']

# Check if all the records are reviewed and feedback provided
len(df_all) == df_all.Feedback.count()

# Read the master article exception file
article_exception_df = pd.read_excel(os.path.join(PROJECT_PATH,"article_exception/article_exception_file.xlsx"))

# Append new RN ("Rejected Not needed") records from recent review to the master file
# keep only unique records in this file
article_exception_df = article_exception_df.append(df_filtered[['SAP_Article_Number', 'SAP_GTIN']]).drop_duplicates()

# Save article_exception file
article_exception_file = pd.ExcelWriter(os.path.join(PROJECT_PATH, "article_exception/article_exception_file.xlsx"))
article_exception_df.to_excel(article_exception_file,'Sheet1', index=False)
article_exception_file.save()


# In[46]:


# Modified by Parakram
#Load reference files
df_cat = pd.read_excel(os.path.join(PROJECT_PATH, 'reference_data/Category.xlsx'))
df_brandref = pd.read_excel(os.path.join(PROJECT_PATH, 'reference_data/ZMD_SUBBRAND_MAP.XLSX'))

# Load all input files placed in input folder
df_item = pd.DataFrame()
for f in glob.glob(os.path.join(PROJECT_PATH,"input_data/*.xlsx")):
    main_df = pd.read_excel(f)
    df_item = df_item.append(main_df)

#df_item = pd.read_excel(os.path.join(PROJECT_PATH, 'input_data/tvDCAttributes_SAP_GS1_Classifying_Article.xlsx'))
#df_UPC = pd.read_csv(os.path.join(DATA_PATH, 'source2.csv')) #na_values = ''


# In[64]:


# Filter the df_item dataframe to remove all articles present in exception list
df_item['SAP_Article_Number'] = pd.to_numeric(df_item['SAP_Article_Number'], errors='ignore')
df_item['SAP_GTIN'] = pd.to_numeric(df_item['SAP_GTIN'], errors='ignore')

df_item = df_item.loc[~df_item['SAP_Article_Number'].isin(article_exception_df['SAP_Article_Number'])]
df_item = df_item.loc[~df_item['SAP_GTIN'].isin(article_exception_df['SAP_GTIN'])]


# In[48]:


df_brandref.rename(columns= {'SUB-Brand':'Subbrand', 'Language Key':'LanguageKey','Sub Brand Name': 'Subbrand_name'} , inplace = True)
df = df_item.loc[:,['SAP_Article_Number', 'SAP_Article_Description', 'CPMS_Descr', 'SAP_MCH0', 'SAP_MCH0_Descr', 'SAP_Brand', 'SAP_Brand_Description','CPMS_Reporting_Brand', 'SAP_Sub_Brand', 'SAP_Sub_Brand_Description','CPMS_Brand','GS1_Brand_EN']]


# In[66]:


#Start logger
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
logging.basicConfig(filename=os.path.join(PROJECT_PATH, 'output/subbrand_log.log'), 
                    filemode='w+',
                    level=logging.INFO) #default level is warning only. overwrite old report

logger = logging.getLogger()
logger.info('Start logging at ' + str(datetime.datetime.now()))


# In[67]:


#Replace empty strings as missing values and Clean empty spaces
df.replace(r'^\s+$', np.nan, regex=True, inplace=True)
df.replace(r'\s+', ' ', regex=True, inplace=True)

#Convert all to upper for consistency
df = df.apply(lambda x: x.str.upper())
df_brandref = df_brandref.apply(lambda x: x.str.upper())


# In[68]:


#List of all brands
brandlist_all = df.SAP_Brand.unique()


# In[69]:


#Articles in brands having no subbrand for matching-> use subbrand matching instead
#These brands all have empty subbrand information, time-consuming and give no result in case of using desc_match
#brandlist_except to be removed if these brands no longer have empty subbrands
brandlist_except = ['UNGM','UNBR','JOE','P','SLD','LH','ESS','N']
#brandlist = [x for x in brandlist_all if x not in brandlist_except]

####test sample####
top_n = 1
#brandlist = ['DANO', '7UP','REGL','DOLE','UNIC','VOGU','LBRS']
brandlist = ['7UP', 'AVEE','REGL','DOLE' ]
####end test####

brand_dict = {}

logger.info('Brand list :' + ','.join(str(b) for b in brandlist_all))
logger.info('Brand count :' + str(len(brandlist_all)))
start_time_all = datetime.datetime.now()
logger.info('Start computing matching score at' + str(start_time_all))


logger.info('------------------------------------------------------------------')

#for brand in brandlist_all[:top_n]:
for brand in brandlist:
#for brand in brandlist_all:
    #print(brand)
    logger.info('\n############################################################\n')
    logger.info('Start computing for brand ' + str(brand))
    start_time = datetime.datetime.now()
    logger.info('Start time brand : ' + str(start_time))
    df_brand = df[df.SAP_Brand == brand]#.loc[:,['SAP_Article_Description', 'CPMS_Descr', 'SAP_MCH0', 'SAP_MCH0_Descr', 'SAP_Brand', 'SAP_Brand_Description','CPMS_Reporting_Brand', 'SAP_Sub_Brand', 'SAP_Sub_Brand_Description']]
    df_subbrand = df_brandref[df_brandref.Brand == brand] #all subbrands under this brand

    #result series
    desc_res = []
    df_no_subbrand = df_brand[pd.isnull(df_brand.SAP_Sub_Brand_Description)]
    
        
    #for desc in df_no_subbrand.SAP_Article_Description:
    for idx in df_no_subbrand.index:
        desc = df_no_subbrand.loc[idx].SAP_Article_Description
        logger.info('Current description :' + str(desc) + ' , starts at : ' + str(datetime.datetime.now()))
        
        #category of this idx:
        current_cat = df_cat[df_cat['SAP_MCH0'] == df_no_subbrand.loc[idx].SAP_MCH0].MCH2.tolist()
        #business request: check with all other even empty or not. But filter first by category, only those of same category will be compared
        #In original all df_brand, those falling within the category, ignoring the current item
        df_brand_others = df_brand[(df_brand.index != idx) & (df_brand['SAP_MCH0'].isin(df_cat[df_cat['MCH2'].isin(current_cat)].SAP_MCH0))]
    
        ##For those brand in exception list, strip to single element to avoid time-consuming analysis and to use subbrand match#####
        if (brand in brandlist_except) : 
            df_brand_others =df_brand_others.loc[:1]
            
        #score for article desc
        #desc_scores = matchlist(desc, df_brand_others.SAP_Article_Description)
        #score for CPMS desc
        #CPMS_scores = matchlist(desc, df_brand_others.CPMS_Descr)
        #Score for different metric
        desc_scores_Ratcliff = matchlist(matchscoreRatcliff, desc,df_brand_others.SAP_Article_Description)
        desc_scores_Jaro_winkler = matchlist(matchscoreJaro_winkler, desc, df_brand_others.SAP_Article_Description)
        desc_scores_Hamming = matchlist(matchscoreHamming, desc, df_brand_others.SAP_Article_Description)
        #desc_scores_Damerau_levenshtein = matchlist(matchscoreDamerau_levenshtein, desc, df_brand_others.SAP_Article_Description)
        CPMS_scores_Ratcliff = matchlist(matchscoreRatcliff, desc, df_brand_others.CPMS_Descr)
        CPMS_scores_Jaro_winkler = matchlist(matchscoreJaro_winkler, desc, df_brand_others.CPMS_Descr)
        CPMS_scores_Hamming = matchlist(matchscoreHamming, desc, df_brand_others.CPMS_Descr)
        #CPMS_scores_Damerau_levenshtein = matchlist(matchscoreDamerau_levenshtein, desc, df_brand_others.CPMS_Descr)
        
        
        desc_match_score = pd.DataFrame({'desc' : df_brand_others.SAP_Article_Description, 'CPMS_desc' : df_brand_others.CPMS_Descr,'subbrand': df_brand_others.SAP_Sub_Brand_Description,                                         'desc_score' : desc_scores_Ratcliff, 'CPMS_score' : CPMS_scores_Ratcliff,                                         'desc_scores_Ratcliff' : desc_scores_Ratcliff, 'CPMS_scores_Ratcliff' : CPMS_scores_Ratcliff,                                        'desc_scores_Jaro_winkler' : desc_scores_Jaro_winkler, 'CPMS_scores_Jaro_winkler' : CPMS_scores_Jaro_winkler,                                         'desc_scores_Hamming' : desc_scores_Hamming, 'CPMS_scores_Hamming' : CPMS_scores_Hamming})
                                        #'desc_scores_Damerau_levenshtein' : desc_scores_Hamming, 'CPMS_scores_Damerau_levenshtein' : CPMS_scores_Hamming
        
        #sorting by score, with higher priority for those with subbrand info
        ##ALL OTHER SCORES
        desc_match_score.sort_values(by=['desc_scores_Jaro_winkler', 'subbrand'],ascending=[False, True], na_position='last', inplace = True)
        desc_match_score['desc_rank_Jaro_winkler']=(desc_match_score.reset_index().index+1)
        desc_match_score.sort_values(by=['desc_scores_Hamming', 'subbrand'],ascending=[False, True], na_position='last', inplace = True)
        desc_match_score['desc_rank_Hamming']=(desc_match_score.reset_index().index+1)
        #skip CPMS score for now
        #desc_match_score.sort_values(by=['CPMS_score', 'subbrand'],ascending=[False, True], na_position='last', inplace = True)
        #desc_match_score['CPMS_rank']=(desc_match_score.reset_index().index + 1)
        desc_match_score.sort_values(by=['desc_score', 'subbrand'],ascending=[False, True], na_position='last', inplace = True)
        desc_match_score['desc_rank']=(desc_match_score.reset_index().index+1)
        desc_match_score.sort_values(by=['desc_rank'],inplace=True)
        
        #print(desc_match_score)
        #match with subbrand name in df_brand. Irrespective of cat -> should not use those filtered by cat
        #sub_scores = matchlist(desc, df_subbrand.Subbrand_name)
        
        sub_scores_Ratcliff = matchlist(matchscoreRatcliff,desc, df_subbrand.Subbrand_name)
        sub_scores_Jaro_winkler = matchlist(matchscoreJaro_winkler,desc, df_subbrand.Subbrand_name)
        sub_scores_Hamming = matchlist(matchscoreHamming,desc, df_subbrand.Subbrand_name)
        #sub_scores_Damerau_levenshtein = matchlist(matchscoreDamerau_levenshtein,desc, df_subbrand.Subbrand_name)
        
        subbrand_match_score = pd.DataFrame({'subbrand' : df_subbrand.Subbrand_name, 'subbrand_score' : sub_scores_Ratcliff, 'subbrand_score_Ratcliff' : sub_scores_Ratcliff,                                             'subbrand_score_Jaro_winkler' : sub_scores_Jaro_winkler, 'subbrand_score_Hamming' : sub_scores_Hamming})
                                            #'subbrand_score_Damerau_levenshtein' : sub_scores_Damerau_levenshtein})
        ##ALL OTHER SCORES
        subbrand_match_score.sort_values(by=['subbrand_score_Jaro_winkler'], ascending = [False], na_position = 'last', inplace=True)
        subbrand_match_score['rank_Jaro_winkler'] = (subbrand_match_score.reset_index().index +1 )
        subbrand_match_score.sort_values(by=['subbrand_score_Hamming'], ascending = [False], na_position = 'last', inplace=True)
        subbrand_match_score['rank_Hamming'] = (subbrand_match_score.reset_index().index +1 )
        
        subbrand_match_score.sort_values(by=['subbrand_score'], ascending = [False], na_position = 'last', inplace=True)
        subbrand_match_score['rank'] = (subbrand_match_score.reset_index().index +1 )

        article = Article(idx, brand, desc, desc_match_score, subbrand_match_score)
        #Results
        desc_res.append(article)
        logger.info('End at : ' + str(datetime.datetime.now()))
    #composite key for (cat, brand)    
    brand_dict[brand] = pd.Series(desc_res)
    end_time = datetime.datetime.now()
    logger.info('End time brand ' + str(brand) + ' : ' + str(end_time) + ". Total time (mins): " + str((end_time - start_time)//60) )
    logger.info('\n############################################################\n')

end_time_all = datetime.datetime.now()
logger.info('End computing matching score at ' +  str(end_time_all) + ". Total time (mins): " + str((end_time_all - start_time_all)//60) )


# In[70]:


#calculate best match
logger.info('Analyzing all distances for best match at :' + str(datetime.datetime.now()))
res_list = []
#for brand in brandlist_all[:top_n]:
for brand in brandlist:
#for brand in brandlist_all:
    for article in brand_dict[brand] :
        article.subbrand_res = best_match(article.desc_match_score, article.subbrand_match_score)
        article.subbrand_text = article.subbrand_res[0] #do not convert to txt to keep NaN
        
        article.match_desc_Ratcliff = get_top_match(article.desc_match_score, 'desc_rank', 'subbrand', 'desc_score', 'desc')
        article.match_subbrand_Ratcliff = get_top_match(article.subbrand_match_score, 'rank', 'subbrand', 'subbrand_score', 'subbrand')
        article.match_desc_Jaro_winkler = get_top_match(article.desc_match_score, 'desc_rank_Jaro_winkler',  'subbrand', 'desc_scores_Jaro_winkler', 'desc')
        article.match_subbrand_Jaro_winkler = get_top_match(article.subbrand_match_score, 'rank_Jaro_winkler', 'subbrand', 'subbrand_score_Jaro_winkler', 'subbrand')
        article.match_desc_Hamming = get_top_match(article.desc_match_score, 'desc_rank_Hamming',  'subbrand', 'desc_scores_Hamming', 'desc')
        article.match_subbrand_Hamming = get_top_match(article.subbrand_match_score, 'rank_Hamming', 'subbrand', 'subbrand_score_Hamming', 'subbrand')
        
        #check agreement between desc match and subbrand match
        article.desc_subbrand_agreement_Ratcliff = check_match_agreement(article.match_desc_Ratcliff, article.match_subbrand_Ratcliff)
        article.desc_subbrand_agreement_Jaro_winkler = check_match_agreement(article.match_desc_Jaro_winkler, article.match_subbrand_Jaro_winkler)
        #1 dict for each item, then append to final list
        res_article = {'idx':article.idx, 'brand':article.brand, 'desc':article.desc, 'seq_sub_brand_out': article.subbrand_text, 'seq_sub_brand_res': article.subbrand_res,                       'desc_subbrand_agreement_Ratcliff':article.desc_subbrand_agreement_Ratcliff,'desc_subbrand_agreement_Jaro_winkler':article.desc_subbrand_agreement_Jaro_winkler,                      'match_desc_Ratcliff':article.match_desc_Ratcliff,'Parallel_sub_brand_1_out':(article.match_desc_Ratcliff)[0],'match_subbrand_Ratcliff':article.match_subbrand_Ratcliff,                      'Parallel_sub_brand_2_out':(article.match_subbrand_Ratcliff)[0],'match_desc_Jaro_winkler':article.match_desc_Jaro_winkler, 'match_subbrand_Jaro_winkler':article.match_subbrand_Jaro_winkler,                      'match_desc_Hamming':article.match_desc_Hamming, 'match_subbrand_Hamming':article.match_subbrand_Hamming}
        res_list.append(res_article)
res = pd.DataFrame(res_list, columns = ['idx','brand','desc','seq_sub_brand_out','seq_sub_brand_res', 'desc_subbrand_agreement_Ratcliff','Parallel_sub_brand_1_out','match_desc_Ratcliff','Parallel_sub_brand_2_out','match_subbrand_Ratcliff',                                       'desc_subbrand_agreement_Jaro_winkler', 'match_desc_Jaro_winkler', 'match_subbrand_Jaro_winkler','match_desc_Hamming','match_subbrand_Hamming'])

logger.info('Finish analyzing all distances for best match at :' + str(datetime.datetime.now()))


# In[71]:


#consolidate with original data
df_res = pd.merge(df_item.reset_index(), res, left_on = 'index', right_on = 'idx', how = 'left').set_index(df_item.index)

col_out = df_item.columns.tolist()

#insert result after column SAP_Sub_Brand_Description
ins_index = col_out.index("SAP_Sub_Brand_Description")
#result columns to insert
col_additional = ['subbrand_text','subbrand_res','desc_subbrand_agreement_Ratcliff', 'match_desc_Ratcliff','match_subbrand_Ratcliff','desc_subbrand_agreement_Jaro_winkler', 'match_desc_Jaro_winkler', 'match_subbrand_Jaro_winkler',           'match_desc_Hamming', 'match_subbrand_Hamming']
for idx in range(0,len(col_additional)):
    col_out.insert(ins_index + idx +1, col_additional[idx])

# logger.info('Saving to Excel at :' + str(datetime.datetime.now()))
# subbrand_out_file = pd.ExcelWriter(os.path.join(PROJECT_PATH, OUTPUT_FILENAME))
# df_res[col_out].to_excel(subbrand_out_file,'Sheet1', index=False)
# subbrand_out_file.save()
# logger.info('Finish saving at :' + str(datetime.datetime.now()))

# Added by Parakram for selected column
logger.info('Saving selected column to Excel at :' + str(datetime.datetime.now()))
subbrand_out_file = pd.ExcelWriter(os.path.join(PROJECT_PATH, OUTPUT_FILENAME))

#Creating feedback column for users to fill in
df_res['Feedback'] = ''
df_res['SAP_GTIN'] = df_res['SAP_GTIN'].astype(str)
col_out1 = ['SAP_Article_Number', 'SAP_GTIN', 'SAP_Article_Description', 'CPMS_Descr', 'SAP_MCH0', 'SAP_MCH0_Descr', 'SAP_Brand', 'SAP_Brand_Description', 'seq_sub_brand_out','seq_sub_brand_res', 'Parallel_sub_brand_1_out','match_desc_Ratcliff','Parallel_sub_brand_2_out','match_subbrand_Ratcliff','Feedback']

df_res[col_out1].to_excel(subbrand_out_file,'Sheet1', index=False)
subbrand_out_file.save()
logger.info('Finish saving selected column to excel at :' + str(datetime.datetime.now()))


# In[82]:


# This will save all columns to the file
# subbrand_out_file = pd.ExcelWriter(os.path.join(PROJECT_PATH, OUTPUT_FILENAME))
# df_res.to_excel(subbrand_out_file,'Sheet1', index=False)
# subbrand_out_file.save()


# In[80]:


df_res.head()


# In[ ]:


brand_dict['AVEE'][].desc_subbrand_agreement_Ratcliff


# In[77]:


#brand_dict['7UP'][1].desc
brand_dict['7UP'][1].desc_match_score


# In[20]:


for keys, values in brand_dict.items():
    print(keys)


# In[ ]:


n=2
brand = 'UNGM'
print(brand_dict[brand][n].match_desc_Ratcliff)
print(brand_dict[brand][n].match_subbrand_Ratcliff)
print(brand_dict[brand][n].match_desc_Ratcliff[0])
print(brand_dict[brand][n].match_subbrand_Ratcliff[0])
#.values[0] if (brand_dict['AVEE'][n].match_desc_Ratcliff[0].values[0] == brand_dict['AVEE'][n].match_subbrand_Ratcliff[0].values[0]) else "False"


# In[55]:


(res.match_desc_Ratcliff[1])[0]


# In[1]:


get_ipython().system('jupyter nbconvert --to script brand_matching.ipynb')


# In[ ]:




