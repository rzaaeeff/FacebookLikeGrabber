grabber_object = FacebookLikeGrabber('ACCESS_TOKEN')

like_list = grabber_object.get_likes_by_post_id('POST_ID')

print like_list