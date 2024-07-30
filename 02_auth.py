from dotenv import load_dotenv
load_dotenv()

import os
from supabase import create_client, Client
from gotrue.errors import AuthApiError

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

supabase = create_client(url, key)

credentials = {"email": "alvinkihato@gmail.com", "password" :"AlvinKimata23"}

#User sign up.
# user = supabase.auth.sign_up(credentials=credentials)
session = None

#User sign in.
try:
    session = supabase.auth.sign_in_with_password(credentials = credentials)

except AuthApiError:
    print("Login failed.")

print(session)

#Sign out.
# supabase.auth.sign_out()
