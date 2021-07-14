# CI-CD GitHub Actions

## Disclaimer 
An online search reviewed that the automatic trigger of GitHub actions may not work at times.

## Background
Tweets are a good reflection of public sentiment on any particular topic. As an extension to my previous [Sentiment Analysis project on United Airlines](https://github.com/kenneth-cheong/Airlines-Tweets-Sentiment-Analysis), this set of code aims to automate the processs of scraping for tweets so that we can obtain a larger set of data which translates to higher accuracy for topic modeling. 

## Process 
The python package [Twython](https://twython.readthedocs.io/en/latest/) is being used to obtain tweets. 

## Challenges
Using Twython or any other similar packages to obtain tweets usually involves having to input the secret keys issued by Twitter. The keys have to be kept confidential or Twitter will not be too happy about it. 

Secondly, Twython has a restriction of obtaining up to 100 tweets per query thus making the scraping of a large set of tweets cumbersome. 


