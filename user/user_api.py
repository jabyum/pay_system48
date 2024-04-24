from fastapi import APIRouter
from datetime import datetime
# импортируйте все необходимое
from database.userservice import register_user_db
# пайдентик валидации из инит
from user import UserRegisterModel, EditUserModel

user_router = APIRouter(prefix='/user', tags=['Работа с пользователя'])


# Регистрация пользователя
@user_router.post('/register')
async def register_user(data: UserRegisterModel):
    # переводим пайдентик в обычный словарь
    new_user_data = data.model_dump()
    pass


# Получение информации о пользователе
@user_router.get('/info')
async def get_user(user_id: int):
    pass


# Изменить данные о пользователе
@user_router.put('/edit-data')
async def edit_user(data: EditUserModel):
    pass

# удалить пользователя
@user_router.delete('/delete-user')
async def delete_user(user_id: int):
    pass