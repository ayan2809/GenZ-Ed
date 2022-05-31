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

## Screenshots
![1](https://user-images.githubusercontent.com/42286904/171078553-00fb50d6-99bb-4214-a082-7bae77afba1c.jpg)
![2](https://user-images.githubusercontent.com/42286904/171078580-e02726d3-f50d-4c91-80e1-7e37b67cd737.jpg)
![3](https://user-images.githubusercontent.com/42286904/171078584-24f1d56c-4061-42c9-97b6-fcee40219869.jpg)
![4](https://user-images.githubusercontent.com/42286904/171078585-fd7c120d-1892-4672-9381-2b720985b63f.jpg)
![5](https://user-images.githubusercontent.com/42286904/171078587-c9005dda-b4e4-4a01-848c-b98d4c0d4d51.jpg)
![6](https://user-images.githubusercontent.com/42286904/171078588-b5cf6de0-2b05-4bf0-8ff8-778943b0db02.jpg)
![7](https://user-images.githubusercontent.com/42286904/171078590-04a7e1e0-feac-4b48-9628-867b76150022.jpg)
![8](https://user-images.githubusercontent.com/42286904/171078593-8a31ab51-0bff-4d50-a625-a24d8c6b9b7b.jpg)
![9](https://user-images.githubusercontent.com/42286904/171078595-e395bcd7-4885-45cd-9982-2609a618797c.jpg)
![10](https://user-images.githubusercontent.com/42286904/171078598-f9b90c83-4124-4864-a208-5f2ba273173c.jpg)
![11](https://user-images.githubusercontent.com/42286904/171078600-65975c96-cf22-4d4d-92e3-6da1b3a79e41.jpg)
![12](https://user-images.githubusercontent.com/42286904/171078602-80bfa41f-b8c1-4238-9d6a-c73dc8e5d0c4.jpg)
![13](https://user-images.githubusercontent.com/42286904/171078605-3dc49005-772e-48d4-b5e7-ecc038418fc0.jpg)
![14](https://user-images.githubusercontent.com/42286904/171078607-aa7b9534-28f9-4365-9be7-6c549cad985e.jpg)
![15](https://user-images.githubusercontent.com/42286904/171078608-fd4568bf-ab82-4183-9962-28b29e725b8c.jpg)
![16](https://user-images.githubusercontent.com/42286904/171078610-e596b7b9-43e4-43c8-9710-a21a764bfac5.jpg)
![17](https://user-images.githubusercontent.com/42286904/171078612-329a7a9d-d2fb-4ee4-8ee0-8a1821389627.jpg)
![18](https://user-images.githubusercontent.com/42286904/171078614-04d031e8-062c-4f57-8e3f-8ef308aba10e.jpg)
![19](https://user-images.githubusercontent.com/42286904/171078616-948d8892-52c3-4469-912c-cc74a48c07e0.jpg)
![20](https://user-images.githubusercontent.com/42286904/171078618-0e2487e4-a3bc-4538-9c7f-5c7b89d5e16c.jpg)
![21](https://user-images.githubusercontent.com/42286904/171078623-87de21ce-877b-447b-8f9a-a44d90c7f990.jpg)
![22](https://user-images.githubusercontent.com/42286904/171078890-5149630d-534c-44e0-ba5c-e9cf5ba21f9a.jpg)

## Future Scope
- Enable Insights for student side for better viewing of the queries and simplified study materials

- Integrate a student evaluation portal for teachers based on the live classes

- Improve the accuracy of the Query Answers by tuning the parameters

## Contributors:

Team Name: Odd Bit Squad

* [Ayan Sadhukhan](https://github.com/ayan2809)
* [Ronit Sarkar](https://github.com/Codee0101)
* [Aakriti Aggarwal](https://github.com/aakriti1318)


### Made at: Hackatra
