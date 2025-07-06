from datetime import datetime
from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    for friend in friends:
        try:
            if "vaccine" not in friend:
                raise NotVaccinatedError("Visitor is not vaccinated")
            if friend["vaccine"]["expiration_date"] < datetime.now().date():
                raise OutdatedVaccineError("Vaccine is expired")
        except (NotVaccinatedError, OutdatedVaccineError):
            return "All friends should be vaccinated"

    masks_to_buy = sum(
        1 for friend in friends if not friend.get("wearing_a_mask", False))
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
