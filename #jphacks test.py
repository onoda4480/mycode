#jphacks test
from supabase import Client, create_client

SUPABASE_URL = "https://vusmwyplxywdcyksdbfu.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZ1c213eXBseHl3ZGN5a3NkYmZ1Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY5Nzg5MjE3MSwiZXhwIjoyMDEzNDY4MTcxfQ.R-2CQ-vYkyzJ2WHmSbo2bU8ZBiPYt46msDHWeQuAfFQ"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

data = supabase.table("test_jphack").select("name").execute()

print(data.data)
