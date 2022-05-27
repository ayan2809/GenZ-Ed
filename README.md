# GenZ Ed

An interative web application for helping the students with their queries while learning.

In this application, the educator can upload a learning material in the form of text or a document(pdf) as data source. The students would be able to access this document and ask their queries in a chatbox, powered by GPT-3. Further, the students can request a summarised form of the data, which would again be fetched using a GPT-3 API.

### Installing in Windows

Clone the repository
```bash
git clone https://github.com/ayan2809/GenZ-Ed.git
```
Make virtual environment for the project and activate it
```bash
python -m venv venv
venv\Scripts\Activate.ps1
```
Install the required packages in the virtual environment
```bash
pip install -r requirements.txt
```
### Running the Application
Apply the django migrations
```bash
python manage.py migrate
```
Collect the static files with modified timestamp
```bash
python manage.py collectstatic
```
Run the web server on the local machine
```bash
python manage.py runserver
```
