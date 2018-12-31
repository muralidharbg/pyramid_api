# pyramid_api

To run:
1. Create virtual environment
  `python3 -m venv ~/env/`
2. Activate virtual environment
  `. ~/env/bin/activate`
3. `pip install --upgrade pip`
4. `pip install --upgrade pip setuptools`
5. Change directory to the root folder of the project
6. Install dependencies
  `python setup.py develop`
7. Change the mysql credentials in development.ini file
8. `alembic -c development.ini upgrade`
9. `pserve development.ini`

API endpoints:

GET /brands

POST /brands

Input:
{
	"name": "Ferrari",
}

GET /brands/:id

PUT /brands/:id

Input:
{
	"name": "Brand name"
}

DELETE /brands/:id
