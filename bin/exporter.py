import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from apiclient.http import MediaFileUpload
from oauth2client import file, client, tools
from httplib2 import Http

def flowCreate():
    SCOPES = [ 'https://www.googleapis.com/auth/drive']
    store = file.Storage('credentials.json')
    creds = None

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return creds

def upload(filename):
    memt = 'text/plain'
    if(filename.split('.')[-1] == 'csv'):
        memt = 'text/csv'
        

    creds = flowCreate()
    drive_service = build('drive', 'v3', credentials=creds)

    file_metadata = {'name': filename }
    media = MediaFileUpload('dataset/' + filename, mimetype=memt)

    file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()

    print ('File ID: %s' % file.get('id'))
    return true