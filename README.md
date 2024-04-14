1. Clone this repository using the following command:
    ```
    git clone https://github.com/Prashant-2024/Quiz-WebApp-Django.git
    ```
2. Change into the project directory:
    ```
    cd QUIZ WEBAPP
    ```
3. Create a virtual environment:
    ```
    py -m myVenv myVenv
    ```
4. Activate the virtual environment:
    - On macOS and Linux:
        ```
        source myVenv/bin/activate
        ```
    - On Windows:
        ```
        myVenv\Scripts\activate
        ```
5. Install the project dependencies:
    ```
    pip install -r requirements.txt
    ```
6. Apply the database migrations:
    ```
    python manage.py migrate
    ```
7. Run the development server:
    ```
    python manage.py runserver
    ```