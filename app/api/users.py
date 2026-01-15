from fastapi import APIRouter, HTTPException, status
from typing import List

from app.schemas.user import UserCreate, UserResponse

router = APIRouter(prefix="/users", tags=["Users"])

# In-memory storage
users_db: List[UserResponse] = []
user_id_counter = 1


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate):
    global user_id_counter

    # Check duplicate email
    for existing_user in users_db:
        if existing_user.email == user.email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )

    new_user = UserResponse(
        id=user_id_counter,
        name=user.name,
        email=user.email,
        age=user.age
    )

    users_db.append(new_user)
    user_id_counter += 1

    return new_user



@router.get("/", response_model=List[UserResponse])
def get_users():
    return users_db


@router.get("/{user_id}", response_model=UserResponse)
def get_user_by_id(user_id: int):
    for user in users_db:
        if user.id == user_id:
            return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )
