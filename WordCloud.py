import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image

airlines = pd.read_csv('combined.csv')

#change to lower case
airlines['lemmatized'] = airlines['text'].str.lower()

# remove punctuation and urls
airlines['lemmatized'].replace(to_replace=r"[^\w\d'\s]",value='',regex=True, inplace=True)

#remove numbers
airlines['lemmatized'].replace(to_replace=r"\d+", value='',regex=True, inplace=True)

# tokenize the text by splitting (leaving apostrophe to be used in remove stop words)
airlines['lemmatized'] = airlines['lemmatized'].str.split()

#remove stop words
add = ["i'm", "i've","airlines","airline","flight","united","amp","u","im","ua","pm","ual","spotted","boeing",
       "mi","away","unknown"]
to_remove = (stopwords.words("english")) + add
airlines['lemmatized'] = airlines['lemmatized'].apply(lambda x: [item for item in x if item not in to_remove])

#remove apostrophes
airlines['lemmatized'].replace(to_replace="'", value = '', inplace = True, regex = True)

# Stem the text

lemmatizer = WordNetLemmatizer()

def lem_text(text):
    return [lemmatizer.lemmatize(w) for w in text]

airlines['lemmatized'] = airlines['lemmatized'].apply(lem_text)

airlines['clean'] = airlines['lemmatized'].apply(' '.join)

# Generate a word cloud image
mask = np.array(Image.open("airplane.png"))
plane_text = " ".join(review for review in airlines.clean) 
wordcloud_plane = WordCloud(background_color="white", mode="RGBA", max_words=1000, width=1600, height=800, mask=mask).generate(plane_text)

# create coloring from image
image_colors = ImageColorGenerator(mask)
plt.figure(figsize=[20,10])
plt.imshow(wordcloud_plane.recolor(colormap='cividis'), interpolation="bilinear")
plt.axis("off")
plt.savefig('wordcloud.png')
plt.show()