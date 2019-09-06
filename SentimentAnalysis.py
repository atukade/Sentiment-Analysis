{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import tweepy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "ACC_TOKEN = '3945791234-ETFJLAptA5R1sU9ymsB2M9NxHwfFvDpThTVztpG'\n",
    "ACC_SECRET = 'YsL4oelkgeih1TEkQ3iCObQers2vZGDAfE8IIpA8bTseN'\n",
    "CONS_KEY = 'rhjGxdATAk9jz6Jt5ueAMQmXO'\n",
    "CONS_SECRET ='8iyDnvZtFbfX55HTiHm7te1onPvtFRGdC6cs11Pe8pn08tlcZF'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "def authentication(cons_key, cons_secret, acc_token, acc_secret):\n",
    "    auth = tweepy.OAuthHandler(cons_key, cons_secret)\n",
    "    auth.set_access_token(acc_token, acc_secret)\n",
    "    api = tweepy.API(auth)\n",
    "    return api"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "from datetime import datetime, timedelta\n",
    "today_datetime = datetime.today().now()\n",
    "yesterday_datetime = today_datetime - timedelta(days=1)\n",
    "today_date = today_datetime.strftime('%Y-%m-%d')\n",
    "yesterday_date = yesterday_datetime.strftime('%Y-%m-%d')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "api = authentication(CONS_KEY,CONS_SECRET,ACC_TOKEN,ACC_SECRET)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "def search_tweets(keyword, total_tweets):\n",
    "    today_datetime = datetime.today().now()\n",
    "    yesterday_datetime = today_datetime - timedelta(days=1)\n",
    "    today_date = today_datetime.strftime('%Y-%m-%d')\n",
    "    yesterday_date = yesterday_datetime.strftime('%Y-%m-%d')\n",
    "    api = authentication(CONS_KEY,CONS_SECRET,ACC_TOKEN,ACC_SECRET)\n",
    "    search_result = tweepy.Cursor(api.search, \n",
    "                                  q=keyword, \n",
    "                                  since=yesterday_date, \n",
    "                                  result_type='recent', \n",
    "                                  lang='en').items(total_tweets)\n",
    "    return search_result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "import re"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "from nltk.tokenize import WordPunctTokenizer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "def clean_tweets(tweet):\n",
    "    user_removed = re.sub(r'@[A-Za-z0-9]+','',tweet.decode('utf-8'))\n",
    "    link_removed = re.sub('https?://[A-Za-z0-9./]+','',user_removed)\n",
    "    number_removed = re.sub('[^a-zA-Z]', ' ', link_removed)\n",
    "    lower_case_tweet= number_removed.lower()\n",
    "    tok = WordPunctTokenizer()\n",
    "    words = tok.tokenize(lower_case_tweet)\n",
    "    clean_tweet = (' '.join(words)).strip()\n",
    "    return clean_tweet"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'google.cloud'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-21-5c3fb4459d75>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mfrom\u001b[0m \u001b[0mgoogle\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcloud\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mlanguage\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mgoogle\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcloud\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mlanguage\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0menums\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mgoogle\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcloud\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mlanguage\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mtypes\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'google.cloud'"
     ]
    }
   ],
   "source": [
    "from google.cloud import language\n",
    "from google.cloud.language import enums\n",
    "from google.cloud.language import types"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_sentiment_score(tweet):\n",
    "    client = language.LanguageServiceClient()\n",
    "    document = types\\\n",
    "               .Document(content=tweet,\n",
    "                         type=enums.Document.Type.PLAIN_TEXT)\n",
    "    sentiment_score = client\\\n",
    "                      .analyze_sentiment(document=document)\\\n",
    "                      .document_sentiment\\\n",
    "                      .score\n",
    "    return sentiment_score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'keyword' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-23-e16460f85b83>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0mscore\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;36m0\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mtweets\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0msearch_tweets\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mkeyword\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mtotal_tweets\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'keyword' is not defined"
     ]
    }
   ],
   "source": [
    "score = 0\n",
    "tweets = search_tweets(keyword, total_tweets)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'tweets' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-24-90c327c3dcf8>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mfor\u001b[0m \u001b[0mtweet\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mtweets\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m     \u001b[0mcleaned_tweet\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mclean_tweets\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mtweet\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtext\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mencode\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'utf-8'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'tweets' is not defined"
     ]
    }
   ],
   "source": [
    "for tweet in tweets:\n",
    "    cleaned_tweet = clean_tweets(tweet.text.encode('utf-8'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'tweets' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-25-380480f7fdb2>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mfor\u001b[0m \u001b[0mtweet\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mtweets\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m     \u001b[0mcleaned_tweet\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mclean_tweets\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mtweet\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtext\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mencode\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'utf-8'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m     \u001b[0msentiment_score\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mget_sentiment_score\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcleaned_tweet\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m     \u001b[0mscore\u001b[0m \u001b[1;33m+=\u001b[0m \u001b[0msentiment_score\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'tweets' is not defined"
     ]
    }
   ],
   "source": [
    "for tweet in tweets:\n",
    "    cleaned_tweet = clean_tweets(tweet.text.encode('utf-8'))\n",
    "    sentiment_score = get_sentiment_score(cleaned_tweet)\n",
    "    score += sentiment_score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'tweets' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-26-ea173a574bb9>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mfor\u001b[0m \u001b[0mtweet\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mtweets\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m     \u001b[0mcleaned_tweet\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mclean_tweets\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mtweet\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtext\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mencode\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'utf-8'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m     \u001b[0msentiment_score\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mget_sentiment_score\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcleaned_tweet\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m     \u001b[0mscore\u001b[0m \u001b[1;33m+=\u001b[0m \u001b[0msentiment_score\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'Tweet: {}'\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mformat\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcleaned_tweet\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'tweets' is not defined"
     ]
    }
   ],
   "source": [
    "for tweet in tweets:\n",
    "    cleaned_tweet = clean_tweets(tweet.text.encode('utf-8'))\n",
    "    sentiment_score = get_sentiment_score(cleaned_tweet)\n",
    "    score += sentiment_score\n",
    "    print('Tweet: {}'.format(cleaned_tweet))\n",
    "    print('Score: {}\\n'.format(sentiment_score))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "def analyze_tweets(keyword, total_tweets):\n",
    "    score = 0\n",
    "    tweets = search_tweets(keyword, total_tweets)\n",
    "    for tweet in tweets:\n",
    "        cleaned_tweet = clean_tweets(tweet.text.encode('utf-8'))\n",
    "        sentiment_score = get_sentiment_score(cleaned_tweet)\n",
    "        score += sentiment_score\n",
    "        print('Tweet: {}'.format(cleaned_tweet))\n",
    "        print('Score: {}\\n'.format(sentiment_score))\n",
    "    final_score = round((score / float(total_tweets)),2)\n",
    "    return final_score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'update' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-29-b2f2758b0b53>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mkeyword\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mupdate\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmessage\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtext\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0mfinal_score\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0manalyze_tweets\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mkeyword\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m50\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'update' is not defined"
     ]
    }
   ],
   "source": [
    "keyword = update.message.text\n",
    "final_score = analyze_tweets(keyword, 50)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "def send_the_result(bot, update):\n",
    "    keyword = update.message.text\n",
    "    final_score = analyze_tweets(keyword, 50)\n",
    "    if final_score <= -0.25:\n",
    "        status = 'NEGATIVE | ❌'\n",
    "    elif final_score <= 0.25:\n",
    "        status = 'NEUTRAL | 🔶'\n",
    "    else:\n",
    "        status = 'POSITIVE | ✅'\n",
    "    bot.send_message(chat_id=update.message.chat_id,\n",
    "                     text='Average score for '\n",
    "                           + str(keyword) \n",
    "                           + ' is ' \n",
    "                           + str(final_score) \n",
    "                           + ' | ' + status)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "ename": "ImportError",
     "evalue": "cannot import name 'TelegramError'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mImportError\u001b[0m                               Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-34-f39ee401c21e>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mfrom\u001b[0m \u001b[0mtelegram\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mext\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mUpdater\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mMessageHandler\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mFilters\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[1;32mdef\u001b[0m \u001b[0mmain\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m     \u001b[0mupdater\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mUpdater\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'YOUR_TOKEN'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m     \u001b[0mdp\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mupdater\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdispatcher\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m     \u001b[0mdp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0madd_handler\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mMessageHandler\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mFilters\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtext\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0msend_the_result\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\anuj tukade\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\telegram\\ext\\__init__.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     19\u001b[0m \u001b[1;34m\"\"\"Extensions over the Telegram Bot API to facilitate bot making\"\"\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     20\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 21\u001b[1;33m \u001b[1;32mfrom\u001b[0m \u001b[1;33m.\u001b[0m\u001b[0mdispatcher\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mDispatcher\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mDispatcherHandlerStop\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mrun_async\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     22\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[1;33m.\u001b[0m\u001b[0mjobqueue\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mJobQueue\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mJob\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     23\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[1;33m.\u001b[0m\u001b[0mupdater\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mUpdater\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\anuj tukade\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\telegram\\ext\\dispatcher.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     31\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mfuture\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mbuiltins\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mrange\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     32\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 33\u001b[1;33m \u001b[1;32mfrom\u001b[0m \u001b[0mtelegram\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mTelegramError\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     34\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mtelegram\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mext\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mhandler\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mHandler\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     35\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mtelegram\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mutils\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpromise\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mPromise\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mImportError\u001b[0m: cannot import name 'TelegramError'"
     ]
    }
   ],
   "source": [
    "from telegram.ext import Updater, MessageHandler, Filters\n",
    "def main():\n",
    "    updater = Updater('YOUR_TOKEN')\n",
    "    dp = updater.dispatcher\n",
    "    dp.add_handler(MessageHandler(Filters.text, send_the_result))\n",
    "    updater.start_polling()\n",
    "    updater.idle()\n",
    "if __name__ == '__main__':\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
