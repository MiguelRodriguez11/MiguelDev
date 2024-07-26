import os
import dotenv
from supabase import create_client, Client
from linkBio.model.Featured import Featured


class SupabaseAPI:

    dotenv.load_dotenv()

    URL_SUPABASE = os.environ.get("URL_SUPABASE")
    SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

    supabase: Client

    def __init__(self) -> None:
        self.supabase: Client = None

    def create_client(self):
        if self.supabase is None:
            self.supabase = create_client(self.URL_SUPABASE, self.SUPABASE_KEY)

    def featured(self) -> list[Featured]:

        if self.supabase is None:
            self.create_client()

        response = self.supabase.table("featured").select("*").execute()

        featured_data = []

        if len(response.data) > 0:
            for featured_item in response.data:
                featured_data.append(
                    Featured(
                        title=featured_item["title"],
                        image=featured_item["image"],
                        url=featured_item["url"]
                    )
                )

        return featured_data
