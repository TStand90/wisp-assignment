# wisp-assignment

This small project uses [FastAPI](https://fastapi.tiangolo.com/). To run it, use Python 3.9 (3.10 should work too). Python 3.9+ is required because of the @cache decorator.

After creating a virtualenv or setting up Python3.9 the way you prefer, do `pip install -r requirements.txt`, which will install FastAPI, Uvicorn, and Pytest.

To run the server, do `uvicorn main:app --reload`, which will run the project on port 8000 by default.

The endpoints are:
* `/special-math/{number}`
* `/special-math/{number}no-recursion`

The first runs the function with the `@cache` decorator and does recursion. The second, as the name imples, uses a non-recursive solution, and can therefore accept larger numbers.

To run the tests, just do `pytest`.
