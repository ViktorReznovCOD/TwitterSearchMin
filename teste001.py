import pandas as pd
import numpy as np
import matplotlib as plt
from TwitterSearch import *

try:

    ts = TwitterSearch(
        consumer_key = 'ZDYLN82IkBw8JQtyDUVv7LqMf',
        consumer_secret = '5HF8FUBhlxLiR1iQW5Ks4tDLeOvGmPlW7wiwXhBBbqsOij16F4',
        access_token = '2697413658-igwnywvuuytG8D3jv6RSeUdxHcV7gU9d3E0gzkY',
        access_token_secret = 'O0zULBbGIYFmzN00sAamqxTRu6EmjMQLJRhsR62zulxwK'
     )

    tso = TwitterSearchOrder()
    tso.set_keywords(['ver o peso'])
    tso.set_language('pt')

    for tweet in ts.search_tweets_iterable(tso):
        print('\n' '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
        print(type(tweet))

        a1 = pd.Series(tweet)
        print(a1)

except TwitterSearchException as e:
    print(e)
    
