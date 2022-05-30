![Logo](https://user-images.githubusercontent.com/42286904/171036981-cb222a42-b84e-4854-a958-ffa6c3c081b9.svg)

An interactive web application ideally suited for narrowing the gap between student and educator. We also touch upon one of the major problems in the path of learning that sometimes students may not get the proper guidance due to any reasons that might include network issues in rural areas. 

We are introducing features to our web application both for educators and students end. 
- The educator can upload a learning material in the form of text or a document(pdf) as a data source. 
- The students would be able to access this document and ask their queries in a chatbox, powered by GPT-3.
- Further, the students have the access to the tool where a student basically can request a simplifier form of translation to the complex data, which would again be fetched using a GPT-3 API. 
- Through this application, educators will get to know the top 5 subtopics that are common where students are facing issues.

Our application is loaded with features which ease the experience for both educator and students which includes:
Interactive, Responsive, Open AI GPT-3, ML Based, Robust, Metrics, Analysing Text and Scalable

This application provides real-time updates based on the usage of the applications from the student's end, which will ease educators in understanding students' behaviour of learning. 



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
