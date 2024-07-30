from dotenv import load_dotenv
load_dotenv()

import os
from supabase import create_client, Client



url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

supabase = create_client(url, key)

#Read data
data = supabase.table("todos").select("id,name").eq("name", "item 1").execute()

#Insert data.
data = supabase.table("todos").insert({"name": "ToDo 2"}).execute()

data = supabase.table("todos").select("*").execute()
print(data)


