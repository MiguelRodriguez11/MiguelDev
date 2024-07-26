import reflex as rx
import linkBio.utils as utils
from linkBio.api.api import live, featured
from linkBio.model.Featured import Featured


class PageState(rx.State):

    is_live: bool
    featured_info: list[Featured]

    async def check_live(self):
        self.is_live = await live()

    async def featured_links(self):
        self.featured_info = await featured()