from dotenv import load_dotenv
load_dotenv()
import asyncio

import os
from supabase import create_client, Client
from gotrue.errors import AuthApiError

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

supabase = create_client(url, key)
func = supabase.functions()

async def test_func():
    resp = await func.invoke("hello-world", invoke_options = {"body": {}})
    return resp

loop = asyncio.new_event_loop()
resp = loop.run_until_complete(test_func())
print(resp)
loop.close()
