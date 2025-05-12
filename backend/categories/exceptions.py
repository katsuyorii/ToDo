from fastapi import HTTPException, status


CATEGORY_NOT_FOUND = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Category not found')