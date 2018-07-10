# recruiter
#Steps to Run Project
1. Create a virtual environment and install requirements.txt
2. run migrations
3. Run project
4. go to URL '/candidate' to list the candidate and filters
5. '/candidate' will also allow to export candidate data as CSV file.
6. '/admin'- gives you the access for the Django admin part (create superuser by command- python manage.py createsuperuser)

# Code Structure
1. recruiter/views.py- Gives the logic for POST and GET method used to filter and Export the data.
2. recruiter/filters.py -  customer filter to filter out the Candidate data.
