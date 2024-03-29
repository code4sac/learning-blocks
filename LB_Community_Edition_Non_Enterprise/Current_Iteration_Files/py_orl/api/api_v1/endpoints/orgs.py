from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import schemas
from api import deps

router = APIRouter()


@router.get('/', response_model=List[schemas.Org])
def read_orgs(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100
) -> Any:
    """
    Retrieve orgs.
    """
    orgs = crud.orgs.get_multi(
        db=db, skip=skip, limit=limit
    )
    return orgs


@router.post('/', response_model=schemas.Org)
def create_org(
        *,
        db: Session = Depends(deps.get_db),
        org_in: schemas.OrgCreate
) -> Any:
    """
    Create new orgs.
    """
    org = crud.org.create(db=db, obj_in=org_in)
    return org


@router.put('/{sourcedId}', response_model=schemas.Org)
def update_org(
        *,
        db: Session = Depends(deps.get_db),
        sourcedId: str,
        org_in: schemas.OrgUpdate
) -> Any:
    """
    Update an orgs.
    """
    org = crud.org.get(db=db, sourcedId=sourcedId)
    if not org:
        raise HTTPException(status_code=404, detail='Org not found')
    org = crud.org.update(db=db, db_obj=org, obj_in=org_in)
    return org


@router.get('/{sourcedId}', response_model=schemas.Org)
def read_org(
        *,
        db: Session = Depends(deps.get_db),
        sourcedId: str
) -> Any:
    """
    Get org by ID.
    """
    org = crud.org.get_by_sourcedId(db=db, sourcedId=sourcedId)
    if not org:
        raise HTTPException(status_code=404, detail='Org not found')
    return org


@router.delete('/{sourcedId}', response_model=schemas.Org)
def delete_org(
        *,
        db: Session = Depends(deps.get_db),
        sourcedId: str
) -> Any:
    """
    Delete an orgs.
    """
    org = crud.org.get_by_sourcedId(db=db, sourcedId=sourcedId)
    if not org:
        raise HTTPException(status_code=404, detail='Org not found')
    org = crud.org.remove(db=db, id=sourcedId)
    return org
