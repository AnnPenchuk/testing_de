import re
from uuid import UUID, uuid4
from pydantic import BaseModel, EmailStr



class ValidationError(Exception):
   """password is not valid."""

pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{,}$'

class Users_valid(BaseModel):
    employee_id: UUID = uuid4()
    email: EmailStr
    password: str
    def validate(password):
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{,}$'
        if re.match(pattern, password) is None:
            raise ValidationError('Password has incorrecr format.')


def list_users(res):
    for i in res:
        Users_valid.model_validate(i)





