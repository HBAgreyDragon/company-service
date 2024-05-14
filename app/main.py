from fastapi import FastAPI, APIRouter
import httpx
from fastapi import APIRouter, HTTPException

app = FastAPI(openapi_url="/api/v1/companies/openapi.json", docs_url="/api/v1/companies/docs")

companies_router = APIRouter()

companies = [
    {
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

]


@companies_router.get("/")
async def read_companies():
    return companies


@companies_router.get("/{companies_id}")
async def read_company(companies_id: int):
    for company in companies:
        if company['companies_id'] == companies_id:
            return company
    return None


app.include_router(companies_router, prefix='/api/v1/companies', tags=['companies'])

if __name__ == '__main__':
    import uvicorn
    import os

    try:
        PORT = int(os.environ['PORT'])
    except KeyError as keyerr:
        PORT = 80
    uvicorn.run(app, host='0.0.0.0', port=PORT)
