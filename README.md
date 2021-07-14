# CI-CD GitHub Actions

## Disclaimer 
This repository is set to private as I am still figuring out how to parse the Github secrets into the Python file run by GitHub actions. Also, an online search reviewed that the automatic trigger of GitHub actions may not work at times.

## Background
Tweets are a good reflection of public sentiment on any particular topic. As an extension to my previous Sentiment Analysis project on United Airlines, this set of code aims to automate the processs of scraping for tweets so that we can obtain a larger set of data which translates to higher accuracy for topic modeling. 

## Process 
The python pacakge [Twython](https://twython.readthedocs.io/en/latest/) is being used to obtain tweets. 

## Challenges
Using Twython or any other similar packages to obtain tweets usually involves having to input the secret keys issued by Twitter. The initial method that was used is to save a separate json file with these secret credentials and use the python script to retrive them. A layer of complication is added when this process is automated through GitHub actions.
Secondly, Twython has a restriction of obtaining up to 100 tweets per query thus making the scraping of a large set of tweets cumbersome. 


