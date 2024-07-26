import linkBio.constants as const
from linkBio.model.Featured import Featured
from .TwitchAPI import TwitchAPI
from .SupabaseAPI import SupabaseAPI

TwitchAPI = TwitchAPI()
SUPABASE_API = SupabaseAPI()

async def repo() -> str:
    return const.REPO_URL

async def live() -> bool:
    return TwitchAPI.live(12136310349)

async def featured() -> list[Featured]:
    return SUPABASE_API.featured()
