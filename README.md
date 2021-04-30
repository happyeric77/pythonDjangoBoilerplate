# Django web server boilerplate

There are there main functions in these boilerplate:
1. debug toolbar module - which allows developer to see more detail information of the web APP.
2. decouple module - which extract the env variable out from settings file. deveoper can manage all the confidential data in ".env" file. (remember to fill the information into env file and change the file name to .env)
3. rename flag: you can change the project name by renmae flag:
    ```
    python manage.py rename "NEW POROJECT NAME"
    ```