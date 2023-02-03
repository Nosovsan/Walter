import requests


def get_data():
    rec = requests.get("https://www.walter-tools.com/ru-ru/tools/standard-tools")
    print(rec.status_code)


def get_url():
    pass


def main():
    get_data()


if __name__ == "__main__":
    main()
