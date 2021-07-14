from InstaContent.insta_assets import InstaContent
from pprint import pprint
obj = InstaContent('username','password') # Enter username and password
unfollowers_data = obj.followers(unfollowers_only=True) #to get the list of unfollowers only
pprint(unfollowers_data)
# obj.downloadPost('https://www.instagram.com/p/CRPoOUVL4hu/?utm_source=ig_web_copy_link',)




