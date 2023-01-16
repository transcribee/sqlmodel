"""These test cases should become obsolete if `sa_relationship`-parameters are dropped from `Relationship`."""

import pytest
from sqlalchemy.orm.relationships import RelationshipProperty
from sqlmodel.main import Relationship, RelationshipInfo


def test_sa_relationship_params_raise_warnings() -> None:
    with pytest.warns(DeprecationWarning):
        Relationship(sa_relationship=RelationshipProperty("a"))
    with pytest.warns(DeprecationWarning):
        Relationship(sa_relationship_args=["a", "b"])
    with pytest.warns(DeprecationWarning):
        Relationship(sa_relationship_kwargs={"doc": "foo"})


def test_sa_relationship_overrides_other_params() -> None:
    rel_prop = RelationshipProperty("a", lazy="noload")
    rel_info = RelationshipInfo(
        lazy="selectin",  # should be ignored
        sa_relationship=rel_prop,
    )
    output = rel_info.construct_relationship("foo", "bar")
    assert output is rel_prop
    assert output.lazy == "noload"
