import re


REGEX_PASSWORD = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"

def validation_password(password: str) -> str:
    if not re.fullmatch(REGEX_PASSWORD, password):
        raise ValueError('Пароль должен содержать минимум 1 букву, 1 цифру и 1 специальный символ!')
    
    return password