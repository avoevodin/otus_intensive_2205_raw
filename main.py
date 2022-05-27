import json
from pprint import pprint
from dataclasses import dataclass
from pathlib import Path
from models import Country, Region, Settlement
from models.session import Session
from sqlalchemy.orm import Session as SessionType


FILENAME = "temp/response_stations.html"
FIELD_YANDEX_CODE = "yandex_code"

session: SessionType = Session()


def get_yandex_code(obj_data):
    """

    :param obj_data:
    :return:
    """
    obj_codes = obj_data["codes"]
    obj_yandex_code = ""
    if obj_codes and obj_codes[FIELD_YANDEX_CODE]:
        obj_yandex_code = obj_codes[FIELD_YANDEX_CODE]
    return obj_yandex_code


def get_title(obj_data):
    """

    :param obj_data:
    :return:
    """
    return obj_data["title"]


def get_country(yandex_code):
    return session.query(Country).filter_by(yandex_code=yandex_code).one_or_none()


def get_region(yandex_code):
    return session.query(Region).filter_by(yandex_code=yandex_code).one_or_none()


def get_settlement(yandex_code):
    return session.query(Settlement).filter_by(yandex_code=yandex_code).one_or_none()


def get_region(yandex_code):
    return session.query(Region).filter_by(yandex_code=yandex_code).one_or_none()


def create_country(country_data):
    yandex_code = get_yandex_code(country_data)
    country = None
    if yandex_code:
        country = get_country(yandex_code)
        if not country:
            country = Country(yandex_code=yandex_code, title=get_title(country_data))
            session.add(country)
            session.commit()
    return country


def create_region(region_data, country_id):
    yandex_code = get_yandex_code(region_data)
    region = None
    if yandex_code:
        region = get_region(yandex_code)
        if not region:
            region = Region(
                yandex_code=yandex_code,
                title=get_title(region_data),
                country_id=country_id,
            )
            session.add(region)
            session.commit()

    return region


def create_settlement(settlement_data, country_id, region_id):
    yandex_code = get_yandex_code(settlement_data)
    settlement = None
    if yandex_code:
        settlement = get_settlement(yandex_code)
        if not settlement:
            settlement = Settlement(
                yandex_code=yandex_code,
                title=get_title(settlement_data),
                country_id=country_id,
                region_id=region_id,
            )
            session.add(settlement)
            session.commit()

    return settlement


def fill_db(countries_list):
    """

    :param countries_list:
    :return:
    """
    for country in countries_list:
        country_in_db = create_country(country)
        if country_in_db:
            country_id = country_in_db.id
            for region in country["regions"]:
                region_in_db = create_region(region, country_id)
                for settlement in region["settlements"]:
                    region_id = region_in_db.id if region_in_db else None
                    settlement = create_settlement(settlement, country_id, region_id)


def main():
    with open(FILENAME) as f:
        print(f.encoding)
        data_dict: dict = json.loads(f.read())
        countries_list = list(data_dict.items())[0][1]
    # fill_db(countries_list)
    # pprint(session.query(Settlement).all())
    pprint(list(map(lambda x: x.get_code(), session.query(Settlement).all())))
    country_russia = session.query(Country).filter_by(title="Россия").first()
    print(country_russia)
    with open(f"temp/{Path(FILENAME).stem}_output.json", "w", encoding="UTF-8") as f:
        json.dump(
            list(
                map(
                    lambda x: x.get_code(),
                    session.query(Settlement).filter_by(country=country_russia).all(),
                )
            ),
            f,
            ensure_ascii=False,
            indent=4,
        )


if __name__ == "__main__":
    main()
