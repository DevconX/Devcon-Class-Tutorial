import tweepy
import json
import time
import os

MAX_FRIENDS = 200
FRIENDS_OF_FRIENDS_LIMIT = 200
CONSUMER_KEY = 'K7H3MKsTvIMJgYL8QGmKQurSt'
CONSUMER_SECRET = 'AIz0rjzSMdZZfpfqRT0SJJiH3tIjwdP5u8OhOlq9ec5iOwS6Y6'
ACCESS_TOKEN = '2438095309-BZOpxIosUolPWzwgFHTIvSqGdCFsTTwZiVBrYSP'
ACCESS_TOKEN_SECRET = '5p8Xl4LYt25IGfENhIoKdie42vDBfo658t3PRbDOlVmTA'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def get_follower_ids(centre, top, max_depth=1, current_depth=0, accepted_list=[], data=[]):
    if current_depth == max_depth:
        print('out of depth')
        return data, accepted_list
    if centre in accepted_list:
        print('already in the list')
        return data, accepted_list
    else:
        accepted_list.append(centre)
    while True:
        try:
            user = api.get_user(centre)
            d = {'name': user.name,
                 'screen_name': user.screen_name,
                 'id': user.id,
                 'friends_count': user.friends_count,
                 'followers_count': user.followers_count,
                 'followers_ids': user.followers_ids(),
                 'centre':top}
            data.append(d)
            break
        except tweepy.TweepError as error:
            if str(error).find('Not authorized') >= 0:
                print('Cannot access user data, not authorized.')
                return data
            if str(error).find('User has been suspended') >= 0:
                print('user suspended')
                return data
            if error[0][0]['message'].find('Rate limit exceeded') >= 0:
                print('Rate limited. Sleeping for 15 mins.')
                time.sleep(60*15)
                continue
            print('undefined error')
            return data, accepted_list
    screen_name = user.screen_name
    c = tweepy.Cursor(api.friends, id=user.id).items()
    friendids = []
    friend_count = 0
    while True:
        try:
            friend = c.next()
            friendids.append(friend.id)
            params = (friend.id, friend.screen_name, friend.name)
            print('%s\t%s\t%s\n' % params)
            d = {'name': friend.name,
                 'screen_name': friend.screen_name,
                 'id': friend.id,
                 'friends_count': friend.friends_count,
                 'followers_count': friend.followers_count,
                 'followers_ids': friend.followers_ids(),
                 'centre':top}
            data.append(d)
            friend_count += 1
            if friend_count >= MAX_FRIENDS:
                print('Reached max no. of friends for "%s".' % friend.screen_name)
                break
        except tweepy.TweepError:
            print('Rate limited. Sleeping for 15 mins.')
            time.sleep(60*15)
            continue
        except StopIteration:
            break
    print('Found %d friends for %s' % (len(friendids), screen_name))
    cd = current_depth
    if cd+1 < max_depth:
        for fid in friendids[:FRIENDS_OF_FRIENDS_LIMIT]:
            data, accepted_list = get_follower_ids(fid, user.id, max_depth=max_depth, current_depth=cd+1, accepted_list=accepted_list,data=data)
    if cd+1 < max_depth and len(friendids) > FRIENDS_OF_FRIENDS_LIMIT:
        print('Not all friends retrieved for %s' % screen_name)
    return data, accepted_list        