import reflex as rx
from linkBio.api.api import live, featured


class PageState(rx.State):

    is_live: bool
    featured_info: list

    async def check_live(self):
        self.is_live = await live()

    async def featured_links(self):
        self.featured_info = await featured()