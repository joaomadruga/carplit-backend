# carplit

### (Optional) Create a virtualenv

1. Create the venv

    ```python
    virtualenv venv
    ```

2. Start

    Windows

    ```shell
    .\venv\Scripts\activate
    ```
    
    Linux

    ```bash
    source venv/scripts/activate
    ```

## Installation

1. Install FastAPI and Uvicorn
    
    ```python
    pip install fastapi
    ```
    
    ```python
    pip install "uvicorn[standard]"
    ```

2. Install manage-fastapi

    ```python
    pip install manage-fastapi 
    ```

## Getting Started 

1. Run `fastapi run` in your terminal.

    * To create a app folder user the following command.
    ```bash
    fastapi starapp {name}
    ```

4. Check for [localhost](http://127.0.0.1:8000) on your browser.

## Docs

FastAPI automatically creates the documentation and you can check it at  [docs](http://127.0.0.1:8000/docs) or [redoc](http://127.0.0.1:8000/redoc).

## Documentation

- [FastAPI](https://fastapi.tiangolo.com/)
- [ManageFastAPI](https://github.com/ycd/manage-fastapi)

## License

This project is licensed under the terms of the MIT license.
