from typing import (
    Optional,
    Type,
)
from types import TracebackType


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

    def __enter__(self) -> 'AbstractIntention':
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ):
        return


class when(AbstractIntention):
    """
    "When" intention implementation.
    """
    pass


class case(AbstractIntention):
    """
    "Case" intention implementation.
    """
    pass


class expect(AbstractIntention):
    """
    "Expect" intention implementation.
    """
    pass
