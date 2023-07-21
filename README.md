# Jo Tests

## **Build**

For correct project working you need to have a Python version: 3.9+. Here is a list of commands to build ptoject, just paste them in your terminal:

```
mkdir Jo-Tests

cd Jo-Tests
```

```
git clone https://github.com/andreybyrsa/Jo-Tests.git
```

```
pip install -r requirements.txt

python manage.py runserver 3000
```
Server runs project on localhost:3000.

## **Team**

### Andrey Byrsa: 
- Dinamically changed JavaScript forms for creating Tests and Courses;

- JavaScript searching options for students and tests data;

- Output JSON data to HTML templates - dynamically changed pages;

- Files with reuseable JavaScript functions; 

- Backend Django auth app.

### Mamedaga Bayramov:
- Created a design for the application form;

- Wrote style files for the Tests and Courses application pages;

- Made the set up for the admin panel and its visualization;

- Created Django forms for user models (User, Student, Author, Teacher);

- Filled the database and moved out model migrations to the database;

### Kirill Vlasov:
- Created a design for the application form;

- Made up the ProfilePage.html page;

- Configured modal windows ProfileModal, CreateGroups and EditGroups;

- Retrieved the student's statistics from the database;

- Set up a post request to change user data in the database;

### Timur Miniazev:
- Created a design for the application form;

- Set up models for auth, Courses, Tests and migrated them to the database

- Made up class-based views for Courses, Tests, Profile apps and mixins for them

- Integrated ImageKit for saving profile pictures

- Created unique slug generator for urls
