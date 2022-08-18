import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')    
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')


def get_sales_data():
    """
    Get sales figures from the user
    """
    print("PLease enter sales data fromthe last market.")
    print("Data should be six numbers, seperated by commas")
    print("Example: 10,20,30,40,50,60\n")

    data_str = input("enter your data here: ")

    sales_data= data_str.split(",")
    validate_data(sales_data)

def validate_data(values):
    print(values)
    """
    Inside the try, converts all string values into integers.
    Raises ValueErrors if strings cannot be converted to int,
    or if there arnt exactly six numbers
    """ 
    try:
        if len(values) != 6:
            raise ValueError(f"exactly 6 values required.You provided {len(values)}")  
        
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")

get_sales_data()