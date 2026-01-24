from app.services.service_book import BookService


class BookQueryResolver:
    def service(self, info):
        session = info.context["session"]
        return BookService(session)

    async def resolve_get_book(self, _, info, id):
        return await self.service(info).get_book_by_id(id)

    async def resolve_get_all_books(self, _, info):
        return await self.service(info).get_all_books()
