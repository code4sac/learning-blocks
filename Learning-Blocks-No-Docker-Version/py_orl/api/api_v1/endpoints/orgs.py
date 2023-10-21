from typing import Any, List

import crud
import models
import schemas
from api import deps
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=List[schemas.Org])
def read_orgs(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100,
        current_org: models.Org = Depends(deps.get_current_active_org),
) -> Any:
    """
    Retrieve orgs.
    """
    if crud.org.is_superorg(current_org):
        orgs = crud.org.get_multi(db, skip=skip, limit=limit)
    else:
        orgs = crud.org.get_multi_by_owner(
            db=db, owner_sourceId=current_org.sourceId, skip=skip, limit=limit
        )
    return orgs


@router.post("/", response_model=schemas.Org)
def create_org(
        *,
        db: Session = Depends(deps.get_db),
        org_in: schemas.OrgCreate,
        current_org: models.Org = Depends(deps.get_current_active_org),
) -> Any:
    """
    Create new org.
    """
    org = crud.org.create_with_owner(db=db, obj_in=org_in, owner_sourceId=current_org.sourceId)
    return org


@router.put("/{sourceId}", response_model=schemas.Org)
def update_org(
        *,
        db: Session = Depends(deps.get_db),
        sourceId: int,
        org_in: schemas.OrgUpdate,
        current_org: models.Org = Depends(deps.get_current_active_org),
) -> Any:
    """
    Update an org.
    """
    org = crud.org.get(db=db, sourceId=sourceId)
    if not org:
        raise HTTPException(status_code=404, detail="Org not found")
    if not crud.org.is_superorg(current_org) and (org.owner_sourceId != current_org.sourceId):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    org = crud.org.update(db=db, db_obj=org, obj_in=org_in)
    return org


@router.get("/{sourceId}", response_model=schemas.Org)
def read_org(
        *,
        db: Session = Depends(deps.get_db),
        sourceId: int,
        current_org: models.Org = Depends(deps.get_current_active_org),
) -> Any:
    """
    Get org by ID.
    """
    org = crud.org.get(db=db, sourceId=sourceId)
    if not org:
        raise HTTPException(status_code=404, detail="Org not found")
    if not crud.org.is_superorg(current_org) and (org.owner_sourceId != current_org.sourceId):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return org


@router.delete("/{sourceId}", response_model=schemas.Org)
def delete_org(
        *,
        db: Session = Depends(deps.get_db),
        sourceId: int,
        current_org: models.Org = Depends(deps.get_current_active_org),
) -> Any:
    """
    Delete an org.
    """
    org = crud.org.get(db=db, sourceId=sourceId)
    if not org:
        raise HTTPException(status_code=404, detail="Org not found")
    if not crud.org.is_superorg(current_org) and (org.owner_sourceId != current_org.sourceId):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    org = crud.org.remove(db=db, sourceId=sourceId)
    return org
