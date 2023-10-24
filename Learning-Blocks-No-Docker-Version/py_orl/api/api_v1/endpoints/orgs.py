from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Org])
def read_orgs(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100
) -> Any:
    """
    Retrieve orgs.
    """
    orgs = crud.org.get_multi_by_owner(
        db=db, skip=skip, limit=limit
    )
    return orgs


@router.post("/", response_model=schemas.Org)
def create_org(
        *,
        db: Session = Depends(deps.get_db),
        org_in: schemas.OrgCreate
) -> Any:
    """
    Create new org.
    """
    org = crud.org.create_with_owner(db=db, obj_in=org_in)
    return org


@router.put("/{source_id}", response_model=schemas.Org)
def update_org(
        *,
        db: Session = Depends(deps.get_db),
        source_id: int,
        org_in: schemas.OrgUpdate
) -> Any:
    """
    Update an org.
    """
    org = crud.org.get(db=db, source_id=source_id)
    if not org:
        raise HTTPException(status_code=404, detail="Org not found")
    org = crud.org.update(db=db, db_obj=org, obj_in=org_in)
    return org


@router.get("/{source_id}", response_model=schemas.Org)
def read_org(
        *,
        db: Session = Depends(deps.get_db),
        source_id: int
) -> Any:
    """
    Get org by ID.
    """
    org = crud.org.get(db=db, source_id=source_id)
    if not org:
        raise HTTPException(status_code=404, detail="Org not found")
    return org


@router.delete("/{source_id}", response_model=schemas.Org)
def delete_org(
        *,
        db: Session = Depends(deps.get_db),
        source_id: int
) -> Any:
    """
    Delete an org.
    """
    org = crud.org.get(db=db, source_id=source_id)
    if not org:
        raise HTTPException(status_code=404, detail="Org not found")
    org = crud.org.remove(db=db, source_id=source_id)
    return org
