from pydantic import BaseModel, EmailStr, constr


class UserSchema(BaseModel):
    email: EmailStr
    username: constr(max_length=63)

    class Config:
        orm_mode = True


class UserLoginSchema(BaseModel):
    username: constr(max_length=63)
    password: constr(max_length=63)


class UserRegistrationSchema(UserLoginSchema):
    email: EmailStr
    username: constr(max_length=63)
    password: constr(max_length=63)
    repeated_password: constr(max_length=63)


class AuthTokens(BaseModel):
    access_token: str
    refresh_token: str


class AccessToken(BaseModel):
    access_token: str
