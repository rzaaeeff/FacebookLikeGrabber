__author__ = 'rzaaeeff'

#Dependencies start
from requests import get
import json
#Finish

class FacebookLikeGrabber:
    def __init__(self, access_token):
        self.access_token_str = '?access_token=%s' % access_token

    def get_likes_by_post_id(self, post_id):
        """
            Facebook uses paging for like list.
            That's why, i used special algorithm
            to grab all users who like post.
        """
        ended = True
        post_likes = {}

        response = get("https://graph.facebook.com/" + post_id + "/likes/" + self.access_token_str + '&limit=1000') #making query to graph.facebook.com | &limit=1000 is the number of maximum likes for each page
        raw = json.loads(response.text) #response.text will give us string, but we need json

        for item in raw['data']:
            post_likes[item['name']] = item['id']

        if 'next' in raw['paging']: #checking if there is next page
            ended = False

        while not ended:
            response = get(raw['paging']['next'])
            raw = json.loads(response.text)

            for x in raw['data']:
                post_likes[x['name']] = x['id']

            if 'next' in raw['paging']:
                ended = False
            else:
                ended = True

        return post_likes

    def get_posts_from_page(self, page_id, count):
        post_ids = []

        response = get("https://graph.facebook.com/" + page_id + "/statuses/" + self.access_token_str + '&limit=' + str(count))
        raw = json.loads(response.text)

        for post in raw['data']:
            post_ids.append(str(post['id']))

        return post_ids

access_token = raw_input("Welcome! Please, enter your access token: ")
grabber_object = FacebookLikeGrabber(str(access_token))
input = '0'
count = 0

while input != '1' and input != '2' and input != '3':
    print "Please choose operation:"
    print "   1. Grab posts from page"
    print "   2. Grab likes from post/photo"
    print "   3. Grab posts and likes"
    input = str(raw_input('Your choice: '))

if input == '1':
    page_id = raw_input("Please, enter ID of a page: ")

    while count < 1 or count > 250:
        count = int(raw_input("Please, enter number of posts you would like to grab. (Not exceeding 250): "))

    posts = grabber_object.get_posts_from_page(page_id, str(count))
    print posts
elif input == '2':
    post_id = str(raw_input("Please, enter ID of a post/photo: "))

    likes = grabber_object.get_likes_by_post_id(post_id)

    print likes

else:
    page_id = raw_input("Please, enter ID of a page: ")

    while count < 1 or count > 250:
        count = int(raw_input("Please, enter number of posts you would like to grab. (Not exceeding 250): "))

    posts = grabber_object.get_posts_from_page(page_id, str(count))

    for post in posts:
        print post + ' : ' + str(grabber_object.get_likes_by_post_id(str(post)))
