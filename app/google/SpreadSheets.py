import gspread
from oauth2client.service_account import ServiceAccountCredentials
from app import config


def get_connection_to_g_api():
    scope = ['https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name(config.SPREAD_SHEET_CREDENTIALS_FILE_PATH, scope)
    return gspread.authorize(credentials)
