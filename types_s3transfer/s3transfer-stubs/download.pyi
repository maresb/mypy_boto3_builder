import logging
from typing import IO, Any, Callable, Dict, List, Optional, TypeVar

from s3transfer.compat import seekable as seekable
from s3transfer.exceptions import RetriesExceededError as RetriesExceededError
from s3transfer.futures import IN_MEMORY_DOWNLOAD_TAG as IN_MEMORY_DOWNLOAD_TAG
from s3transfer.futures import BoundedExecutor, TaskTag, TransferCoordinator, TransferFuture
from s3transfer.tasks import SubmissionTask as SubmissionTask
from s3transfer.tasks import Task as Task
from s3transfer.utils import S3_RETRYABLE_DOWNLOAD_ERRORS as S3_RETRYABLE_DOWNLOAD_ERRORS
from s3transfer.utils import CountCallbackInvoker as CountCallbackInvoker
from s3transfer.utils import DeferredOpenFile as DeferredOpenFile
from s3transfer.utils import FunctionContainer as FunctionContainer
from s3transfer.utils import OSUtils
from s3transfer.utils import StreamReaderProgress as StreamReaderProgress
from s3transfer.utils import calculate_num_parts as calculate_num_parts
from s3transfer.utils import calculate_range_parameter as calculate_range_parameter
from s3transfer.utils import get_callbacks as get_callbacks
from s3transfer.utils import invoke_progress_callbacks as invoke_progress_callbacks

_R = TypeVar("_R")

logger: logging.Logger

class DownloadOutputManager:
    def __init__(
        self,
        osutil: OSUtils,
        transfer_coordinator: TransferCoordinator,
        io_executor: BoundedExecutor,
    ) -> None: ...
    @classmethod
    def is_compatible(cls, download_target: IO[Any], osutil: OSUtils) -> bool: ...
    def get_download_task_tag(self) -> TaskTag: ...
    def get_fileobj_for_io_writes(self, transfer_future: TransferFuture) -> None: ...
    def queue_file_io_task(self, fileobj: IO[Any], data: str, offset: int) -> None: ...
    def get_io_write_task(self, fileobj: IO[Any], data: str, offset: int) -> Task: ...
    def get_final_io_task(self) -> Task: ...

class DownloadFilenameOutputManager(DownloadOutputManager):
    def __init__(
        self,
        osutil: OSUtils,
        transfer_coordinator: TransferCoordinator,
        io_executor: BoundedExecutor,
    ) -> None: ...
    @classmethod
    def is_compatible(cls, download_target: IO[Any], osutil: OSUtils) -> bool: ...
    def get_fileobj_for_io_writes(self, transfer_future: TransferFuture) -> IO[Any]: ...
    def get_final_io_task(self) -> Task: ...

class DownloadSeekableOutputManager(DownloadOutputManager):
    @classmethod
    def is_compatible(cls, download_target: IO[Any], osutil: OSUtils) -> bool: ...
    def get_fileobj_for_io_writes(self, transfer_future: TransferFuture) -> IO[Any]: ...
    def get_final_io_task(self) -> Task: ...

class DownloadNonSeekableOutputManager(DownloadOutputManager):
    def __init__(
        self,
        osutil: OSUtils,
        transfer_coordinator: TransferCoordinator,
        io_executor: BoundedExecutor,
        defer_queue: Optional[DeferQueue] = ...,
    ) -> None: ...
    @classmethod
    def is_compatible(cls, download_target: IO[Any], osutil: OSUtils) -> bool: ...
    def get_download_task_tag(self) -> TaskTag: ...
    def get_fileobj_for_io_writes(self, transfer_future: TransferFuture) -> IO[Any]: ...
    def get_final_io_task(self) -> Task: ...
    def queue_file_io_task(self, fileobj: IO[Any], data: str, offset: int) -> None: ...
    def get_io_write_task(self, fileobj: IO[Any], data: str, offset: int) -> Task: ...

class DownloadSpecialFilenameOutputManager(DownloadNonSeekableOutputManager):
    def __init__(
        self,
        osutil: OSUtils,
        transfer_coordinator: TransferCoordinator,
        io_executor: BoundedExecutor,
        defer_queue: Optional[DeferQueue] = ...,
    ) -> None: ...
    @classmethod
    def is_compatible(cls, download_target: IO[Any], osutil: OSUtils) -> bool: ...
    def get_fileobj_for_io_writes(self, transfer_future: TransferFuture) -> IO[Any]: ...
    def get_final_io_task(self) -> Task: ...

class DownloadSubmissionTask(SubmissionTask): ...
class GetObjectTask(Task): ...
class ImmediatelyWriteIOGetObjectTask(GetObjectTask): ...
class IOWriteTask(Task): ...
class IOStreamingWriteTask(Task): ...
class IORenameFileTask(Task): ...
class IOCloseTask(Task): ...

class CompleteDownloadNOOPTask(Task):
    def __init__(
        self,
        transfer_coordinator: TransferCoordinator,
        main_kwargs: Optional[Dict[str, Any]] = ...,
        pending_main_kwargs: Optional[Dict[str, Any]] = ...,
        done_callbacks: Optional[Callable[..., Any]] = ...,
        is_final: bool = ...,
    ) -> None: ...

class DownloadChunkIterator:
    def __init__(self, body: IO[Any], chunksize: int) -> None: ...
    def __iter__(self: _R) -> _R: ...
    def __next__(self) -> str: ...
    next: Callable[[], str]

class DeferQueue:
    def __init__(self) -> None: ...
    def request_writes(self, offset: int, data: str) -> List[Dict[str, Any]]: ...
