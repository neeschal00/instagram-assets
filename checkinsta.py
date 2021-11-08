from InstaContent.insta_assets import InstaContent
from pprint import pprint
from creds import username,password
obj = InstaContent(username,password) # Enter username and password
# unfollowers_data = obj.followers(unfollowers_only=True) #to get the list of unfollowers only
# pprint(unfollowers_data)
obj.downloadPost('https://www.instagram.com/p/CVv2nOSItkG/')




