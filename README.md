# CI-CD GitHub Actions

![1568663838814](https://user-images.githubusercontent.com/49676161/125658541-34f01210-12de-4dd5-a69a-ecebe49402c0.png)

## Disclaimer 
An online search reviewed that the automatic trigger of GitHub actions may not work at times.

## Background
![word_cloud](https://user-images.githubusercontent.com/49676161/125658667-3f0f57a8-025d-4535-84c6-501127d75961.png)
Tweets are a good reflection of public sentiment on any particular topic. As an extension to my previous [Sentiment Analysis project on United Airlines](https://github.com/kenneth-cheong/Airlines-Tweets-Sentiment-Analysis), this set of code aims to automate the processs of scraping for tweets so that we can obtain a larger set of data which translates to higher accuracy for topic modeling. 

## Process 
The python package [Twython](https://twython.readthedocs.io/en/latest/) is being used to obtain tweets. The secrets function in GitHub actions has been used to make the access the confidential Twitter keys.

## Challenges
Using Twython or any other similar packages to obtain tweets usually involves having to input the secret keys issued by Twitter. The keys have to be kept confidential or Twitter will not be too happy about it. 

Secondly, Twython has a restriction of obtaining up to 100 tweets per query thus making the scraping of a large set of tweets cumbersome. 


