import requests
from bs4 import BeautifulSoup
from datetime import datetime
from pprint import pprint
import json
import asyncio, aiohttp
from urllib.parse import quote, urlsplit


class InstaContent:
    def __enter__(self):
        return self

    def __exit__(self,*args):
        self.close()

    def __init__(self, uid:str, password:str) -> None:

        self.uid = uid
        self.password = password

        self.headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51"
        }
        self.login_url = 'https://www.instagram.com/accounts/login/ajax/'

        self.time = int(datetime.now().timestamp())

        # instead of encrypted password
        payload = {
            'username': self.uid,
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{self.time}:{self.password}',
            'queryParams': {},
            'optIntoOneTap': 'false'
        }
        self.instaS = requests.session()



        # with requests.session() as self.instaS:
        login_cont = self.instaS.get('https://www.instagram.com/accounts/login/',headers=self.headers)
        self.csrf = login_cont.cookies['csrftoken']
        self.login_headers = {
            "x-requested-with": "XMLHttpRequest",
            "referer": "https://www.instagram.com/accounts/login/",
            "x-csrftoken": self.csrf
        }
        print(payload)
        login_resp = self.instaS.post(self.login_url,data=payload,headers={**self.headers,**self.login_headers})
        print(login_resp.status_code)
        self.userId = login_resp.json()['userId'] #numerical user id stored in insta
        print(self.userId)
        # pprint(login_resp.headers)

        # self.followers()


    def followers(self,unfollowers_only:bool=False)-> list:

        if not isinstance(unfollowers_only,bool):
            raise TypeError("The unfollowers_only value should be boolean(i.e. True or False)")

        followers_list = []

        # q_data = {
        # "query_hash": "3dec7e2c57367ef3da3d987d89f9dbc8",
        # "variables": {"id":self.userId,"include_reel":True,"fetch_mutual":False,"first":24}
        # }

        query_headers = {
            "referer": f"https://www.instagram.com/{self.uid}/",
            "x-csrftoken": self.csrf,
            "x-requested-with": "XMLHttpRequest",
            "x-ig-app-id": "936619743392459"
        }

        #the first url with which the other urls will be figured out
        #can't find proper url encoding to pass queries seperately
        follower_pg = self.instaS.get(f'https://www.instagram.com/graphql/query/?query_hash=3dec7e2c57367ef3da3d987d89f9dbc8&variables=%7B%22id%22%3A%22{self.userId}%22%2C%22include_reel%22%3Atrue%2C%22fetch_mutual%22%3Afalse%2C%22first%22%3A24%7D',headers={**self.headers,**query_headers})
        pg_details = follower_pg.json()["data"]["user"]["edge_follow"]

        if unfollowers_only:
            for nodes in pg_details["edges"]:
                if not nodes["node"]["follows_viewer"]:
                    followers_list.append({nodes["node"]["username"] : f'https://www.instagram.com/{nodes["node"]["username"]}/'})

        else:
            for nodes in pg_details["edges"]:
                followers_list.append({nodes["node"]["username"] : f'https://www.instagram.com/{nodes["node"]["username"]}/'})


        has_next_pg = pg_details["page_info"]["has_next_page"]
        print(has_next_pg)
        after_c = pg_details["page_info"]["end_cursor"]



        # URLs following the main to get remaining data of user following
        while has_next_pg:

            remain_query = self.instaS.get(f'https://www.instagram.com/graphql/query/?query_hash=3dec7e2c57367ef3da3d987d89f9dbc8&variables=%7B%22id%22%3A%22{self.userId}%22%2C%22include_reel%22%3Atrue%2C%22fetch_mutual%22%3Afalse%2C%22first%22%3A12%2C%22after%22%3A%22{quote(after_c)}%22%7D',headers={**self.headers,**query_headers})
            print(remain_query.status_code)

            pg_details = remain_query.json()["data"]["user"]["edge_follow"]
            if unfollowers_only:
                for nodes in pg_details["edges"]:
                    if not nodes["node"]["follows_viewer"]:
                        followers_list.append({nodes["node"]["username"] : f'https://www.instagram.com/{nodes["node"]["username"]}/'})

            else:
                for nodes in pg_details["edges"]:
                    followers_list.append({nodes["node"]["username"] : f'https://www.instagram.com/{nodes["node"]["username"]}/'})

            has_next_pg = pg_details["page_info"]["has_next_page"]
            print(has_next_pg)
            after_c = pg_details["page_info"]["end_cursor"]

        return followers_list

    #using __a=1 as query param to get graph json
    def downloadPost(self,url:str,filename = None) -> bool:

        _url = urlsplit(url)
        if not _url.path.startswith('/p/'):
            raise Exception("The url is incorrect")
        else:

            new_url = _url.scheme + '://'+ _url.netloc+ _url.path #restructuring the url without any query
            short_code_id = _url.path.lstrip('/p/').rstrip('/')
            headers = {
            "referer": new_url,
            "x-csrftoken": self.csrf,
            "x-requested-with": "XMLHttpRequest",
            "x-ig-app-id": "936619743392459"
            }

            self.instaS.headers.update(headers | self.headers)
            _get_graph = self.instaS.get(f'https://www.instagram.com/graphql/query/?query_hash=971f52b26328008c768b7d8e4ac9ce3c&variables=%7B%22shortcode%22%3A%22{short_code_id}%22%2C%22child_comment_count%22%3A3%2C%22fetch_comment_count%22%3A40%2C%22parent_comment_count%22%3A24%2C%22has_threaded_comments%22%3Atrue%7D')


            if _get_graph.status_code == 200:
                _api_data = _get_graph.json()["data"]["shortcode_media"]

                #If doesn't have multiple images/videos in one
                if not (_api_data["__typename"] == "GraphSidecar"):
                    if _api_data["is_video"]:
                        video_cont = self.instaS.get(_api_data["video_url"])
                        if filename is None:
                            InstaContent.writeVideo(_api_data["shortcode"],video_cont.content)
                        else:
                            InstaContent.writeVideo(filename,video_cont.content)

                    else:
                        image_cont = self.instaS.get(_api_data["display_url"])
                        if filename is None:
                            InstaContent.writeImage(_api_data["shortcode"],image_cont.content)
                        else:
                            InstaContent.writeImage(filename,image_cont.content)
                else:
                    all_sidecar = _api_data["edge_sidecar_to_children"]["edges"]
                    # print('test')
                    if filename is None:
                        asyncio.get_event_loop().run_until_complete(self.get_all_medias(all_sidecar,_api_data["shortcode"]))
                    else:
                        asyncio.get_event_loop().run_until_complete(self.get_all_medias(all_sidecar,filename))

                    # print('done')

                    """Synchronous Version"""
                    # for position,nodes in enumerate(all_sidecar):
                    #     node_data = nodes["node"]

                    #     if node_data["is_video"]:
                    #         video_cont = self.instaS.get(node_data["video_url"])
                    #         InstaContent.writeVideo(str(node_data["id"])+"_"+str(position),video_cont.content)
                    #     else:
                    #         image_cont = self.instaS.get(node_data["display_url"])
                    #         InstaContent.writeImage(str(node_data["id"])+"_"+str(position),image_cont.content)



            # print(_get_graph.headers)
            # print(_get_graph.json())


    #work with single media file
    async def get_single_media(self,session,url:str,position:int,filename:str,is_video:bool=False):
        async with session.get(url) as response:
            print(url)
            print(position)
            print(is_video)
            # print(filecontent.headers)
            # print(filecontent.status_code)
            if is_video is True:
                filecontent = await response.read()
                print(filecontent)
                print('true')
                InstaContent.writeVideo(filename+str(position)+'.mp4',filecontent)
            elif is_video is False:
                filecontent = await response.read()
                print('false is image')
                InstaContent.writeImage(filename+str(position)+'.jpg',filecontent)

    async def get_all_medias(self,sites_edges:list,filename:str)->None: #get list of all sidecar edges of post with multiple images
        async with aiohttp.ClientSession(headers=self.headers) as session:
            tasks = []
            for position, url in enumerate(sites_edges):
                node_data = url["node"]
                # print(position)
                # print(node_data["is_video"])
                if node_data["is_video"]:
                    print(node_data["video_url"])
                    task = asyncio.ensure_future(self.get_single_media(session,node_data["video_url"],position,filename,is_video=node_data["is_video"])) #concurrent run
                else:
                    print(node_data["display_url"])
                    task = asyncio.ensure_future(self.get_single_media(session,node_data["display_url"],position,filename,is_video=node_data["is_video"])) #concurrent run
                tasks.append(task)

            await asyncio.gather(*tasks,return_exceptions=True)


    def downloadMultiple(self,url:str):
        pass

    @staticmethod
    def writeVideo(filename:str,filecontent:bytes):
        if not filename.endswith('.mp4'):
            with open(filename+'.mp4','wb') as videof:
                videof.write(filecontent)

        else:
            with open(filename,'wb') as videof:
                videof.write(filecontent)

    @staticmethod
    def writeImage(filename:str, filecontent:bytes):
        if not filename.endswith('.jpg'):
            with open(filename+'.jpg','wb') as videof:
                videof.write(filecontent)

        else:
            with open(filename,'wb') as videof:
                videof.write(filecontent)






if __name__ == "__main__":
    obj = InstaContent('username','password') # Enter username and password
    # unfollowers_data = obj.followers(unfollowers_only=True) #to get the list of unfollowers only
    # pprint(unfollowers_data)
    obj.downloadPost('url',filename=None)













