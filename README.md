# Instagram-Assets
Script for instagram scraping
```
from instgram-assets import InstaContent
```

## Login
```
insta_obj = InstaContent('username','password') #To login to instagram
```

## Get Following data 
Can be used to get the dictionary of users who don't follow you back
```
followers_data = insta_obj.followers() #to get followers only
unfollowers_data = insta_obj.followers(unfollowers_only=True) #to get unfollowers data
```

## Download Post 
```
insta_obj.downloadPost('https://www.instagram.com/p/CPJGp3Yp6wR/',filename=None) #(url,filename) filename should be included
```


