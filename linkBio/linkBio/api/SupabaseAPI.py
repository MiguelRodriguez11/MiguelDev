import os
import dotenv
from supabase import create_client, Client


class SupabaseAPI:

    dotenv.load_dotenv()

    URL_SUPABASE = os.environ.get("URL_SUPABASE")
    SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

    supabase: Client = create_client(URL_SUPABASE, SUPABASE_KEY)

    def feature(self) -> list:

        
        response = self.supabase.table("featured").select("*").execute()

        feature_data = []

        if len(response.data) > 0:
            for feature_item in response.data:
                feature_data.append(feature_item)

        return feature_data