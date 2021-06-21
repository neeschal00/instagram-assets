import requests
from pprint import pprint
from urllib.parse import urlencode, quote, urlsplit, urljoin
from urllib.request import urlretrieve
# url = 'https://www.instagram.com/accounts/login/'
# header = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
# }
# rep = requests.get(url,headers=header)
# print(rep.status_code)
# print(rep.cookies)
# # print(rep.json())

# dict1 = {1:"abkszdb",2:"ldishfksh,d"}
# dict2 = {"jabsd":1,"baksjd":"21nqwlkn"}
# dict3 = {**dict1,**dict2}
# print(dict3)

<<<<<<< HEAD
# https://www.instagram.com/p/BvZVTxugX68/

=======
>>>>>>> 07b36bcb368b3163609ac876dec26172a61044ee
# hdrs = {'Content-Type': 'application/json; charset=utf-8', 'ig-set-password-encryption-web-key-id': '12', 'ig-set-password-encryption-web-pub-key': 'f3d320d6756230c6e1ccca141e633d9ef50f4d9cdcd70fcb26fd17107b54c649', 'ig-set-password-encryption-web-key-version': '10', 'x-robots-tag': 'noindex', 'Vary': 'Accept-Language, Cookie', 'Content-Language': 'en', 'Date': 'Fri, 07 May 2021 15:37:18 GMT', 'Strict-Transport-Security': 'max-age=31536000', 'Cache-Control': 'private, no-cache, no-store, must-revalidate', 'Pragma': 'no-cache', 'Expires': 'Sat, 01 Jan 2000 00:00:00 GMT', 'X-Frame-Options': 'SAMEORIGIN', 'content-security-policy': "report-uri https://www.instagram.com/security/csp_report/; default-src 'self' https://www.instagram.com; img-src data: blob: https://*.fbcdn.net https://*.instagram.com https://*.cdninstagram.com https://*.facebook.com https://*.fbsbx.com https://*.giphy.com; font-src data: https://*.fbcdn.net https://*.instagram.com https://*.cdninstagram.com; media-src 'self' blob: https://www.instagram.com https://*.cdninstagram.com https://*.fbcdn.net; manifest-src 'self' https://www.instagram.com; script-src 'self' https://instagram.com https://www.instagram.com https://*.www.instagram.com https://*.cdninstagram.com wss://www.instagram.com https://*.facebook.com https://*.fbcdn.net https://*.facebook.net 'unsafe-inline' 'unsafe-eval' blob:; style-src 'self' https://*.www.instagram.com https://www.instagram.com 'unsafe-inline'; connect-src 'self' https://instagram.com https://www.instagram.com https://*.www.instagram.com https://graph.instagram.com https://*.graph.instagram.com https://graphql.instagram.com https://*.cdninstagram.com https://api.instagram.com https://i.instagram.com https://*.i.instagram.com wss://www.instagram.com wss://edge-chat.instagram.com https://*.facebook.com https://*.fbcdn.net https://*.facebook.net chrome-extension://boadgeojelhgndaghljhdicfkmllpafd blob:; worker-src 'self' blob: https://www.instagram.com; frame-src 'self' https://instagram.com https://www.instagram.com https://*.instagram.com https://staticxx.facebook.com https://www.facebook.com https://web.facebook.com https://connect.facebook.net https://m.facebook.com; object-src 'none'; upgrade-insecure-requests", 'cross-origin-embedder-policy-report-only': 'require-corp;report-to="coep"', 'report-to': '{"group": "coep", "max_age": 86400, "endpoints": [{"url": "/security/coep_report/"}]}', 'X-Content-Type-Options': 'nosniff', 'X-XSS-Protection': '0', 'x-ig-push-state': 'c2', 'x-aed': '44', 'Access-Control-Expose-Headers': 'X-IG-Set-WWW-Claim', 'Set-Cookie': 'csrftoken=t9gJhmgXrAViTaIgu9o6ukSu4MgXXFvN; Domain=.instagram.com; expires=Fri, 06-May-2022 15:37:18 GMT; Max-Age=31449600; Path=/; Secure, rur=NAO; Domain=.instagram.com; HttpOnly; Path=/; Secure, ds_user_id=44503193972; Domain=.instagram.com; expires=Thu, 05-Aug-2021 15:37:18 GMT; Max-Age=7776000; Path=/; Secure, sessionid=44503193972%3ANXv2osTiIcMNl4%3A16; Domain=.instagram.com; expires=Sat, 07-May-2022 15:37:18 GMT; HttpOnly; Max-Age=31536000; Path=/; Secure', 'x-ig-origin-region': 'nao', 'X-FB-TRIP-ID': '1679558926', 'Alt-Svc': 'h3-29=":443"; ma=3600,h3-27=":443"; ma=3600', 'Connection': 'keep-alive', 'Content-Length': '91'}
# pprint(hdrs)

# data = {'data': {'user': {'edge_follow': {'count': 137, 'page_info': {'has_next_page': True, 'end_cursor': 'QVFEZ1NOMkJ6WGpEVy1WMFJ0QndmTFBwMDk1N284VzdDemlRMGlyQU8tTk1uZE1jWnJ4WEY0ajJTX3d6Rnlfb2lmZ3JqU1hGS1BVYkZ0Q1p4V3A0NFNYLQ=='}, 'edges': [{'node': {'id': '3144447773', 'username': 'aayuushmaa', 'full_name': 'Aayushma Bajracharya', 'profile_pic_url': 'https://instagram.fbwa1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/131372534_814215196092527_53253237212519559_n.jpg?tp=1&_nc_ht=instagram.fbwa1-1.fna.fbcdn.net&_nc_ohc=AA0o18LRTxYAX8qUTJa&edm=ANg5bX4BAAAA&ccb=7-4&oh=1aab609d10d6d878b6b126e1a61cd057&oe=60BB6D88&_nc_sid=55937d', 'is_private': True, 'is_verified': False, 'followed_by_viewer': True, 'follows_viewer': False, 'requested_by_viewer': False, 'reel': {'id': '3144447773', 'expiring_at': 1620492146, 'has_pride_media': False, 'latest_reel_media': 0, 'seen': None, 'owner': {'__typename': 'GraphUser', 'id': '3144447773', 'profile_pic_url': 'https://instagram.fbwa1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/131372534_814215196092527_53253237212519559_n.jpg?tp=1&_nc_ht=instagram.fbwa1-1.fna.fbcdn.net&_nc_ohc=AA0o18LRTxYAX8qUTJa&edm=ANg5bX4BAAAA&ccb=7-4&oh=1aab609d10d6d878b6b126e1a61cd057&oe=60BB6D88&_nc_sid=55937d', 'username': 'aayuushmaa'}}}}, {'node': {'id': '2048931707', 'username': 'nikita__khadka', 'full_name': '𝓝𝓲𝓴𝓴𝓼💛', 'profile_pic_url': 'https://instagram.fbwa1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/176439522_517198086111978_1011131411237631185_n.jpg?tp=1&_nc_ht=instagram.fbwa1-1.fna.fbcdn.net&_nc_ohc=aAgx_0Ur2PoAX-y68UE&edm=ANg5bX4BAAAA&ccb=7-4&oh=249c3494d1b175a90ff9ae4517f2dd65&oe=60BB6C52&_nc_sid=55937d', 'is_private': True, 'is_verified': False, 'followed_by_viewer': True, 'follows_viewer': False, 'requested_by_viewer': False, 'reel': {'id': '2048931707', 'expiring_at': 1620492146, 'has_pride_media': False, 'latest_reel_media': 0, 'seen': None, 'owner': {'__typename': 'GraphUser', 'id': '2048931707', 'profile_pic_url': 'https://instagram.fbwa1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/176439522_517198086111978_1011131411237631185_n.jpg?tp=1&_nc_ht=instagram.fbwa1-1.fna.fbcdn.net&_nc_ohc=aAgx_0Ur2PoAX-y68UE&edm=ANg5bX4BAAAA&ccb=7-4&oh=249c3494d1b175a90ff9ae4517f2dd65&oe=60BB6C52&_nc_sid=55937d', 'username': 'nikita__khadka'}}}}, {'node': {'id': '1457862604', 'username': 'aryal.riya', 'full_name': 'Riya Aryal', 'profile_pic_url': 'https://instagram.fbwa1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/171445021_238796811327148_2907598722205568640_n.jpg?tp=1&_nc_ht=instagram.fbwa1-1.fna.fbcdn.net&_nc_ohc=vsNTe8Fy1E8AX_UccsO&edm=ANg5bX4BAAAA&ccb=7-4&oh=1e7dd54abb0b8085dff73c8628750ab6&oe=60BB8885&_nc_sid=55937d', 'is_private': True, 'is_verified': False, 'followed_by_viewer': True, 'follows_viewer': False, 'requested_by_viewer': False, 'reel': {'id': '1457862604', 'expiring_at': 1620492146, 'has_pride_media': False, 'latest_reel_media': 0, 'seen': None, 'owner': {'__typename': 'GraphUser', 'id': '1457862604', 'profile_pic_url': 'https://instagram.fbwa1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/171445021_238796811327148_2907598722205568640_n.jpg?tp=1&_nc_ht=instagram.fbwa1-1.fna.fbcdn.net&_nc_ohc=vsNTe8Fy1E8AX_UccsO&edm=ANg5bX4BAAAA&ccb=7-4&oh=1e7dd54abb0b8085dff73c8628750ab6&oe=60BB8885&_nc_sid=55937d', 'username': 'aryal.riya'}}}}, {'node': {'id': '1437208534', 'username': 'yammuna_chhetri', 'full_name': 'Yammuna Chhetri', 'profile_pic_url': 'https://instagram.fbwa1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/176599722_1549588661915446_7968458158980293737_n.jpg?tp=1&_nc_ht=instagram.fbwa1-1.fna.fbcdn.net&_nc_ohc=W5_gW4gutb0AX9Uote2&edm=ANg5bX4BAAAA&ccb=7-4&oh=7b0c9357ef3e389be4da574893d812af&oe=60BBC21C&_nc_sid=55937d', 'is_private': True, 'is_verified': False, 'followed_by_viewer': True, 'follows_viewer': False, 'requested_by_viewer': False, 'reel': {'id': '1437208534', 'expiring_at': 1620492146, 'has_pride_media': False, 'latest_reel_media': 1620388646, 'seen': None, 'owner': {'__typename': 'GraphUser', 'id': '1437208534', 'profile_pic_url': 'https://instagram.fbwa1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/176599722_1549588661915446_7968458158980293737_n.jpg?tp=1&_nc_ht=instagram.fbwa1-1.fna.fbcdn.net&_nc_ohc=W5_gW4gutb0AX9Uote2&edm=ANg5bX4BAAAA&ccb=7-4&oh=7b0c9357ef3e389be4da574893d812af&oe=60BBC21C&_nc_sid=55937d', 'username': 'yammuna_chhetri'}}}}, {'node': {'id': '1406816274', 'username': 'soniyarai_', 'full_name': 'Soniya Chamling Rai🦄', 'profile_pic_url': 'https://instagram.fbwa1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/182866069_2971453263139172_4791740163744728754_n.jpg?tp=1&_nc_ht=instagram.fbwa1-1.fna.fbcdn.net&_nc_ohc=8U8w1y5a_TAAX8D0-Xd&edm=ANg5bX4BAAAA&ccb=7-4&oh=26e9ddd9613ab0b154889afe6c822d16&oe=60BC2AEA&_nc_sid=55937d', 'is_private': False, 'is_verified': False, 'followed_by_viewer': True, 'follows_viewer': False, 'requested_by_viewer': False, 'reel': {'id': '1406816274', 'expiring_at': 1620492146, 'has_pride_media': False, 'latest_reel_media': 1620397713, 'seen': None, 'owner': {'__typename': 'GraphUser', 'id': '1406816274', 'profile_pic_url': 'https://instagram.fbwa1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/182866069_2971453263139172_4791740163744728754_n.jpg?tp=1&_nc_ht=instagram.fbwa1-1.fna.fbcdn.net&_nc_ohc=8U8w1y5a_TAAX8D0-Xd&edm=ANg5bX4BAAAA&ccb=7-4&oh=26e9ddd9613ab0b154889afe6c822d16&oe=60BC2AEA&_nc_sid=55937d', 'username': 'soniyarai_'}}}}, {'node': {'id': '5720046714', 'username': 'pujanishah', 'full_name': 'Pujj', 'profile_pic_url': 'https://instagram.fbwa1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/177619410_506770020328674_7329176620702633014_n.jpg?tp=1&_nc_ht=instagram.fbwa1-1.fna.fbcdn.net&_nc_ohc=um4hg2LHFq0AX8qcmc8&edm=ANg5bX4BAAAA&ccb=7-4&oh=6cd2d3349a84a8f49f899d10f1e882ea&oe=60B9CE82&_nc_sid=55937d', 'is_private': False, 'is_verified': False, 'followed_by_viewer': True, 'follows_viewer': False, 'requested_by_viewer': False, 'reel': {'id': '5720046714', 'expiring_at': 1620492146, 'has_pride_media': False, 'latest_reel_media': 1620391928, 'seen': 1620391928, 'owner': {'__typename': 'GraphUser', 'id': '5720046714', 'profile_pic_url': 'https://instagram.fbwa1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/177619410_506770020328674_7329176620702633014_n.jpg?tp=1&_nc_ht=instagram.fbwa1-1.fna.fbcdn.net&_nc_ohc=um4hg2LHFq0AX8qcmc8&edm=ANg5bX4BAAAA&ccb=7-4&oh=6cd2d3349a84a8f49f899d10f1e882ea&oe=60B9CE82&_nc_sid=55937d', 'username': 'pujanishah'}}}}, {'node': {'id': '3078563016', 'username': 'subeefa._', 'full_name': '', 'profile_pic_url': 'https://instagram.fbwa1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/176891108_507762156895535_5740788632690579438_n.jpg?tp=1&_nc_ht=instagram.fbwa1-1.fna.fbcdn.net&_nc_ohc=CcWqruEYcvcAX-hr3NP&edm=ANg5bX4BAAAA&ccb=7-4&oh=78f63fafece2ddb2fe38b20e6ed9e5a4&oe=60BBC265&_nc_sid=55937d', 'is_private': False, 'is_verified': False, 'followed_by_viewer': True, 'follows_viewer': False, 'requested_by_viewer': False, 'reel': {'id': '3078563016', 'expiring_at': 1620492146, 'has_pride_media': False, 'latest_reel_media': 0, 'seen': None, 'owner': {'__typename': 'GraphUser', 'id': '3078563016', 'profile_pic_url': 'https://instagram.fbwa1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/176891108_507762156895535_5740788632690579438_n.jpg?tp=1&_nc_ht=instagram.fbwa1-1.fna.fbcdn.net&_nc_ohc=CcWqruEYcvcAX-hr3NP&edm=ANg5bX4BAAAA&ccb=7-4&oh=78f63fafece2ddb2fe38b20e6ed9e5a4&oe=60BBC265&_nc_sid=55937d', 'username': 'subeefa._'}}}}, {'node': {'id': '4561878420', 'username': 'richa_neupane_', 'full_name': 'Richa Neupane', 'profile_pic_url': 'https://instagram.fbwa1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/179989907_4221432994542334_1581230566438811658_n.jpg?tp=1&_nc_ht=instagram.fbwa1-1.fna.fbcdn.net&_nc_ohc=YOdw5OgGXbsAX_siXYq&edm=ANg5bX4BAAAA&ccb=7-4&oh=e1087a0fce2f25d49fbfb60c35e6e326&oe=60BAB3CE&_nc_sid=55937d', 'is_private': False, 'is_verified': False, 'followed_by_viewer': True, 'follows_viewer': False, 'requested_by_viewer': False, 'reel': {'id': '4561878420', 'expiring_at': 1620492146, 'has_pride_media': False, 'latest_reel_media': 0, 'seen': None, 'owner': {'__typename': 'GraphUser', 'id': '4561878420', 'profile_pic_url': 'https://instagram.fbwa1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/179989907_4221432994542334_1581230566438811658_n.jpg?tp=1&_nc_ht=instagram.fbwa1-1.fna.fbcdn.net&_nc_ohc=YOdw5OgGXbsAX_siXYq&edm=ANg5bX4BAAAA&ccb=7-4&oh=e1087a0fce2f25d49fbfb60c35e6e326&oe=60BAB3CE&_nc_sid=55937d', 'username': 'richa_neupane_'}}}}, {'node': {'id': '44946804623', 'username': 'amshuuuuuu', 'full_name': 'A M S H U💫', 'profile_pic_url': 'https://instagram.fbwa1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/182134511_877922506088537_7914947383415697143_n.jpg?tp=1&_nc_ht=instagram.fbwa1-1.fna.fbcdn.net&_nc_ohc=V7tBX19EOuQAX-fHcRM&edm=ANg5bX4BAAAA&ccb=7-4&oh=02ee386e5c89d8893a4695d997238d93&oe=60B9506C&_nc_sid=55937d', 'is_private': False, 'is_verified': False, 'followed_by_viewer': True, 'follows_viewer': False, 'requested_by_viewer': False, 'reel': {'id': '44946804623', 'expiring_at': 1620492146, 'has_pride_media': False, 'latest_reel_media': 1620395149, 'seen': 1620352922, 'owner': {'__typename': 'GraphUser', 'id': '44946804623', 'profile_pic_url': 'https://instagram.fbwa1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/182134511_877922506088537_7914947383415697143_n.jpg?tp=1&_nc_ht=instagram.fbwa1-1.fna.fbcdn.net&_nc_ohc=V7tBX19EOuQAX-fHcRM&edm=ANg5bX4BAAAA&ccb=7-4&oh=02ee386e5c89d8893a4695d997238d93&oe=60B9506C&_nc_sid=55937d', 'username': 'amshuuuuuu'}}}}, {'node': {'id': '1353481945', 'username': '__prazuuuuuu', 'full_name': 'Prazu Dhaubanjar', 'profile_pic_url': 'https://instagram.fbwa1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/172918663_2932739813673895_6543872465236587142_n.jpg?tp=1&_nc_ht=instagram.fbwa1-1.fna.fbcdn.net&_nc_ohc=yPQOMokmtXgAX8KXJFR&tn=BoLveKYyQhmteCGc&edm=ANg5bX4BAAAA&ccb=7-4&oh=25acf9a9159f283d431e018adfdeced8&oe=60BA34AA&_nc_sid=55937d', 'is_private': False, 'is_verified': False, 'followed_by_viewer': True, 'follows_viewer': False, 'requested_by_viewer': False, 'reel': {'id': '1353481945', 'expiring_at': 1620492146, 'has_pride_media': False, 'latest_reel_media': 0, 'seen': None, 'owner': {'__typename': 'GraphUser', 'id': '1353481945', 'profile_pic_url': 'https://instagram.fbwa1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/172918663_2932739813673895_6543872465236587142_n.jpg?tp=1&_nc_ht=instagram.fbwa1-1.fna.fbcdn.net&_nc_ohc=yPQOMokmtXgAX8KXJFR&edm=ANg5bX4BAAAA&ccb=7-4&oh=c1560673d4d24ecf9f1d01bb4928b18c&oe=60BA34AA&_nc_sid=55937d', 'username': '__prazuuuuuu'}}}}, {'node': {'id': '3176786135', 'username': '__swastii', 'full_name': 'S W A S T I K A', 'profile_pic_url': 'https://instagram.fbwa1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/165630567_312953383583467_6808858692478202456_n.jpg?tp=1&_nc_ht=instagram.fbwa1-1.fna.fbcdn.net&_nc_ohc=hT0qBjNyoI8AX8SR0dN&edm=ANg5bX4BAAAA&ccb=7-4&oh=62053160e1dc7e684e1ad1f053645e4a&oe=60BB135A&_nc_sid=55937d', 'is_private': False, 'is_verified': False, 'followed_by_viewer': True, 'follows_viewer': False, 'requested_by_viewer': False, 'reel': {'id': '3176786135', 'expiring_at': 1620492146, 'has_pride_media': False, 'latest_reel_media': 0, 'seen': None, 'owner': {'__typename': 'GraphUser', 'id': '3176786135', 'profile_pic_url': 'https://instagram.fbwa1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/165630567_312953383583467_6808858692478202456_n.jpg?tp=1&_nc_ht=instagram.fbwa1-1.fna.fbcdn.net&_nc_ohc=hT0qBjNyoI8AX8SR0dN&edm=ANg5bX4BAAAA&ccb=7-4&oh=62053160e1dc7e684e1ad1f053645e4a&oe=60BB135A&_nc_sid=55937d', 'username': '__swastii'}}}}, {'node': {'id': '217327765', 'username': 'malla.surakshya', 'full_name': 'Surakshya M.', 'profile_pic_url': 'https://instagram.fbwa1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/155286888_442469810334308_1904211029172408078_n.jpg?tp=1&_nc_ht=instagram.fbwa1-1.fna.fbcdn.net&_nc_ohc=ppTEHHZxVcQAX-o5kEz&edm=ANg5bX4BAAAA&ccb=7-4&oh=46278c261433540a898352e728243a4b&oe=60BBEF8B&_nc_sid=55937d', 'is_private': False, 'is_verified': False, 'followed_by_viewer': True, 'follows_viewer': False, 'requested_by_viewer': False, 'reel': {'id': '217327765', 'expiring_at': 1620492146, 'has_pride_media': False, 'latest_reel_media': 0, 'seen': 1620398560, 'owner': {'__typename': 'GraphUser', 'id': '217327765', 'profile_pic_url': 'https://instagram.fbwa1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/155286888_442469810334308_1904211029172408078_n.jpg?tp=1&_nc_ht=instagram.fbwa1-1.fna.fbcdn.net&_nc_ohc=ppTEHHZxVcQAX-o5kEz&edm=ANg5bX4BAAAA&ccb=7-4&oh=46278c261433540a898352e728243a4b&oe=60BBEF8B&_nc_sid=55937d', 'username': 'malla.surakshya'}}}}, {'node': {'id': '1300347066', 'username': 'kritiika', 'full_name': '𝙺𝚛𝚒𝚝𝚒𝚔𝚊', 'profile_pic_url': 'https://instagram.fbwa1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/173426426_484673389322424_4769562623511252476_n.jpg?tp=1&_nc_ht=instagram.fbwa1-1.fna.fbcdn.net&_nc_ohc=6yGk7bUj95EAX8mXbZK&edm=ANg5bX4BAAAA&ccb=7-4&oh=02992598864ebf7609c6ab6ea8816f06&oe=60BA2334&_nc_sid=55937d', 'is_private': False, 'is_verified': False, 'followed_by_viewer': True, 'follows_viewer': False, 'requested_by_viewer': False, 'reel': {'id': '1300347066', 'expiring_at': 1620492146, 'has_pride_media': False, 'latest_reel_media': 0, 'seen': None, 'owner': {'__typename': 'GraphUser', 'id': '1300347066', 'profile_pic_url': 'https://instagram.fbwa1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/173426426_484673389322424_4769562623511252476_n.jpg?tp=1&_nc_ht=instagram.fbwa1-1.fna.fbcdn.net&_nc_ohc=6yGk7bUj95EAX8mXbZK&edm=ANg5bX4BAAAA&ccb=7-4&oh=02992598864ebf7609c6ab6ea8816f06&oe=60BA2334&_nc_sid=55937d', 'username': 'kritiika'}}}}, {'node': {'id': '1949925424', 'username': 'deepaa__', 'full_name': 'दिपा अधिकारी 🇳🇵', 'profile_pic_url': 'https://instagram.fbwa1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/176996015_185873673370853_6320344702571789923_n.jpg?tp=1&_nc_ht=instagram.fbwa1-1.fna.fbcdn.net&_nc_ohc=MKbFKad9KIMAX_sOxaj&edm=ANg5bX4BAAAA&ccb=7-4&oh=ac281d8f6298911842a80ccac8a18727&oe=60BC1592&_nc_sid=55937d', 'is_private': True, 'is_verified': False, 'followed_by_viewer': True, 'follows_viewer': False, 'requested_by_viewer': False, 'reel': {'id': '1949925424', 'expiring_at': 1620492146, 'has_pride_media': False, 'latest_reel_media': 0, 'seen': None, 'owner': {'__typename': 'GraphUser', 'id': '1949925424', 'profile_pic_url': 'https://instagram.fbwa1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/176996015_185873673370853_6320344702571789923_n.jpg?tp=1&_nc_ht=instagram.fbwa1-1.fna.fbcdn.net&_nc_ohc=MKbFKad9KIMAX_sOxaj&edm=ANg5bX4BAAAA&ccb=7-4&oh=ac281d8f6298911842a80ccac8a18727&oe=60BC1592&_nc_sid=55937d', 'username': 'deepaa__'}}}}, {'node': {'id': '1518632781', 'username': 'soniyaa.l', 'full_name': 'SONIYA', 'profile_pic_url': 'https://instagram.fbwa1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/181381750_973356123436845_1140225503395230453_n.jpg?tp=1&_nc_ht=instagram.fbwa1-1.fna.fbcdn.net&_nc_ohc=gkaHV-51QOwAX8xGkOK&edm=ANg5bX4BAAAA&ccb=7-4&oh=40fdd2604f429c2eeecaf6d1783dbda4&oe=60BA2C95&_nc_sid=55937d', 'is_private': True, 'is_verified': False, 'followed_by_viewer': True, 'follows_viewer': False, 'requested_by_viewer': False, 'reel': {'id': '1518632781', 'expiring_at': 1620492146, 'has_pride_media': False, 'latest_reel_media': 1620387368, 'seen': None, 'owner': {'__typename': 'GraphUser', 'id': '1518632781', 'profile_pic_url': 'https://instagram.fbwa1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/181381750_973356123436845_1140225503395230453_n.jpg?tp=1&_nc_ht=instagram.fbwa1-1.fna.fbcdn.net&_nc_ohc=gkaHV-51QOwAX8xGkOK&edm=ANg5bX4BAAAA&ccb=7-4&oh=40fdd2604f429c2eeecaf6d1783dbda4&oe=60BA2C95&_nc_sid=55937d', 'username': 'soniyaa.l'}}}}, {'node': {'id': '2233282120', 'username': 'manchae313', 'full_name': 'Manisha Kc', 'profile_pic_url': 'https://instagram.fbwa1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/173632465_3994999427187033_4309030135178340637_n.jpg?tp=1&_nc_ht=instagram.fbwa1-1.fna.fbcdn.net&_nc_ohc=2c6TRQZGSS8AX8oMUmo&edm=ANg5bX4BAAAA&ccb=7-4&oh=d18b16a33536d4b7d443f2b0689f28cf&oe=60B90A24&_nc_sid=55937d', 'is_private': False, 'is_verified': False, 'followed_by_viewer': True, 'follows_viewer': False, 'requested_by_viewer': False, 'reel': {'id': '2233282120', 'expiring_at': 1620492146, 'has_pride_media': False, 'latest_reel_media': 0, 'seen': None, 'owner': {'__typename': 'GraphUser', 'id': '2233282120', 'profile_pic_url': 'https://instagram.fbwa1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/173632465_3994999427187033_4309030135178340637_n.jpg?tp=1&_nc_ht=instagram.fbwa1-1.fna.fbcdn.net&_nc_ohc=2c6TRQZGSS8AX8oMUmo&edm=ANg5bX4BAAAA&ccb=7-4&oh=d18b16a33536d4b7d443f2b0689f28cf&oe=60B90A24&_nc_sid=55937d', 'username': 'manchae313'}}}}, {'node': {'id': '181481517', 'username': 'amandatrivizas', 'full_name': 'AMANDA TRIVIZAS', 'profile_pic_url': 'https://instagram.fbwa1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/53211154_785283978521646_5068196984217665536_n.jpg?tp=1&_nc_ht=instagram.fbwa1-1.fna.fbcdn.net&_nc_ohc=zoEqSFJwqq8AX_21vEL&edm=ANg5bX4BAAAA&ccb=7-4&oh=40727673317edb84cf567f813e447fb1&oe=60B9C84A&_nc_sid=55937d', 'is_private': False, 'is_verified': True, 'followed_by_viewer': True, 'follows_viewer': False, 'requested_by_viewer': False, 'reel': {'id': '181481517', 'expiring_at': 1620492146, 'has_pride_media': False, 'latest_reel_media': 1620401137, 'seen': None, 'owner': {'__typename': 'GraphUser', 'id': '181481517', 'profile_pic_url': 'https://instagram.fbwa1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/53211154_785283978521646_5068196984217665536_n.jpg?tp=1&_nc_ht=instagram.fbwa1-1.fna.fbcdn.net&_nc_ohc=zoEqSFJwqq8AX_21vEL&edm=ANg5bX4BAAAA&ccb=7-4&oh=40727673317edb84cf567f813e447fb1&oe=60B9C84A&_nc_sid=55937d', 'username': 'amandatrivizas'}}}}, {'node': {'id': '195635609', 'username': 'srijana____', 'full_name': 'Srijana Thapa Magar', 'profile_pic_url': 'https://instagram.fbwa1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/145462224_986606888750347_3689383162516629476_n.jpg?tp=1&_nc_ht=instagram.fbwa1-1.fna.fbcdn.net&_nc_ohc=bu_7f0f7SAgAX8Lv6zt&edm=ANg5bX4BAAAA&ccb=7-4&oh=e57a6f6846391ec3295be00f38e407ce&oe=60B9E979&_nc_sid=55937d', 'is_private': False, 'is_verified': False, 'followed_by_viewer': True, 'follows_viewer': False, 'requested_by_viewer': False, 'reel': {'id': '195635609', 'expiring_at': 1620492146, 'has_pride_media': False, 'latest_reel_media': 0, 'seen': None, 'owner': {'__typename': 'GraphUser', 'id': '195635609', 'profile_pic_url': 'https://instagram.fbwa1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/145462224_986606888750347_3689383162516629476_n.jpg?tp=1&_nc_ht=instagram.fbwa1-1.fna.fbcdn.net&_nc_ohc=bu_7f0f7SAgAX8Lv6zt&edm=ANg5bX4BAAAA&ccb=7-4&oh=e57a6f6846391ec3295be00f38e407ce&oe=60B9E979&_nc_sid=55937d', 'username': 'srijana____'}}}}, {'node': {'id': '6386466398', 'username': 'mati.naa', 'full_name': '', 'profile_pic_url': 'https://instagram.fbwa1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/179911232_319556169537378_2734579696119645269_n.jpg?tp=1&_nc_ht=instagram.fbwa1-1.fna.fbcdn.net&_nc_ohc=ysx8lg4U8SAAX8HlkTc&edm=ANg5bX4BAAAA&ccb=7-4&oh=dcaca061433b2b63b9b09fb479d7d9b8&oe=60BBD390&_nc_sid=55937d', 'is_private': True, 'is_verified': False, 'followed_by_viewer': True, 'follows_viewer': False, 'requested_by_viewer': False, 'reel': {'id': '6386466398', 'expiring_at': 1620492146, 'has_pride_media': False, 'latest_reel_media': 0, 'seen': None, 'owner': {'__typename': 'GraphUser', 'id': '6386466398', 'profile_pic_url': 'https://instagram.fbwa1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/179911232_319556169537378_2734579696119645269_n.jpg?tp=1&_nc_ht=instagram.fbwa1-1.fna.fbcdn.net&_nc_ohc=ysx8lg4U8SAAX8HlkTc&edm=ANg5bX4BAAAA&ccb=7-4&oh=dcaca061433b2b63b9b09fb479d7d9b8&oe=60BBD390&_nc_sid=55937d', 'username': 'mati.naa'}}}}, {'node': {'id': '5789325709', 'username': 'shrinashakya', 'full_name': 'shrinashakya', 'profile_pic_url': 'https://instagram.fbwa1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/62420810_489910498246145_8664947376940646400_n.jpg?tp=1&_nc_ht=instagram.fbwa1-1.fna.fbcdn.net&_nc_ohc=4wntsof4l0AAX8jSmrW&edm=ANg5bX4BAAAA&ccb=7-4&oh=eba1e8affb9de9e8d01d98dffb7ad50e&oe=60BB8335&_nc_sid=55937d', 'is_private': True, 'is_verified': False, 'followed_by_viewer': True, 'follows_viewer': False, 'requested_by_viewer': False, 'reel': {'id': '5789325709', 'expiring_at': 1620492146, 'has_pride_media': False, 'latest_reel_media': 0, 'seen': None, 'owner': {'__typename': 'GraphUser', 'id': '5789325709', 'profile_pic_url': 'https://instagram.fbwa1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/62420810_489910498246145_8664947376940646400_n.jpg?tp=1&_nc_ht=instagram.fbwa1-1.fna.fbcdn.net&_nc_ohc=4wntsof4l0AAX8jSmrW&edm=ANg5bX4BAAAA&ccb=7-4&oh=eba1e8affb9de9e8d01d98dffb7ad50e&oe=60BB8335&_nc_sid=55937d', 'username': 'shrinashakya'}}}}, {'node': {'id': '2277559750', 'username': 'sabbu.balami', 'full_name': 'Sabbu✌✌', 'profile_pic_url': 'https://instagram.fbwa1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/162097909_958382568239924_7239158560191763387_n.jpg?tp=1&_nc_ht=instagram.fbwa1-1.fna.fbcdn.net&_nc_ohc=Klga3Ka2jbgAX_KrNHX&edm=ANg5bX4BAAAA&ccb=7-4&oh=6dab383cbcd3b7f02d338c7f2e781f6c&oe=60BC6A03&_nc_sid=55937d', 'is_private': False, 'is_verified': False, 'followed_by_viewer': True, 'follows_viewer': False, 'requested_by_viewer': False, 'reel': {'id': '2277559750', 'expiring_at': 1620492146, 'has_pride_media': False, 'latest_reel_media': 0, 'seen': None, 'owner': {'__typename': 'GraphUser', 'id': '2277559750', 'profile_pic_url': 'https://instagram.fbwa1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/162097909_958382568239924_7239158560191763387_n.jpg?tp=1&_nc_ht=instagram.fbwa1-1.fna.fbcdn.net&_nc_ohc=Klga3Ka2jbgAX_KrNHX&edm=ANg5bX4BAAAA&ccb=7-4&oh=6dab383cbcd3b7f02d338c7f2e781f6c&oe=60BC6A03&_nc_sid=55937d', 'username': 'sabbu.balami'}}}}, {'node': {'id': '3186950590', 'username': '__bomzan_', 'full_name': '𝒷𝑜𝓂𝒷🦄', 'profile_pic_url': 'https://instagram.fbwa1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/180747852_781027082617482_5601735959734376723_n.jpg?tp=1&_nc_ht=instagram.fbwa1-1.fna.fbcdn.net&_nc_ohc=KZXN_dvB_EMAX8_lkwv&edm=ANg5bX4BAAAA&ccb=7-4&oh=f17a4d299fd77dfa744b7ec3e127e266&oe=60B9BB28&_nc_sid=55937d', 'is_private': True, 'is_verified': False, 'followed_by_viewer': True, 'follows_viewer': False, 'requested_by_viewer': False, 'reel': {'id': '3186950590', 'expiring_at': 1620492146, 'has_pride_media': False, 'latest_reel_media': 1620376603, 'seen': None, 'owner': {'__typename': 'GraphUser', 'id': '3186950590', 'profile_pic_url': 'https://instagram.fbwa1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/180747852_781027082617482_5601735959734376723_n.jpg?tp=1&_nc_ht=instagram.fbwa1-1.fna.fbcdn.net&_nc_ohc=KZXN_dvB_EMAX8_lkwv&edm=ANg5bX4BAAAA&ccb=7-4&oh=f17a4d299fd77dfa744b7ec3e127e266&oe=60B9BB28&_nc_sid=55937d', 'username': '__bomzan_'}}}}, {'node': {'id': '581735705', 'username': 'emirafoods', 'full_name': 'EmiraFoods', 'profile_pic_url': 'https://instagram.fbwa1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/122085310_801151230618969_1720564294373348620_n.jpg?tp=1&_nc_ht=instagram.fbwa1-1.fna.fbcdn.net&_nc_ohc=j3QozGD7nLcAX8WT-eU&edm=ANg5bX4BAAAA&ccb=7-4&oh=33ffce5c3c66fe1a0461ae975e43877b&oe=60B97B03&_nc_sid=55937d', 'is_private': False, 'is_verified': False, 'followed_by_viewer': True, 'follows_viewer': False, 'requested_by_viewer': False, 'reel': {'id': '581735705', 'expiring_at': 1620492146, 'has_pride_media': False, 'latest_reel_media': 1620364018, 'seen': None, 'owner': {'__typename': 'GraphUser', 'id': '581735705', 'profile_pic_url': 'https://instagram.fbwa1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/122085310_801151230618969_1720564294373348620_n.jpg?tp=1&_nc_ht=instagram.fbwa1-1.fna.fbcdn.net&_nc_ohc=j3QozGD7nLcAX8WT-eU&edm=ANg5bX4BAAAA&ccb=7-4&oh=33ffce5c3c66fe1a0461ae975e43877b&oe=60B97B03&_nc_sid=55937d', 'username': 'emirafoods'}}}}, {'node': {'id': '1231106130', 'username': 'drishtikoirala', 'full_name': 'दृष्टि कोइराला', 'profile_pic_url': 'https://instagram.fbwa1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/181804068_990933561651024_8460106980772548262_n.jpg?tp=1&_nc_ht=instagram.fbwa1-1.fna.fbcdn.net&_nc_ohc=SXHqlJnztEMAX_9vF7u&edm=ANg5bX4BAAAA&ccb=7-4&oh=0d0861f25a914362f28572671d867d31&oe=60B9C918&_nc_sid=55937d', 'is_private': True, 'is_verified': False, 'followed_by_viewer': True, 'follows_viewer': False, 'requested_by_viewer': False, 'reel': {'id': '1231106130', 'expiring_at': 1620492146, 'has_pride_media': False, 'latest_reel_media': 1620364354, 'seen': None, 'owner': {'__typename': 'GraphUser', 'id': '1231106130', 'profile_pic_url': 'https://instagram.fbwa1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/181804068_990933561651024_8460106980772548262_n.jpg?tp=1&_nc_ht=instagram.fbwa1-1.fna.fbcdn.net&_nc_ohc=SXHqlJnztEMAX_9vF7u&edm=ANg5bX4BAAAA&ccb=7-4&oh=0d0861f25a914362f28572671d867d31&oe=60B9C918&_nc_sid=55937d', 'username': 'drishtikoirala'}}}}]}}}, 'status': 'ok'}
# pprint(data)
# https://www.instagram.com/graphql/query/?query_hash=3dec7e2c57367ef3da3d987d89f9dbc8&variables=%7B%22id%22%3A%2244503193972%22%2C%22include_reel%22%3Atrue%2C%22fetch_mutual%22%3Afalse%2C%22first%22%3A24%7D
# https://www.instagram.com/graphql/query/?%7B%22query_hash%22:%20%223dec7e2c57367ef3da3d987d89f9dbc8%22,%20%22variables%22:%20%7B%22id%22:%20%2244503193972%22,%20%22include_reel%22:%20true,%20%22fetch_mutual%22:%20false,%20%22first%22:%2024%7D%7D

# # with after query
# https://www.instagram.com/graphql/query/?query_hash=3dec7e2c57367ef3da3d987d89f9dbc8&variables=%7B%22id%22%3A%222253976586%22%2C%22include_reel%22%3Atrue%2C%22fetch_mutual%22%3Afalse%2C%22first%22%3A12%2C%22after%22%3A%22QVFCYlk2X0xSaThfcDhiUXhOa1JBdFB5WE1PZXd1eExsZTVwSmlDZTFsa0pJbWw3UkVLX3lxUXA0RWNTNHUwUUtQY1RYSVlGUkZZWTZGaC00OWNrWmhVUw%3D%3D%22%7D

# query_headers = {
#     "referer": f"https://www.instagram.com/{self.uid}/",
#     "x-csrftoken": self.csrf,
#     "x-requested-with": "XMLHttpRequest",
#     "x-ig-app-id": "936619743392459"
# }
# import json
# q_data = {"query_hash": "3dec7e2c57367ef3da3d987d89f9dbc8","variables":{"id":"2253976586","include_reel":True,"fetch_mutual":False,"first":24,"after":"QVFDLVJnZk1zSm43NHY2RmRHWWJWV0JoUEZsWjRtSVFNTEwwbjVhM0ZxTm80a0dTS1J3RDM5d3pMXzd4bEVyWFA3RGlkcjlYVnYySWIxYlIxR2g2Vjlfcw=="}}
# url = 'https://www.instagram.com/graphql/query/'

# q_url = requests.get('https://www.instagram.com/graphql/query/?query_hash=3dec7e2c57367ef3da3d987d89f9dbc8',data=json.dumps(q_data))
# print(q_url.status_code)
# print(q_url.url)
# print(q_url.headers)

# e_url = urlencode(q_data)
# print(e_url)
'''
quote_1 = quote(q_data["variables"]["after"])
print(quote_1)

final_url = url + e_url
print(final_url.replace('+',''))
given_url = f'https://www.instagram.com/graphql/query/?query_hash=3dec7e2c57367ef3da3d987d89f9dbc8&variables=%7B%22id%22%3A%22{q_data["variables"]["id"]}%22%2C%22include_reel%22%3Atrue%2C%22fetch_mutual%22%3Afalse%2C%22first%22%3A13%2C%22after%22%3A%22QVFCbHRETFlheVpxcm9LbkNBZ3owdXRCbnVSWk54aURVOFZvbFJGRF9xckJpNzBVb2EyVmZtUnRxOEtJNUtTOTQ0UFVhck5vaDczZ05ydlBTc0tGR29aQQ%3D%3D%22%7D'
print(given_url)
next_url = f'https://www.instagram.com/graphql/query/?query_hash=3dec7e2c57367ef3da3d987d89f9dbc8&variables=%7B%22id%22%3A%22{q_data["variables"]["id"]}%22%2C%22include_reel%22%3Atrue%2C%22fetch_mutual%22%3Afalse%2C%22first%22%3A12%2C%22after%22%3A%22{quote(q_data["variables"]["after"])}%22%7D'
print('next : '+next_url)
q_data["variables"]["first"] = 80
print(q_data)

ul = '%7B%27id%27%3A+%272244503193972%27%2C+%27include_reel%27%3A+True%2C+%27fetch_mutual%27%3A+False%2C+%27first%27%3A+24%2C+%27after%27%3A+%27QVFCYlk2X0xSaThfcDhiUXhOa1JBdFB5WE1PZXd1eExsZTVwSmlDZTFsa0pJbWw3UkVLX3lxUXA0RWNTNHUwUUtQY1RYSVlGUkZZWTZGaC00OWNrWmhVUw%3D%3D%27%7D'
ol = '%7B%22id%22%3A%222253976586%22%2C%22include_reel%22%3Atrue%2C%22fetch_mutual%22%3Afalse%2C%22first%22%3A24%7D'
'''
# def jack(val = 1):
#     if isinstance(val,bool):
#         print('jack')

# jack()
def fag(jack=None,is_video=False):
<<<<<<< HEAD
    url = 'https://www.instagram.com/p/CM82JSksC7LzsL_-2dpLbJxjCEtdwCA8nbHrOI0/?utm_source=ig_web_copy_link'
=======
    url = 'https://www.instagram.com/p/CPcOXXVLME-/?utm_source=ig_web_copy_link'
>>>>>>> 07b36bcb368b3163609ac876dec26172a61044ee
    _url = urlsplit(url)
    if not urlsplit(url).path.startswith('/p/'):
        print('fag')
    else:
<<<<<<< HEAD
        print(_url.path.lstrip('/p/').rstrip('/'))
        print('..............')
=======
>>>>>>> 07b36bcb368b3163609ac876dec26172a61044ee
        new_url = _url.scheme + '://'+ _url.netloc+ _url.path
        print(new_url)

    if not (_url.netloc == 'www.instagram.com'):
        print('js')
    else:
        print('psych')
    if jack:
        print('jacl none')
    else:
        print('bang')
    if is_video is False:
        print('hello')
    else:
        print('fag')
    # print(type(requests.get('https://cloud.google.com/blog/products/application-development/rest-vs-rpc-what-problems-are-you-trying-to-solve-with-your-apis').content))
# print(urljoin(urlsplit(url).scheme,urlsplit(url).netloc,urlsplit(url).path))

fag()
if None:
    print('sag')


# import json,requests,asyncio,aiohttp
# header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36 Edg/84.0.522.61'}
# data = requests.get('https://www.instagram.com/p/CGNQsz4g4Kx/?__a=1',headers=header)
# print(data.status_code)
# cont = json.dumps(data.json(),indent=2)
# with open('post_data.json','w') as file:
#     file.write(cont)
<<<<<<< HEAD
# import time
# start_t = time.time()
# data = requests.get('https://instagram.fktm3-1.fna.fbcdn.net/v/t51.2885-15/sh0.08/e35/s640x640/199149591_202779401696209_1809620098758956202_n.jpg?tp=1&_nc_ht=instagram.fktm3-1.fna.fbcdn.net&_nc_cat=101&_nc_ohc=lmsik8raE_kAX-L27r6&edm=AP_V10EBAAAA&ccb=7-4&oh=73cf826b2a87adeb05aae8e027708ceb&oe=60CA9063&_nc_sid=4f375e')
# print(data.status_code)
# print(data.content)
# print(data.text)
# data =
=======
import time
start_t = time.time()
data = requests.get('https://instagram.fktm3-1.fna.fbcdn.net/v/t51.2885-15/sh0.08/e35/s640x640/199149591_202779401696209_1809620098758956202_n.jpg?tp=1&_nc_ht=instagram.fktm3-1.fna.fbcdn.net&_nc_cat=101&_nc_ohc=lmsik8raE_kAX-L27r6&edm=AP_V10EBAAAA&ccb=7-4&oh=73cf826b2a87adeb05aae8e027708ceb&oe=60CA9063&_nc_sid=4f375e')
print(data.status_code)
print(data.content)
print(data.text)
data =
>>>>>>> 07b36bcb368b3163609ac876dec26172a61044ee
# diff = time.time() - start_t
# print(diff)
# json_d = json.loads(json.dumps(edges_to))
# print(type(json_d))
'''
def writeVideo(filename:str,filecontent:bytes):
    if not filename.endswith('.mp4'):
        with open(filename+'.mp4','wb') as videof:
            videof.write(filecontent)

    else:
        with open(filename,'wb') as videof:
            videof.write(filecontent)

def writeImage(filename:str, filecontent:bytes):
        if not filename.endswith('.jpg'):
            with open(filename+'.jpg','wb') as videof:
                videof.write(filecontent)

        else:
            with open(filename,'wb') as videof:
                videof.write(filecontent)

async def download_site(session,url):
    async with session.get(url) as response:
        graph_data = await response.json()


async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
    # async with httpx.AsyncClient() as session:

#can share session across all tasks so created as contxt mangr; running on same thread; no interruptio;if session in bad state
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(session,url)) #creatinng list of tasks;also takes care of starting them
            tasks.append(task)
        await asyncio.gather(*tasks,return_exceptions=True) #to keep sesssion contxt alive until the tsks have been completed

if __name__=="__main__":
    sites = ['https://realpython.com/intro-to-python-threading/','https://developer.mozilla.org/en-US/docs/Learn/CSS'] * 60
    start_t = time.time()
    asyncio.get_event_loop().run_until_complete(download_all_sites(sites)) #can also use asyncio.run()
    duration = time.time() - start_t
    print(f"It took {duration} seconds to download {len(sites)} sitess")

'''
<<<<<<< HEAD

#request post url
# https://www.instagram.com/graphql/query/?query_hash=971f52b26328008c768b7d8e4ac9ce3c&variables=%7B%22shortcode%22%3A%22ByC3cvilSp8OT3YJ8vKd3qN7Xdyi453WOQi4tM0%22%2C%22child_comment_count%22%3A3%2C%22fetch_comment_count%22%3A40%2C%22parent_comment_count%22%3A24%2C%22has_threaded_comments%22%3Atrue%7D
# https://www.instagram.com/graphql/query/?query_hash=971f52b26328008c768b7d8e4ac9ce3c&variables=%7B%22shortcode%22%3A%22CQIiMfKsAOo%22%2C%22child_comment_count%22%3A3%2C%22fetch_comment_count%22%3A40%2C%22parent_comment_count%22%3A24%2C%22has_threaded_comments%22%3Atrue%7D
=======
>>>>>>> 07b36bcb368b3163609ac876dec26172a61044ee
