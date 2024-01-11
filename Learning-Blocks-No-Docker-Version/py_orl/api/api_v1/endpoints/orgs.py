from sqlite3 import dbapi2
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlmodel import select

from neworgsmodel import Org, OrgCreate, OrgOut, OrgUpdate
from api.deps import SessionDep

router = APIRouter()


@router.get('/', response_model=list[OrgOut])
def read_orgs(
        session: SessionDep,
        skip: int = 0,
        limit: int = 100
) -> Any:
    """
    Retrieve orgs.
    """
    statement = select(Org).offset(skip).limit(limit)
    return session.exec(statement).all()


@router.post('/', response_model=Org)
def create_org(
        *,
        session: SessionDep,
        org_in: OrgCreate
) -> Any:
    """
    Create new org.
    """
    org = Org.from_orm(org_in)
    session.add(org)
    session.commit()
    session.refresh(org)
    return org


@router.put('/{sourcedId}', response_model=Org)
def update_org(
        *,
        session: SessionDep,
        sourcedId: str,
        org_in: OrgUpdate
) -> Any:
    """
    Update an org.
    """
    org = org.get(db=session, sourcedId=sourcedId)
    if not org:
        raise HTTPException(status_code=404, detail='Org not found')
    org = org.update(db=session, db_obj=org, obj_in=org_in)
    return org


@router.get('/{sourcedId}', response_model=OrgOut)
def read_org(
        *,
        session: SessionDep,
        sourcedId: str
) -> Any:
    """
    Get org by ID.
    """
    org = session.get(Org, id)
    if not org:
        raise HTTPException(status_code=404, detail='Org not found')
    return org


@router.delete('/{sourcedId}', response_model=Org)
def delete_org(
        *,
        session: SessionDep,
        sourcedId: str
) -> Any:
    """
    Delete an org.
    """
    org = org.get_by_sourcedId(db=session, sourcedId=sourcedId)
    if not org:
        raise HTTPException(status_code=404, detail='Org not found')
    org = org.remove(db=session, id=sourcedId)
    return org
