Outdated. Project is no longer updated. 
***

## Synopsis
This library helps you to grab likes from any given post or photo. It can also grab ID of posts from page, for now number of maximum posts can be revealed is 250. It is beta version.

## Code Example
Examples are located at 'Examples' folder. Here is one of them:<br/>
```
grabber_object = FacebookLikeGrabber('ACCESS_TOKEN')

post_IDs = grabber_object.get_posts_from_page(page_id='PAGE_ID', count='Count of posts you want to grab | It will grab only their IDs')

for post in post_IDs:
  print grabber_object.get_likes_by_post_id(post)
```

## Reference
This library has only two functions for now. <br/>
* `get_likes_by_post_id(post_id)` : `post_id` is string which stands for ID of post object. <br/>
* `get_posts_from_page(page_id, count)`
 * `page_id` is string which stands for ID of page object.
 * `count` is the number of posts you want to grab. For now, it's limited up to 250.

If you want to find out page's ID, use this website: http://findmyfacebookid.com/

## License
GNU General Public License v2.0
