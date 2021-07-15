# CI-CD GitHub Actions

![1568663838814](https://user-images.githubusercontent.com/49676161/125658541-34f01210-12de-4dd5-a69a-ecebe49402c0.png)

## Disclaimer 
An online search reviewed that the automatic trigger of GitHub actions may not work at times. Also, I have not been able to access the csv files by the scheduled runs via GitHub actions. 

## Background
![word_cloud](https://user-images.githubusercontent.com/49676161/125658667-3f0f57a8-025d-4535-84c6-501127d75961.png)
Tweets are a good reflection of public sentiment on any particular topic. As an extension to my previous [Sentiment Analysis project on United Airlines](https://github.com/kenneth-cheong/Airlines-Tweets-Sentiment-Analysis), this set of code aims to automate the processs of scraping for tweets so that we can obtain a larger set of data which translates to higher accuracy for topic modeling. 

## GitHub Actions
There are two .yml files in CI-CD-GitHub-Actions/.github/workflows/. One [manual](https://github.com/kenneth-cheong/CI-CD-GitHub-Actions/blob/main/.github/workflows/collect-manual.yml) and one [automatic](https://github.com/kenneth-cheong/CI-CD-GitHub-Actions/blob/main/.github/workflows/collect-auto.yml). As its name suggests, the manual one has to be triggered in the 'Actions' tab of this repository. 

## Process 
The python package [Twython](https://twython.readthedocs.io/en/latest/) is being used to obtain tweets. The secrets function in GitHub actions has been used to make the access the confidential Twitter keys.

## Challenges
Using Twython or any other similar packages to obtain tweets usually involves having to input the secret keys issued by Twitter. The keys have to be kept confidential or Twitter will not be too happy about it. 

Secondly, Twython has a restriction of obtaining up to 100 tweets per query thus making the scraping of a large set of tweets cumbersome. 

## Learning Points
1) Installing python packages in GitHub Actions
``` - name: setup dependencies
            run: |
              pip install twython
              pip install pandas
              pip install path
```
2) Referencing repo's secrets in GitHub Actions and running .py script
```          - name: execute py script # run the run.py to get the latest data
            env: 
                CONSUMER_KEY: ${{ secrets.CONSUMER_KEY }}
                CONSUMER_SECRET: ${{ secrets.CONSUMER_SECRET }}
            run: |
              python collect_tweets.py
```
3) Pushing and commiting the output .csv (generated by .py file) to the repo
```          - name: Commit and push if it changed
            run: |
              git config user.name "${GITHUB_ACTOR}"
              git config user.email "${GITHUB_ACTOR}@users.noreply.github.com"
              git add -A
              timestamp=$(date -u)
              git commit -m "Latest data: ${timestamp}" || exit 0
```
