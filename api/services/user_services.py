from account.models import CustomUser
from api.selectors.user_selectors import customUser_get
def customUser_delete(pk):
    user = customUser_get(pk)
    if user: user.delete()
    return user
    