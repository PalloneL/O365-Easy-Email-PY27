from lib2to3.pgen2 import token
import requests
import json

class O365Easy:

    def __init__(self):
        self.clientToken = ''

    def Get_Token_Data(self, app_id, client_secret, tenant_id, email, password):
        token_data = {
        'grant_type': 'password',
        'client_id':app_id,
        'client_secret':client_secret,
        'resource':'https://graph.microsoft.com',
        'scope':'https://graph.microsoft.com',
        'username':email,
        'password':password,
        }
        #print(token_data)
        token_url = "https://login.microsoftonline.com/{}/oauth2/token".format(tenant_id)
        print(token_url)
        token_r = requests.post(token_url, data=token_data)
        clientToken = token_r.json().get('access_token')
        self.clientToken=clientToken
    
    #---id is an optional parameter if you know the id of an email you're looking for.---#
    def getMessages(self, id=None):
        users_url = ''
        if id:
            users_url = 'https://graph.microsoft.com/v1.0/me/mailFolders/inbox/messages/{}'.format(id)
        else:
            users_url = 'https://graph.microsoft.com/v1.0/me/mailFolders/inbox/messages'
        headers = {
        'Authorization': 'Bearer {}'.format(self.clientToken),
        'Prefer': 'outlook.body-content-type="html"'
        }
        print(headers)
        user_response_data = json.loads(requests.get(users_url, headers=headers).text)
        print(user_response_data)
        return(user_response_data['value'])
    
    #---The delete should return a 204 code if a message is sucessfully deleted---#
    def deleteMessage(self, id):
        users_url = 'https://graph.microsoft.com/v1.0/me/mailFolders/inbox/messages/{}'.format(id)
        headers = {
        'Authorization': 'Bearer {}'.format(self.clientToken)
        }
        user_response_data = requests.delete(users_url, headers=headers)
        print(user_response_data)
