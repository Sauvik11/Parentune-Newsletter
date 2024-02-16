Description
Home :
The Home page has the form to add a new subscriber to the list 

To update the news letter content use the form on the bottom (ideally visible only to Admin).

Scheduler: 

A scheduler has been set up that checks the users that have subscriptions enabled and periodically sends them emails at regular intervals (currently set to 10s for testing )
The above has been done using celery and celery beats on redis server so that main server is free , hence the project is scalable.

Steps to run this project:

1. Clone the repository:

2. Navigate to the project directory:

3. Create a virtual environment (optional but recommended):

4. Activate the virtual environment

5. Install dependencies

6. Configure according to your system
   	1. Configure your database settings in `settings.py`.
	2. Set up your email configuration in `settings.py`.
	3. Set up Celery and Redis configuration in `settings.py`.

7. Run the following commands to apply initial migrations:
	1.python manage.py makemigrations
	2.python manage.py migrate

8  Run Django server : python manage.py runserver

9 Open two more terminals for celery worker and beat

10 Run this command to start celery worker this will reeive the tasks 
	 
	celery -A parentune  worker --pool=solo -l info to 

11 Run this command to start celery beat this will periodically send the tasks.
	
	celery -A parentune  beat -l info

Note : to change the timing of the mail in settings.py find  CELERY_BEAT_SCHEDULE change schedule according to your requirement