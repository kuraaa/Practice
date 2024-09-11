from models.house_model import House as HouseMD
from models.house_owner_model import HouseOwner as HouseOwnerMD
from models.town_model import Town as TownMD
from models.district_model import District as DistrictMD
from models.street_model import Street as StreetMD
from sqlalchemy.orm import Session
from settings import settings


ENGINE = settings.ENGINE


def select_all_from_house():

    with Session(autoflush=False, bind=ENGINE) as db:

        houses = db.query(HouseMD).all()
        # houses = [houses[i]
        #           for i in range(len(houses) - 1, len(houses) - 100, -1)]

        if not houses:
            return "Error: House table is empty"

        result = list()

        for house in houses:

            try:
                town = db.query(TownMD).filter(
                    house.id_town == TownMD.id).first().name
            except AttributeError:
                town = "null"

            try:
                district = db.query(DistrictMD).filter(
                    house.id_district == DistrictMD.id).first().name
            except AttributeError:
                district = "null"

            try:
                street = db.query(StreetMD).filter(
                    house.id_street == StreetMD.id).first().name
            except AttributeError:
                street = "null"

            try:
                id_client = db.query(HouseOwnerMD).filter(
                    HouseOwnerMD.id_house == house.id).first().id_person
                is_actual = db.query(HouseOwnerMD).filter(
                    HouseOwnerMD.id_house == house.id).first().is_actual
            except AttributeError:
                id_client = "null"
                is_actual = "null"

            id_organization = house.id_organization
            house_number = house.house_number
            corpus_number = house.corpus_number
            flat_number = house.flat_number
            cadastr_number = house.cadastr_number

            data = {
                "id_organization": id_organization,
                "town": town,
                "district": district,
                "street": street,
                "house_number": house_number,
                "corpus_number": corpus_number,
                "flat_number": flat_number,
                "cadastr_number": cadastr_number,
                "id_client": id_client,
                "is_actual": is_actual
            }

            result.append(data)

        return result
