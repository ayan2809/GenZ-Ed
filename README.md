![Logo](https://user-images.githubusercontent.com/42286904/171036981-cb222a42-b84e-4854-a958-ffa6c3c081b9.svg)
## Introduction:
An interactive web application ideally suited for narrowing the gap between student and educator. We also touch upon one of the major problems in the path of learning that sometimes students may not get the proper guidance due to any reasons that might include network issues in rural areas. 

We are introducing features to our web application both for educators and students end. 
- The educator can upload a learning material in the form of text or a document(pdf) as a data source. 
- The students would be able to access this document and ask their queries in a chatbox, powered by GPT-3.
- Further, the students have the access to the tool where a student basically can request a simplifier form of translation to the complex data, which would again be fetched using a GPT-3 API. 
- Through this application, educators will get to know the top 5 subtopics that are common where students are facing issues.

Our application is loaded with features which ease the experience for both educator and students which includes:
Interactive, Responsive, Open AI GPT-3, ML Based, Robust, Metrics, Analysing Text and Scalable

This application provides real-time updates based on the usage of the applications from the student's end, which will ease educators in understanding students' behaviour of learning. 

## Demo Video Link:
  <a href="">Demo Video Link</a>

## API Endpoints:
<b>/                 </b>- Home page for our application <br>
<b>/authentication            </b>- Signs and authenticates a teacher or student <br>
<b>/signup  </b> - Sign up a new user <br>
<b>/profile  </b> - Get profile of a user <br>
<b>/logout </b> - Logout a user <br>
<b>/failure </b> - Failure page <br>
<b>/UpdateClassNumber/     </b> - Updates the class number of the teacher<br>
<b>/GetClassNumbers/     </b> - Fetches the class numbers of the teacher<br>
<b>/UploadExtractedText/     </b> - Uploads the extracted text of the pdf file for teacher<br>
<b>/UpdateClassNumberStudent/    </b> - Updates the class number of the student<br>
<b>/GetClassNumbersStudent/    </b> - Fetches the class numbers of the student<br>
<b>/FetchUploadedMaterial/    </b> - Fetches the uploaded material of the teacher<br>
<b>/GetSummary/    </b> - Fetches the summary of the uploaded material of the teacher<br>
<b>/chatBotReply/    </b> - Fetches the chatbot reply of the uploaded query of the student<br>
<b>/GetQuestions/    </b> - Fetches the questions asked by the student for easy insights by the teacher<br>

## Screenshots

## Future Scope
- Enable Insights for student side for better viewing of the queries and simplified study materials

- Integrate a student evaluation portal for teachers based on the live classes

- Improve the accuracy of the Query Answers by tuning the parameters


## Technology Stack:
 - Django
 - HTML, CSS, JS
 - Bootstrap4
 - Jquery
 - Python
 - Open AI GPT-3
 - Mongo DB
 - AJAX
 - Heroku


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

## Contributors:

Team Name: Odd Bit Squad

* [Ayan Sadhukhan](https://github.com/ayan2809)
* [Ronit Sarkar](https://github.com/Codee0101)
* [Aakriti Aggarwal](https://github.com/aakriti1318)


### Made at: Hackatra