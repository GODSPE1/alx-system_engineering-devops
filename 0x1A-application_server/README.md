An application server is a software framework that provides an environment for running and managing applications. It typically sits between the backend database servers and the frontend web servers, serving as an intermediary layer responsible for handling business logic, application services, and data access.

Background Context


Your web infrastructure is already serving web pages via Nginx that you installed in your first web stack project. While a web server can also serve dynamic content, this task is usually given to an application server. In this project you will add this piece to your infrastructure, plug it to your Nginx and make is serve your Airbnb clone project.

Resources
Read or watch:

Application server vs web server
How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04 (As mentioned in the video, do not install Gunicorn using virtualenv, just install everything globally)
Running Gunicorn
Be careful with the way Flask manages slash in route - strict_slashes
Upstart documentation
