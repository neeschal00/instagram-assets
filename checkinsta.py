from InstaContent.insta_assets import InstaContent
from pprint import pprint
# from creds import username,password
username = input("Enter Your instagram Username :")
password = input("Enter Your Password :")
obj = InstaContent(username,password) # Enter username and password
unfollowers_data = obj.followers(unfollowers_only=True) #to get the list of unfollowers only
# pprint(unfollowers_data)
post_url = input("Enter the Post url that you want to download: ")
obj.downloadPost(post_url)




