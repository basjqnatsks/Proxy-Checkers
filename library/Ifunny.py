
import requests
from typing import Union
class Ifunny():
    def __init__(self):
        self.API_BASE = 'https://api.ifunny.mobi/v4'
        self.AUTHTOKEN = None
        self.HEADERS = None



    def set_header(self) -> None:
        self.HEADERS = {
            "Host": "api.ifunny.mobi",
            "Content-Length" : "0",
            "Connection": "keep-alive",
            "Accept": "video/mp4, image/jpeg",
            "iFunny-Project-Id": "iFunny",
            "User-Agent": 'iFunny/5.34.1(9137) iphone/12.1 (Apple; iPhone11,2)',
            "Accept-Language": "en-US;q=1",
            "Authorization": "Bearer " + str(self.AUTHTOKEN),
            "Accept-Encoding": "br, gzip, deflate",
        }
        
    def login(self, email : str = None, password : str = None, Token : str = None) -> Union[str, bytearray]:
        
        if email and password:
            DATA = {
                "grant_type": "password",
                "username": email,
                "password": password
            }
            del email, password
            TEMPHEADERS = {
            "Host": "api.ifunny.mobi",
            'ApplicationState': '1',
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
            "Content-Length" : "0",
            "Connection": "keep-alive",
            "Accept": "video/mp4, image/jpeg",
            "iFunny-Project-Id": "iFunny",
            "User-Agent": 'iFunny/5.34.1(9137) iphone/12.1 (Apple; iPhone11,2)',
            "Accept-Language": "en-US;q=1",
            "Authorization": 'Basic YTExNDk4N2U3ZmI0NWJiMmI3NTcxOGNiODQ4NjkyNTgzNzIyY2VjYTU3MTkwNTY2OGE2Y2E5OWE4ODFjY2IyMV9KdWlVSCYzODIyOjk2NjQ2YTJmNjQ1ZGI0YjUwMWNmMTQ0ZTFmODY4ZjM5NDU5ZDMzNmQ=',
            "Accept-Encoding": "br, gzip, deflate",
            }
            RESPONSE = requests.post(self.API_BASE+"/oauth2/token", data=DATA, headers=TEMPHEADERS).json()
            try:
                self.AUTHTOKEN  = RESPONSE['access_token']
            except KeyError:
                print("RESPONSE JSON: " + str(RESPONSE) )
                raise KeyError("Failed Json Respones")
            self.set_header()
            return RESPONSE

        elif Token:
            self.AUTHTOKEN = Token
            del Token
            self.set_header()
            return self.AUTHTOKEN

        else:
            raise UserWarning("Impropper Login Function")

    def delete_smile_comment(self, CONTENTID : str, COMMENTID: str) -> Union[bytearray, bool]:
        if CONTENTID and COMMENTID and self.AUTHTOKEN:
            return requests.delete(self.API_BASE + '/content/' + CONTENTID + '/comments/' + COMMENTID + '/smiles', headers=self.HEADERS).json()
        else:
            return False

    def put_add_smile_comment(self, CONTENTID : str, COMMENTID: str) -> Union[bytearray, bool]:
        if CONTENTID and COMMENTID:
            return requests.put(self.API_BASE + '/content/' + CONTENTID + '/comments/'+ COMMENTID + '/smiles', headers=self.HEADERS).json()
        else:
            return False




    def delete_smile(self, CONTENTID: str, fromLoc: str = 'coll') -> Union[bytearray, bool]:
        if CONTENTID:
            return requests.delete(self.API_BASE + '/content/' + CONTENTID + '/smiles?from=' + fromLoc, headers=self.HEADERS).json()
        else:
            return False


    def put_add_smile(self, CONTENTID: str, fromLoc: str = 'coll') -> Union[bytearray, bool]:
        if CONTENTID:
            print(self.HEADERS)
            return requests.put(self.API_BASE + '/content/' + CONTENTID + '/smiles?from=' + fromLoc, headers=self.HEADERS).json()
        else:
            return False
   
"""




import requests, time, json, random

class API:
 
    API_BASE = 'https://api.ifunny.mobi/'
    API_VERSION = 'v4'
    DEFAULT_AUTH_TOKEN = 'NThGQ0Q5NkZFRDQ2RTkwN0NFODNEN0Y3QzM1QjYyRTc0QjVEMTE2REI4NEEyREE0OUZGQUI1MjA5NTQyQTBGQV9Nc09JSjM5UTI4OjY0MDcwYThkZjM3ZTk5NjE5OWVkNWUyNjdiN2E2OTNjYTFjN2E2ODM='
    DEFAULT_USER_AGENT = 'iFunny/5.34.1(9137) iphone/12.1 (Apple; iPhone11,2)'
 
    def __init__(self, AUTH_TOKEN=None, API_BASE=API_BASE, API_VERSION=API_VERSION, DEFAULT_AUTH_TOKEN=DEFAULT_AUTH_TOKEN, DEFAULT_USER_AGENT=DEFAULT_USER_AGENT):
        self.API_BASE = API_BASE
        self.API_VERSION = API_VERSION
        self.API_URL = API_BASE + API_VERSION
        self.DEFAULT_AUTH_HEADER = 'Basic ' + DEFAULT_AUTH_TOKEN
        self.DEFAULT_USER_AGENT = DEFAULT_USER_AGENT
        self.AUTH_TOKEN = AUTH_TOKEN
 
    def get_headers(self):
        if self.AUTH_TOKEN:
            headers = {
                "Host": "api.ifunny.mobi",
                "Content-Length" : "0",
                "Connection": "keep-alive",
                "Accept": "video/mp4, image/jpeg",
                "iFunny-Project-Id": "iFunny",
                "User-Agent": self.DEFAULT_USER_AGENT,
                "Accept-Language": "en-US;q=1",
                "Authorization": "Bearer " + self.AUTH_TOKEN,
                "Accept-Encoding": "br, gzip, deflate",

            }
        else:
            headers = {
                "Authorization": self.DEFAULT_AUTH_HEADER,
                "user-agent": self.DEFAULT_USER_AGENT
            }
        return headers
 
    def do_get(self, endpoint, params=None):
        headers = self.get_headers()
        url = self.API_URL + endpoint
        res = requests.get(url, params=params, headers=headers)
        return res.json()
 
    def do_post(self, endpoint, data=None, files=None):
        headers = self.get_headers()
        url = self.API_URL + endpoint
        print(url)
        res = requests.post(url, data=data, files=files, headers=headers)
        return res.json()
 
    def do_put(self, endpoint, data=None, params=None):
        headers = self.get_headers()
        url = self.API_URL + endpoint
        print(url)
        print(params)
        print(headers)
        res = requests.put(url, data=data, params=params, headers=headers)
        return res.json()
 
    def do_delete(self, endpoint):
        headers = self.get_headers()
        url = self.API_URL + endpoint
        res = requests.delete(url, headers=headers)
        return res.json()
 
    def login(self, email, password):
        if self.AUTH_TOKEN is None:
            data = {
                "grant_type": "password",
                "username": email,
                "password": password
            }
            #res = self.do_post('/oauth2/token', data)
            #print(res)

            self.AUTH_TOKEN = 'da21338914540bfb336a64533fb1969738e8def6073b781c828f40d08b536474' #res['access_token']
            return self.AUTH_TOKEN
        else:
            return self.AUTH_TOKEN
   
    def get_account(self):
        if self.AUTH_TOKEN:
            return self.do_get('/account')
        else:
            return False
   
    def nick_exists(self, nick):
        res = self.do_get('/users/nicks_available', params={ 'nick': nick })
        return res['data']['available']
   
    def sugguest_tags(self, query=None):
        if query:
            return self.do_get('/tags/suggested', params={'q': query })
        else:
            return False
   
    def get_memes(self, limit=48, category=None):
        if category == 'popular' or category == 'new':
            return self.do_get('/sources/memes', params={'limit': limit, 'cat': category})
        else:
            return self.do_get('/sources/memes', params={'limit': limit})
   
    def get_task_status(self, taskID):
        return self.do_get('/tasks/' + taskID)
   
    def get_content(self, contentID):
        return self.do_get('/content/' + contentID)
   
    def get_content_comments(self, contentID, limit=40):
        return self.do_get('/content/' + contentID + '/comments', params={'limit': limit})
   
    def post_content(self, image, type='pic', tags=[], top_text=None, bottom_text=None):
        data = {
            "type": type,
            "tags": json.dumps(tags),
            "top_text": top_text,
            "bottom_text": bottom_text
        }
        files = {
            "image": open(image, 'rb')
        }
        return self.do_post('/content', data=data, files=files)
 
    def post_feeds_collective(self, limit=20):
        return self.do_post('/feeds/collective', data={'limit': limit})
   
    def post_comment(self, contentID, text=None):
        if contentID and text:
            return self.do_post('/content/' + contentID + '/comments', data={'text':text})
        else:
            return False
   
    def put_add_smile(self, contentID, fromLoc='coll'):
        if contentID:
            return self.do_put('/content/' + contentID + '/smiles?from=' + fromLoc)
        else:
            return False
   
    def put_add_unsmile(self, contentID, fromLoc='coll'):
        if contentID:
            return self.do_put('/content/' + contentID + '/unsmiles?from=' + fromLoc)
        else:
            return False
   
    def put_add_smile_comment(self, contentID, commentID):
        if contentID and commentID:
            return self.do_put('/content/' + contentID + '/comments/'+ commentID + '/smiles')
        else:
            return False
   
    def put_add_unsmile_comment(self, contentID, commentID):
        if contentID and commentID:
            return self.do_put('/content/' + commentID + '/comments/' + contentID + '/unsmiles')
        else:
            return False
   
    def delete_smile(self, contentID, fromLoc='coll'):
        if contentID:
            return self.do_delete('/content/' + contentID + '/smiles?from=' + fromLoc)
        else:
            return False
   
    def delete_unsmile(self, contentID, fromLoc='coll'):
        if contentID:
            return self.do_delete('/content/' + contentID + '/unsmiles?from=' + fromLoc)
        else:
            return False
   
    def delete_smile_comment(self, contentID, commentID):
        if contentID and commentID:
            return self.do_delete('/content/' + contentID + '/comments/' + commentID + '/smiles')
        else:
            return False
   
    def delete_unsmile_comment(self, contentID, commentID):
        if contentID and commentID:
            return self.do_delete('/content/' + contentID + '/comments/' + commentID + '/unsmiles')





"""