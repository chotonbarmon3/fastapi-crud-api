from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession

from connection import get_db
from model import user
from schema import user_create,user_response,user_update



router=APIRouter(prefix="/user",tags=["user"])

@router.get("",response_model=list[user_response],status_code = status.HTTP_200_OK)
async def get_user(db : AsyncSession=Depends(get_db)):
    stmt=select(user)
    result =await db.execute(stmt)
    all_user=result.scalars().all()
    return all_user





@router.post("")
async def add_user(user_add: user_create,db : AsyncSession=Depends(get_db)):
    uuser=user(**user_add.model_dump())
    db.add(uuser)
    await db.commit()
    await db.refresh(uuser)
    return uuser




@router.patch("/{user_id}")
async def update_user(user_id: int,uuser_update:user_update,db: AsyncSession=Depends(get_db)):
    stmt=select(user).where(user_id==user.id)
    rresult=await db.execute(stmt)
    result=rresult.scalar_one_or_none()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"User with ID {user_id} not found")
    updated=uuser_update.model_dump(exclude_unset=True)
    for key,value in updated.items():
        setattr(result,key,value)

    await db.commit()   
    await db.refresh(result)
    return result




@router.delete("/{user_id}")
async def user_delete(user_id: int,db:AsyncSession=Depends(get_db)):
    stmt=select(user).where(user.id==user_id)
    result=await db.execute(stmt)
    result=result.scalar()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="user not found")
    await db.delete(result)
    await db.commit()
    return {"message":"user deleted successfully"}
    





    







