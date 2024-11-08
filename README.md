Project Management Tool API
TechForing Limited is developing a project management tool to help teams collaborate on projects. The API serves as the backend for managing users, projects, tasks, and comments. The tool will be integrated with both web and mobile applications.

Database Schema
Users
id: Primary Key
username: Unique String
email: Unique String
password: String
first_name: String
last_name: String
date_joined: DateTime
Projects
id: Primary Key
name: String
description: Text
owner: Foreign Key (to Users)
created_at: DateTime
Project Members
id: Primary Key
project: Foreign Key (to Projects)
user: Foreign Key (to Users)
role: String (Admin, Member)
Tasks
id: Primary Key
title: String
description: Text
status: String (To Do, In Progress, Done)
priority: String (Low, Medium, High)
assigned_to: Foreign Key (to Users, nullable)
project: Foreign Key (to Projects)
created_at: DateTime
due_date: DateTime
Comments
id: Primary Key
content: Text
user: Foreign Key (to Users)
task: Foreign Key (to Tasks)
created_at: DateTime
API Endpoints
Users
Register User: POST /api/users/register/
Create a new user.

Login User: POST /api/users/login/
Authenticate a user and return a token.

Get User Details: GET /api/users/{id}/
Retrieve details of a specific user.

Update User: PUT/PATCH /api/users/{id}/
Update user details.

Delete User: DELETE /api/users/{id}/
Delete a user account.

Projects
List Projects: GET /api/projects/
Retrieve a list of all projects.

Create Project: POST /api/projects/
Create a new project.

Retrieve Project: GET /api/projects/{id}/
Retrieve details of a specific project.

Update Project: PUT/PATCH /api/projects/{id}/
Update project details.

Delete Project: DELETE /api/projects/{id}/
Delete a project.

Tasks
List Tasks: GET /api/projects/{project_id}/tasks/
Retrieve a list of all tasks in a project.

Create Task: POST /api/projects/{project_id}/tasks/
Create a new task in a project.

Retrieve Task: GET /api/tasks/{id}/
Retrieve details of a specific task.

Update Task: PUT/PATCH /api/tasks/{id}/
Update task details.

Delete Task: DELETE /api/tasks/{id}/
Delete a task.

Comments
List Comments: GET /api/tasks/{task_id}/comments/
Retrieve a list of all comments on a task.

Create Comment: POST /api/tasks/{task_id}/comments/
Create a new comment on a task.

Retrieve Comment: GET /api/comments/{id}/
Retrieve details of a specific comment.

Update Comment: PUT/PATCH /api/comments/{id}/
Update comment details.

Delete Comment: DELETE /api/comments/{id}/
Delete a comment.

Implementation Steps
Set Up Django Project
Initialize a new Django project and configure it for the API.

Design the Database Schema
Define the models for Users, Projects, Tasks, Comments, and Project Members. Use Django ORM to establish relationships between the models and migrate the database.

Implement the REST API
Use Django REST Framework to create serializers and viewsets for each model. Set up authentication and authorization, such as JWT token authentication.

Testing the API
Use tools like Postman or Curl to test the endpoints and ensure they work as expected.

Documentation
Document the API using Swagger or Postman. Provide clear instructions on how to set up and use the API.

Setup Instructions
Clone the Repository
Clone this repository to your local machine.

bash
Copy code
git clone <repository_url>
cd project_management
Create a Virtual Environment
Set up a virtual environment to manage dependencies.

bash
Copy code
python -m venv venv
source venv/bin/activate   # For macOS/Linux
venv\Scripts\activate      # For Windows
Install Dependencies
Install the required Python packages.

Copy code
pip install -r requirements.txt
Migrate the Database
Set up the database and apply migrations.

Copy code
python manage.py migrate
Create a Superuser (Optional)
Create a superuser to access the Django admin panel.

Copy code
python manage.py createsuperuser
Run the Development Server
Start the development server.

Copy code
python manage.py runserver
Access the API
The API will be available at http://127.0.0.1:8000/api/.

Submission
Push Code to Git
Commit and push your code to the Git repository.

Include a README
Ensure this README file is included with clear instructions on setting up and running the project.

Provide API Documentation
Provide a link to the API documentation generated with Swagger or Postman.

Submit the Code
Submit the project using the provided Google form.
