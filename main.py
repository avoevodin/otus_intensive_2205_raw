import json
from pprint import pprint
from dataclasses import dataclass
from pathlib import Path

FILENAME = "temp/response_stations.html"

# countries -> regions -> settlements -> stations
@dataclass
class BaseMapObject:
    title: str
    yandex_code: str


@dataclass
class Country(BaseMapObject):
    pass


@dataclass
class Settlement(BaseMapObject):
    pass


@dataclass
class Regions(BaseMapObject):
    pass


@dataclass
class Stations(BaseMapObject):
    pass


def main():
    with open(FILENAME) as f:
        print(f.encoding)
        data_dict: dict = json.loads(f.read())
        countries_list = list(data_dict.items())[0][1]
    # pprint(countries_list[140])
    # pprint(list(filter(lambda x: x['title'] == "Россия", countries_list))[0])
    print(
        list(
            map(
                lambda x: str(x["regions"][3]),
                filter(lambda x: x["title"] == "Россия", countries_list),
            )
        )
    )
    with open(f"temp/{Path(FILENAME).stem}_output.json", "w", encoding="UTF-8") as f:
        json.dump(
            list(
                map(
                    lambda x: x["regions"][3],
                    filter(lambda x: x["title"] == "Россия", countries_list),
                )
            ),
            f,
            ensure_ascii=False,
            indent=4,
        )


if __name__ == "__main__":
    main()
