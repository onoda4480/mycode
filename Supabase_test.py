from supabase import Client, create_client
from datetime import datetime

supabase: Client = create_client("https://vusmwyplxywdcyksdbfu.supabase.co", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZ1c213eXBseHl3ZGN5a3NkYmZ1Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY5Nzg5MjE3MSwiZXhwIjoyMDEzNDY4MTcxfQ.R-2CQ-vYkyzJ2WHmSbo2bU8ZBiPYt46msDHWeQuAfFQ")
#data = supabase.table("test_jphack").insert({"name": "Japan"}).execute()
#country_id = data.data[0]["id"]
today = datetime.now()
current_datetime = datetime.now().isoformat()
supabase.table("test_jphack").insert(
   [
       {"name": "tanaka", "rental_day": current_datetime},
       {"name": "asda", "rental_day": current_datetime},
   ]
).execute()

#supabase.table("cities").delete().eq("name", "Kyoto").execute()