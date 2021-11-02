from simple_salesforce import Salesforce, format_soql
# from pprint import pprint
# import json
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
# import numpy as np

sf = Salesforce(username="reale360dm@ceptes.com",
                password="ceptes@123",
                organizationId='00D4x000002z6ij')

# SOQL = "SELECT AccountName__c, Comments__c FROM Inquiry__c"
# data = sf.query(SOQL)
data = [{'AccountName__c': f"Bulk Test {i}"} for i in range(0, 1000)]
SOQL = format_soql("SELECT AccountName__c, Comments__c FROM Inquiry__c", "Bulk Test")
the_accounts = sf.bulk.Inquiry__c.query(SOQL)
# pprint(the_accounts)
df = pd.DataFrame(the_accounts)
print(df.head(10))


def word_cloud_func(df):
    word_cloud = WordCloud(
        background_color='black',
        stopwords=set(STOPWORDS),
        max_words=50,
        max_font_size=40,

    ).generate(str(df))
    fig = plt.figure(
        figsize=(10, 10),
        facecolor='k',
        edgecolor='k')
    plt.axis('off')

    fig.subplots_adjust(right=0.77)
    plt.imshow(word_cloud)
    plt.show()


print(word_cloud_func(df['Comments__c']))
