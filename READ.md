# capstone

## Capstone Project for Udacity's Full Stack Developer Nanodegree
Heroku Link: https://smallgalaxy.herokuapp.com

While running locally: http://localhost:5000

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python).

#### Virtual Enviornment

Recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

## Running the server

Before running the application locally, make the following changes in the `app.py` file in root directory:
- uncomment the line `db_drop_and_create_all()` on the initial run to setup the required tables in the database.

To run the server, execute:

```bash
export DATABASE_URL=<database-connection-url>
export FLASK_APP=app.py
flask run --reload
```

Setting the `FLASK_APP` variable to `app.py` directs flask to use the `app.py` file to find the application. 

Using the `--reload` flag will detect file changes and restart the server automatically.

## API Reference

## Getting Started
Base URL: This application can be run locally. The hosted version is at `https://smallgalaxy.herokuapp.com`.

Authentication: This application requires authentication to perform various actions. All the endpoints require
various permissions, except the root endpoint, that are passed via the `Bearer` token.

The application has three different types of roles:
- human
  - can only view (planets).
  - has `get:planets, post:planets, patch:planets, delete:planets` permissions.
- alien
  - can can only view (stars).
  - has `get:stars, post:stars, patch:stars, delete:stars` permissions.


## Error Handling
Errors are returned as JSON objects in the following format:
```
{
    "success": false,
    "error": 404,
    "message": "resource not found"
}
```

The API will return the following errors based on how the request fails:
 - 401: Unauthorized
 - 404: Not Found
 - 422: Unprocessable Entity
 - 500: Internal Server Error

## Endpoints



#### GET /planets
 - General
   - gets the list of all the planets
   - requires `get:planets` permission
 
 - Sample Request
   - `https://smallgalaxy.herokuapp.com/planets`

<details>
<summary>Sample Response</summary>

```
{
    "planets": [
        {
            "name": 30,
            "moons_number": 1
        }
    ]
}
```
</details>

#### POST /planets
 - General
   - creates a new planet.
   - requires `post:planets` permission.
 
 - Request Body
   - name: string, required.
   - moons_number: Integer, required.
 
 - Sample Request
   - `https://smallgalaxy.herokuapp.com/planets`
   - Request Body
     ```
        {
        "name": "blue",
        "moons_number": 30
        }
     ```

<details>
<summary>Sample Response</summary>

```
{
    "success": true
}
```
  
</details>

#### PATCH /actors/{id}
 - General
   - updates the info for a planet
   - requires `patch:planets` permission
 
 - Request Body (at least one of the following fields required)
   - name: string, optional.
   - moons_number: Integer, required.
 
 - Sample Request
   - `https://smallgalaxy.herokuapp.com/planets/1`
   - Request Body
     ```
       {
            "moons_number": 32
       }
     ```

<details>
<summary>Sample Response</summary>

```
{
    "success": true,
    "id": 1
}
```
  
</details>

#### DELETE /actors/{id}
 - General
   - deletes an actor
   - requires `delete:actors` permission
 
 - Sample Request
   - `https://smallgalaxy.herokuapp.com/planets/1`

<details>
<summary>Sample Response</summary>

```
{
    "success": true,
    "id": 1
}
```
  
</details>

#### GET /stars
 - General
   - gets the list of all the stars
   - requires `get:stars` permission
 
 - Sample Request
   - `https://smallgalaxy.herokuapp.com/stars`

<details>
<summary>Sample Response</summary>

```
{
    "stars": [
        {
            "id": 1,
            "name": "red",
            "age": "2"
        },
        {
            "id": 2,
            "name": "black",
            "age": "8"
        }
    ]
}
```

</details>

#### POST /stars
 - General
   - creates a new star.
   - requires `post:stars` permission.
 
 - Request Body
   - name: string, required.
   - age: integer, required.
 
 - Sample Request
   - `https://smallgalaxy.herokuapp.com/stars`
   - Request Body
     ```
        {
            "name": "Spider Man",
            "age": 2019,
        }
     ```

<details>
<summary>Sample Response</summary>

```
{
    "success": true
}
```
  
</details>

#### PATCH/stars/{id}
 - General
   - updates the info for a star
   - requires `post:stars` permission
 
 - Request Body (at least one of the following fields required)
   - name: string, optional
   - age: integer, optional
 
 - Sample Request
   - `https://smallgalaxy.herokuapp.com/stars/3`
   - Request Body
     ```
       {
            "age": 5
       }
     ```

<details>
<summary>Sample Response</summary>

```
{
    "success": true,
    "id": 3
}
```
  
</details>

#### DELETE /stars/id}
 - General
   - deletes a movie
   - requires `delete:stars` permission
 
 - Sample Request
   - `https://smallgalaxy.herokuapp.com/stars/3`

<details>
<summary>Sample Response</summary>

```
{
    "success": true,
    "id": 3
}
```
  
</details>

## Testing

### For MAC OS
For testing the backend, run the following commands (in the exact order):
```
dropdb galaxy
createdb galaxy
psql galaxy < galaxy.pgsql
python test.py
```
### For Windows OS
For testing the backend, run the following commands (in the exact order):
```
dropdb -U <DATABASE USER> galaxy
createdb -U <DATABASE USER> galaxy
psql -U <DATABASE USER> galaxy < galaxy.pgsql
py test.py
```

Alternate way: Create the db `galaxy` using PgAdmin and copy the contents of galaxy.pgsql and paste them
in Query tool in PgAdmin and create the db table with records. Then, run the command for MAC OS `python test.py` or `py test.py` for Windows OS.