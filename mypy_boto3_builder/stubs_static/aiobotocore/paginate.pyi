from typing import Any, Iterator, Type

from botocore.paginate import PageIterator, Paginator

class AioPageIterator(PageIterator):
    def __aiter__(self) -> Any: ...
    resume_token: Any
    async def __anext__(self) -> Iterator[Any]: ...
    def result_key_iters(self) -> Any: ...
    async def build_full_result(self) -> Any: ...
    async def search(self, expression: str) -> Iterator[Any]: ...  # type: ignore [override]

class AioPaginator(Paginator):
    PAGE_ITERATOR_CLS: Type[AioPageIterator]

class ResultKeyIterator:
    result_key: str
    def __init__(self, pages_iterator: PageIterator, result_key: str) -> None: ...
    def __aiter__(self) -> Any: ...
    async def __anext__(self) -> Iterator[Any]: ...
