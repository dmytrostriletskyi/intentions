from __future__ import annotations

from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Optional,
    TypeVar,
)

if TYPE_CHECKING:
    from types import TracebackType

T = TypeVar('T')


class AbstractIntention:
    """
    Abstract intention implementation.
    """

    def __init__(self, description: str) -> None:
        """
        Construct the object.

        Arguments:
            description (str): a description of the intention.
        """
        self.description = description

    def __enter__(self) -> AbstractIntention:
        return self

    def __exit__(
        self,
        exc_type: Optional[type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        return


class when(AbstractIntention):
    """
    "When" intention implementation.
    """


class case(AbstractIntention):
    """
    "Case" intention implementation.
    """


class expect(AbstractIntention):
    """
    "Expect" intention implementation.
    """


def describe(object: str, domain: str) -> Callable[[Callable[..., T]], Callable[..., T]]:  # noqa: ARG001
    def decorator(func: [..., T]) -> Callable[..., T]:
        def wrapper(*args: tuple[Any, ...], **kwargs: dict[str, Any]) -> T:
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator
