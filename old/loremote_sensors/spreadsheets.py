from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from oauth2client.service_account import ServiceAccountCredentials
import datetime

MY_SPREADSHEET_ID = '1d3v3sRYEgFiG7JHmL9lileLnNTXUOcU2qMFZ_rgCFjQ'


SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
creds = ServiceAccountCredentials.from_json_keyfile_name(
        '../token.json', SCOPES)
service = build('sheets', 'v4', http=creds.authorize(Http()))

values = [ [ str(datetime.datetime.now()),
    'Temperature', "1.0", 'Pressure', "1.1", 'Humidity', "1.2" ] ]
body = { 'values': values }

sheetname="data"

service.spreadsheets().values().append(
            spreadsheetId=MY_SPREADSHEET_ID,
            range=sheetname + '!A1:G1',
            valueInputOption='USER_ENTERED',
            insertDataOption='INSERT_ROWS',
            body=body).execute()
