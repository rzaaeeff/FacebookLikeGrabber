grabber_object = FacebookLikeGrabber('ACCESS_TOKEN')

post_IDs = grabber_object.get_posts_from_page(page_id='PAGE_ID', count='Count of posts you want to grab | It will grab only their IDs')

for post in post_IDs:
    print grabber_object.get_likes_by_post_id(post)