from dataclasses import dataclass

from intentions.render.enums import Intention


@dataclass
class Describe:
    domain: str
    component: str
    layer: str


@dataclass
class TestCaseIntention:

    type: Intention  # noqa: A003
    code_line: int
    description: str


@dataclass
class TestCase:

    file_path: str
    class_name: str
    class_code_line: int
    case_name: str
    function_name: str
    function_code_line: int
    intentions: list[TestCaseIntention]
