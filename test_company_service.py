import requests


def test_get_all_companies(url: str):
    res = requests.get(url).json()
    assert (res == [{
        'companies_id': 1,
        'name': 'Apple',
        'description': 'Мировой лидер в производстве высококачественных технологических устройств, включая iPhone, iPad, MacBook и другие продукты.',
        'phone_model': 'iPhone 13',
        'year': 1976
    },
        {
            'companies_id': 2,
            'name': 'Xiaomi',
            'description': 'Компания, предлагающая широкий ассортимент технологических устройств, включая смартфоны, планшеты, ноутбуки и умные устройства для дома.',
            'phone_model': 'Xiaomi Mi 11',
            'year': 2010
        },
        {
            'companies_id': 3,
            'name': 'Huawei',
            'description': 'Мировой лидер в производстве телекоммуникационного оборудования и потребительской электроники, включая смартфоны, планшеты и носимые устройства.',
            'phone_model': 'Huawei P50 Pro',
            'year': 1987
        },
        {
            'companies_id': 4,
            'name': 'Samsung',
            'description': 'Одна из крупнейших компаний в мире, производящая широкий спектр электроники, включая смартфоны, телевизоры, холодильники и другие продукты.',
            'phone_model': 'Samsung Galaxy S21',
            'year': 1938
        },
        {
            'companies_id': 5,
            'name': 'OnePlus',
            'description': 'Компания, специализирующаяся на производстве высококачественных смартфонов с передовыми технологиями и дизайном.',
            'phone_model': 'OnePlus 9 Pro',
            'year': 2013
        }

    ])


def test_get_company_by_id(url: str):
    res = requests.get(url).json()
    assert (res == {
        'companies_id': 5,
        'name': 'OnePlus',
        'description': 'Компания, специализирующаяся на производстве высококачественных смартфонов с передовыми технологиями и дизайном.',
        'phone_model': 'OnePlus 9 Pro',
        'year': 2013
    })


if __name__ == '__main__':
    URL = 'http://127.0.0.1:80/api/v1/companies/'
    test_get_company_by_id(URL + '1')
    test_get_all_companies(URL)
