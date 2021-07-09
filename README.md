# Instagram-Assets
Script that directly interacts with Instagram's Official api and make use of it
```
from InstaContent.insta_assets import InstaContent
```

## Login
```
insta_obj = InstaContent('username','password') #To login to instagram
```
> **Note:** If **2-factor Authentication** is on it doesn't work


## Get Following data 
Can be used to get the dictionary of users who don't follow you back
```
followers_data = insta_obj.followers() #to get followers only
unfollowers_data = insta_obj.followers(unfollowers_only=True) #to get unfollowers data
```

## Download Post 
```
insta_obj.downloadPost('https://www.instagram.com/p/CPJGp3Yp6wR/',filename=None) 
```
> **Note:** If **filename=None** the images are saved using post id and adds underscore(_) + number if post has multiple images/videos

