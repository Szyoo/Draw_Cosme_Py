# service.presents.service.py

from app.models import Present
from app.exceptions import ElementNotFoundException
from app.services.page_services import PresentListNormalPage, PresentListBrandFanClubPage
from app.services.presents import scanner, converter
from app.utils import selenium_utils
from app.database import repository
from app.database.session import get_db


class PresentService:

    def get_total_presents_by_user(self, user_id: int) -> int:
        with get_db() as db:
            return repository.count_presents_by_user(db, user_id)

    def get_total_drawn_by_user(self, user_id: int) -> int:
        with get_db() as db:
            return repository.count_drawn_presents_by_user(db, user_id)
