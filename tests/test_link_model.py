import pytest
from sqlmodel.main import Relationship, SQLModel


def test_link_model_and_secondary_together_error() -> None:
    rel_info = Relationship(secondary="foo", link_model="bar")
    with pytest.raises(RuntimeError):
        rel_info.construct_relationship("spam", type("Annotation", (SQLModel,), {}))
