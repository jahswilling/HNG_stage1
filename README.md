# HNG_stage1

A simple application written using [FastAPI](https://fastapi.tiangolo.com/). 

The application has on one endpoint:

[http://localhost:8000/](http://localhost:8000/) displays the index page


## Want to use this project?

1. Fork/Clone

2. Create and activate a virtual environment:

    ```sh
    $ python3 -m venv venv && source venv/bin/activate
    ```

3. Install the requirements:

    ```sh
    (venv)$ pip install -r requirements.txt
    ```

4.  Run the server:

    ```sh
    (venv)$ uvicorn main:app --reload or python3 -m uvicorn main:app --reload
    ```
    
 6. Navigate to [http://localhost:8000/](http://localhost:8000/) in your favorite web browser.