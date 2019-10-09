import httplib2
import os

from apiclient import discovery
from google.oauth2 import service_account


def addSong(values):
    scopes = ["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/spreadsheets"]
    secret_file = os.path.join(os.getcwd(), 'client_secret.json')

    spreadsheet_id = '1NdG2fO5OUq2YLKYFZeUlzfVrXLBXLEc-eV5bwDf7HcU'
    range_name = 'A1:B1'

    credentials = service_account.Credentials.from_service_account_file(secret_file, scopes=scopes)
    service = discovery.build('sheets', 'v4', credentials=credentials)

    data = {
        'values' : [values]
    }

    service.spreadsheets().values().append(spreadsheetId=spreadsheet_id, body=data, range=range_name, valueInputOption='USER_ENTERED').execute()