#!/usr/bin/env python
# coding: utf-8

# ## Profitable and Attractives Apps 
# 
# In this report, we'll analysis and explain datasets to help companies or anyone that works with apps building. In particular, the datasets that wil be analised are **Mobile Apps Stores - Apple** (https://www.kaggle.com/ramamet4/app-store-apple-data-set-10k-apps) and **Google Play Store Apps**(https://www.kaggle.com/lava18/google-play-store-apps), two tables from june, 2018. Our goal is explain more about free apps for occidental Audience, that to use ads as revenue source.   
# 
# We'll initiate with a quick approach how to explore these datasets; going through to find and fix data inconsistencies such as writing erros and duplicate entries. Lastly, we'll see how to conceive basic build strategies and parameters to decision making related to apps building.     
# 
# We hope that you enjoy this!
# 
# For any questions, suggestions or corrections, send me a mail or message that I'll answer with pleasure!
# 
# **e-mail:** osmancesar.mr@gmail.com
# 
# 
# **linkedin:** https://www.linkedin.com/in/osman-rodrigues/

# ### 1. Oppening and Fast Checking files and datasets
# 
# The first step we should do is open datasets files and check its first rows and columns. It's allow us to verify which data type of informations we lead.   

# In[91]:


#to export and open dataset files

opened_file_apple = open('AppleStore.csv', encoding="utf8")
opened_file_google = open('googleplaystore.csv', encoding="utf8")
from csv import reader
read_file_apple = reader(opened_file_apple)
read_file_google = reader(opened_file_google)
apps_data_apple = list(read_file_apple)
apps_data_google = list(read_file_google)


print('First rows of Apple Store Apps:',('\n'),apps_data_apple[:3])
('\n')
print('First rows of Google Store Apps:',('\n'),apps_data_google[:3])


# ### 2. Searching, idetifying and removing wrong entries
# 
# After choosing the datasets above, we took a quick read in Kaggle forum to find possibles questions about how clean these datasets are. After that, we saw a incosistency in 'Reviews' column of Google Store Apps table.     

# In[92]:


#wrong entry identified position after pre analysis in forum

data_slice = apps_data_google[10473]
print (data_slice)

#search and confirm wrong data statement 

for row in apps_data_google:
    if len(row) != len(apps_data_google[0]):
        print(row)
        print(apps_data_google.index(row))


# In[93]:


#removing wrong data

del apps_data_google[10473]


# ### 3. Exploring the datasets
# 
# To more specific analyse and measure of these datasets, we can use the function below in which the input sequence is dataset, start row, end row and the conditional statement.     

# In[94]:


#explore_dataset_function
def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]    
    for row in dataset_slice:
        print(row)
        print('\n') # adds a new (empty) line after each row

    if rows_and_columns:
        print('Number of rows:', len(dataset))
        print('Number of columns:', len(dataset[0]))
        
explore_data(apps_data_apple, 0, 1, apps_data_apple[:1])
print('\n')
explore_data(apps_data_google, 0, 1, apps_data_google[:1])


# ### 4. Searching, cleaning and separate duplicated for non-duplicated entries
# 
# Is common that large datasets have duplicated entries. But, to remove them, we need a careful analyse to find parameteres that allow us for a correctly removing. Below, some steps to help us in searching, confirm and removing duplicate entries. 

# In[95]:


#Until here, we've been cleaning up these datasets. 
#Now, we clear the duplicate entries of Android dataset.
#For instance, we print fews Instagram entries to see that 
#duplicate facts occurs:

for  app in apps_data_google:
    name = app[0]
    if name == 'Instagram':
        print(app)


# In[96]:


#To count the number of occurrences, we can use this code below:

duplicate_g_apps = []
unique_g_apps = []

for g_app in apps_data_google:
    g_name = g_app[0]
    if g_name in unique_g_apps:
        duplicate_g_apps.append(g_name)
    else:
        unique_g_apps.append(g_name)
            
duplicate_a_apps = []
unique_a_apps = []

for a_app in apps_data_apple:
    a_name = a_app[1]
    if a_name in unique_a_apps:
        duplicate_a_apps.append(a_name)
    else:
        unique_a_apps.append(a_name)
            
print('Number of duplicate Android apps: ', len(duplicate_g_apps))
print('\n')
print('Example of duplicate Android apps: ', duplicate_g_apps[:10])
print('\n')
print('Number of duplicate iOS apps: ', len(duplicate_a_apps))
print('\n')
print('Example of duplicate iOS apps: ', duplicate_a_apps[:10])

#So that we didn't equivocate randomly remove duplicate data,
#we can observe unique parameteres in the same row associeted 
#to the duplicate app entries. For example the number of reviews
#of these app.


# In[97]:


#creating a dictionary to store non-duplicate entries:

reviews_g_max = {}
for g_app in apps_data_google[1:]:
    g_name = g_app[0]
    g_n_reviews = float(g_app[3])
    
    if g_name in reviews_g_max and reviews_g_max[g_name] < g_n_reviews:
        reviews_g_max[g_name] = g_n_reviews
        
    elif g_name not in reviews_g_max:
        reviews_g_max[g_name] = g_n_reviews
        
reviews_a_max = {}
for a_app in apps_data_apple[1:]:
    a_name = a_app[1]
    a_n_reviews = float(a_app[5])
    
    if a_name in reviews_a_max and reviews_a_max[a_name] < a_n_reviews:
        reviews_a_max[a_name] = a_n_reviews

        
    elif a_name not in reviews_a_max:
        reviews_a_max[a_name] = a_n_reviews
        
print('Nº of Cleaned Google Play Store Apps: ', len(reviews_g_max))
print('Nº of Cleaned Apple Store Apps: ', len(reviews_a_max))


# In[98]:


#to remove the duplicate rows using the dictonary in technic above:

#1. creat a list to store clening apps
google_clean = [] 
g_already_added = []

#2. loop through the data sets 
for g_app in apps_data_google[1:]:
    g_name = g_app[0]
    g_n_reviews = float(g_app[3])

#3. compare row to row and separate singular and already appened entries  
    if (g_n_reviews == reviews_g_max[g_name]) and (g_name not in g_already_added):
        google_clean.append(g_app)
        g_already_added.append(g_name)

#4. do the same steps to both datasets        
apple_clean = []
a_already_added = []

for a_app in apps_data_apple[1:]:
    a_name = a_app[1]
    a_n_reviews = float(a_app[5])
    
    if (a_n_reviews == reviews_a_max[a_name]) and (a_name not in a_already_added):
        apple_clean.append(a_app)
        a_already_added.append(a_name)
        
#5. check the cleaning datasets to confirm the work done
        
print('Nº of Cleaned Google Play Store Apps: ', len(google_clean))
print(google_clean[:2])

print('Nº of Cleaned Apple Store Apps: ', len(apple_clean))
print(apple_clean[:2])


# ### 5. Entries validation
# 
# To reach the goals of this analysis, we need to validate the target Audience of each apps these datasets through the basic language used. Its means that, if the app be wrote in non-english character, it must be removed from our analysis. Another pattern is around the free apps, as stated in principle.      

# In[99]:


#using a common english character validation function

def char_valid(string):
    n_checks = 0
    for character in string:
        if ord(character) > 127:
            n_checks += 1
            if n_checks > 3:
                return False
       
    return True

#testing the function

check_1 = print(char_valid('爱奇艺PPS -《欢乐颂2》电视剧热播'))
check_2= print(char_valid('Docs To Go™ Free Office Suite'))
check_3 = print(char_valid('Instachat 😜'))


# In[100]:


#applying the character validation function on the android and apple datasets

g_apps_english = []
a_apps_english = []

for g_app in google_clean:
    g_name = g_app[0]
    if char_valid(g_name):
        g_apps_english.append(g_app)

for a_app in apple_clean:
    a_name = a_app[1]
    if char_valid(a_name):
        a_apps_english.append(a_app)

#checking results        
        
explore_data(g_apps_english, 0, 3, True)
print('\n')
explore_data(a_apps_english, 0, 3, True)


# In[101]:


#collecting free apps

g_apps_free = []

for g_row in g_apps_english:
    g_price = g_row[7]
    if g_price == '0':
        g_apps_free.append(g_row)
        
a_apps_free = []

for a_row in a_apps_english:
    a_price = a_row[4]
    if a_price == '0.0':
        a_apps_free.append(a_row)

print('Nº of Free Apps of Google Play Store: ', len(g_apps_free))
print('Nº of Free Apps of Apple Store: ',len(a_apps_free))


# ### 6. Build Strategy 
# 
# Until here, the steps which we did was for turn the datasets more clear and focused in english free user apps to use ads as revenue source. 
# 
# The next aim is to inspect the most common genres of apps of determined market. Thus, we need to build a frequency tables to direct us around the most attractive genres.
# 
# Columns to collect apps genres information:
# 
# **Google Play Store dataset - Index 9 and 1**
# 
# **Apple Store dataset - Index 11**

# In[102]:


#bulding a frequency table 

def freq_table(dataset, index):
    
    frequency_table = {}
    
    for app in dataset[1:]:
        genre = app[index]
        
        if genre in frequency_table:
            frequency_table[genre] += 1
        else:
            frequency_table[genre] = 1
    
    for key in frequency_table:
        frequency_table[key] = float((frequency_table[key]/len(dataset))*100)
    
    return frequency_table

def display_table(dataset, index):
    table = freq_table(dataset, index)
    table_display = []
    for key in table:
        key_val_as_tuple = (table[key], key)
        table_display.append(key_val_as_tuple)

    table_sorted = sorted(table_display, reverse = True)
    for entry in table_sorted:
        print(entry[1], ':', entry[0])


print('-iOS Apps Common Genres-')
print('\n')
genres_apple = display_table(a_apps_free, 11)
print('\n')
print('-Android Apps Common Genres-')
print('\n')
genres_google = display_table(g_apps_free, 9)
print('\n')
print('-Android Apps Common Categories-')
print('\n')
category_google = display_table(g_apps_free, 1)


# ### 7. Answering the questions raised
# 
# #### Analyzing the frequency table generated from the Category and Genres column of the Google Play Store dataset.
# 
# 
# - 7.1 What are the most common genres?
# 
# 
# **Answer** 
# 
# 5 most common Android Apps categories percentages (%):
# 
# Family : 18.9
# 
# Game : 9.72
# 
# Tools : 8.46
# 
# Business : 4.59
# 
# Lifestyle : 3.90
# 
# 
# - 7.2 What other patterns do you see?
# 
# 
# **Answer** 
# 
# 1. Health related apps are in 8th and 12th most commons;
# 2. Business related apps are in 4th, 6th and 7th most commons; 
# 3. Global occurrence related apps - Weather (0.8%) and Events (0.71%) - are in most low frequency.
# 
# 
# 
# #### Analyzing the frequency table generated from the Genre column of the Apple Store dataset.
# 
# 
# - 7.3 Compare the patterns you see for the Google Play Store market with those you saw for the Apple Store market.
# 
# 
# **Answer** 
# 
# 5 most common iOS Apps genres percentages (%):
# 
# Games : 58.13
# 
# Entertainment : 7.88
# 
# Photo & Video : 4.96
# 
# Education : 3.66
# 
# Social Networking : 3.26
# 
# In this sense, Android Apps seems more curvated to learning and productivity purposes and iOS Apps is more proximily of entertaiment and media content.    
# 
# - 7.4 Can you recommend an app profile based on what you found so far? Do the frequency tables you generated reveal the most frequent app genres or what genres have the most users?
# 
# 
# **Answer**
# 
# No, cause we only generated frequency tables of most builded apps and others considerations must be taken, such as number of users, rating, content rating and installs.
# 

# ### 8. Analysing another indicators
# 
# As we saw above, others considerations must be taken. For this, below we'll analyse two attraction indicators: number of intalls and rating or reviews. Its give us more precision when analyse apps genres and how genre is more installed and better evaluated, that is, which genre of apps are most observated, requested, utilized and provides better user experiences.
# 
# **Obs. 1:** Apple Store Apps dataset not have direct information about number of apps installed. Therefore, we use the total of ratings per account user.
# 
# **Obs. 2:** Google Play Store Apps dataset not have a consistent data about ratings, cause many entries in this how is Not a Number - NaN, then we use the total of Reviews per app category.

# In[111]:


#1. using a frequence table technique

def genre_freq_table(dataset, index):
    
    frequency_table = {}
    
    for app in dataset[1:]:
        genre = app[index]
        
        if genre in frequency_table:
            frequency_table[genre] += 1
        else:
            frequency_table[genre] = 1
    
    return frequency_table

genre_apple = genre_freq_table(a_apps_free, 11) #isolating app of each genre (prime genre - column 11)

#2. number of installs per genre

install_a = {}

for a_genre in genre_apple: #1st iterate(main loop)
    total_genre = 0 #store the sum of user ratings(reviews)
    len_genre = 0 #store the number of apps specific to each genre
    for a_app in a_apps_free: #2nd iterate (nested loop)
        genre_app = a_app[11]
        if genre_app == a_genre: #condition: genre in a_apps_free == genre in genre_apple(freq_table)
            a_n_ratings = float(a_app[5]) #a_apps[5] = rating_count_tot(proxy)
            total_genre += a_n_ratings #sum up users reviews of each genre
            len_genre += 1
    
    avg_ratings = total_genre/len_genre
    install_a[a_genre] = round(avg_ratings)
    

    
print('iOS apps ratings per genre:')
print('\n')
print(install_a)


# In[113]:


# using visualizations with matplotlib 

# 1. import module
import numpy as np
import matplotlib.pyplot as plt

# 2. defining a function to better visualizations in all datasets cases
def visu_gen(dataset, limit, title, x_label, y_label):

# 3. attributing referred objects
    group_data = list(dataset.values())
    group_names = list(dataset.keys())
    group_mean = np.mean(group_data)

# 4. dimensioning graphics
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.barh(group_names, group_data)
    labels = ax.get_xticklabels()
    plt.setp(labels, rotation=45, horizontalalignment='right')

# 5. add a vertical average line
    ax.axvline(group_mean, ls='--', color='r')

# 6. atribuate title and labels
    ax.title.set(y=1.05)
    ax.set(xlim=[0, limit], xlabel= x_label , ylabel= y_label,
            title= title)
    
    plt.show()


visu_gen(install_a, 100000, 'iOS Apps ratings per genre', 'Total users ratings', 'Genre')


# In[105]:


#1. using a frequence table technique

category_google = genre_freq_table(g_apps_free, 1) #isolating app of each genre (prime genre - column 1)

#2. number of installs per category

install_g = {}

for category in category_google:
    total_category = 0
    len_category = 0
    for g_apps in g_apps_free:
        category_app = g_apps[1]
        if category_app == category:
            n_installs = g_apps[5]
            n_installs = n_installs.replace(',','') #using replace built-in to fix data entries
            n_installs = n_installs.replace('+','')
            n_installs = int(n_installs)
            total_category += n_installs
            len_category += 1
    
    avg_install = total_category/len_category
    install_g[category] = round(avg_install)

    
print('iOS Apps installs per genre:')
print('\n')
print(install_g)

visu_gen(install_g, 40000000, 'Android Apps installs', 'Total installs (in tens of millions)', 'Category')


# In[106]:


#1. to gathering ratings per iOS Apps genre  

ratings_a = {}

for a_genre in genre_apple: #1st iterate(main loop)
    total_genre = 0 #store the sum of user ratings
    len_genre = 0 #store the number of apps specific to each genre
    for a_app in a_apps_free: #2nd iterate (nested loop)
        genre_app = a_app[11]
        if genre_app == a_genre: #condition: genre in a_apps_free == genre in genre_apple(freq_table)
            a_ratings = float(a_app[7]) #a_apps[7] = user_rating(proxy)
            total_genre += a_ratings #sum up user rating of each genre
            len_genre += 1
    
    avg_u_ratings = total_genre/len_genre
    ratings_a[a_genre] = round(avg_u_ratings, 1)
    
#2. to gathering reviews per Android Apps category

reviews_g = {}

for category in category_google:
    total_category = 0
    len_category = 0
    for g_apps in g_apps_free:
        category_app = g_apps[1]
        if category_app == category:
            n_reviews = g_apps[3]
            total_category += float(n_reviews)
            len_category += 1
            
    
    avg_reviews = total_category/len_category
    reviews_g[category] = round(avg_reviews)


print('Android reviews per category:')
print('\n')
print(reviews_g)
print('\n')
visu_gen(reviews_g, 1100000, 'Android Apps reviews per category', 'Total reviews', 'Category')
print('\n')
print('iOS ratings per genre:')
print('\n')
print(ratings_a)
print('\n')
visu_gen(ratings_a, 5.0, 'iOS Apps ratings per genre', 'Average ratings', 'Genre')


# ### 9. Conclusion 
# 
# After we consider other parameteres besides the apps quantity percentage per genre, such as User Conversion (total of installs) and Usability (reviews and user ratings) indicators, the decision making about apps building is better guided. Overall, the genres that did demonstrated most high or above average numbers in all evaluated indicators seem to show solid behavior in their positions.
# 
# 9.1 In **Google Play Store dataset analysis**, **Games** and **Tools** categories demonstrate good behavior, such as:
# 
# **Games**: 
# 
# - **2nd most common** category (9.72% of total), more than **15 milions of installs (120% above average)** and **3rd most reviewed** (683.524 reviews);   
# 
# **Tools**: 
# 
# - **3rd most common** category (8.46% of total), more than **10 milions of installs (53,4% above average)** and **6th most reviewed** (305.733 reviews);
# 
# 
# 9.2 In **Apple Store dataset analysis**, **Games** and **Social Networking** categories demonstrate good behavior, cause:
# 
# **Games**: 
# 
# - **1sf most common** genre (58.13% of total), more than **22.813 of reviews (27.5% below average)** and **2nd top rated** (average 4.0);   
# 
# **Social Networking**: 
# 
# - **5th most common** genre (3.26% of total), **3rd most reviewed (127% above average)** and **on average between iOS Apps** (average 3.6).

# ### 10. Final considerations
# 
# We hope that companies and anyone that want for guidance use this data analysis to help their insights and developments. Even though this article have been developed and written by just a person, all technical instructions, sources and recomendations was absorved at a pleasurably study journey during the Python for Data Science: Fundamentals course, powered by Dataquest.io company.    
# 
# For any questions, suggestions or corrections, send me a mail or message that I'll answer with pleasure!
# 
# e-mail: osmancesar.mr@gmail.com
# 
# linkedin: https://www.linkedin.com/in/osman-rodrigues/
# 
# Github: https://github.com/OsmanRodrigues
