[![Build Status](https://travis-ci.org/deevdz/final-project.svg?branch=master)](https://travis-ci.org/deevdz/final-project)

Full Stack Development Project
======

### Yoga Studio Site with Blog, Shop and Events - Full Stack Development Project for the Code Institute

This submission is part of the Fullstack Software Development diploma course offered by Code Institute.

## Overview

For my [final project](https://deevdz-final-project.herokuapp.com/) for the Code Institute I have taken inspiration from my [First Milestone Project](https://deevdz.github.io/milestone-project-1/index.html "First Milestone Project") and added features that I could only have dreamed of adding at the start of this process.

**What is this website for?** 

This Project is designed to allow users to view information and timetables for a yoga studio, to read articles from the blog and comment on articles, create an account and purchase various products from the site.

**What does it do?** 

The website provides an online presence for a yoga studio and allows users to register on it, log in and log out, to send an enquiry to the studio via the contact form and to purchase the products on offer on both the workshops page and the shop page. 

Users are also able to find out a bit about the studio, classes on offer, workshops available and read and comment on blog posts.

**How does it work?** 

The site's major functionality is to allow users to purchase gift vouchers, class packs and workshops. To be able to add items to their cart users must first register or login to the site. The final stage is to fill in some billing information (user can enter new information or use previously saved information) and enter debit/credit card details via stripe to complete the order. Users will receive an email notification of their order with instructions on how they will receive their product.

A blog section was also created which allows the user to page through multiple posts, comment on individual posts, search posts and filter posts by category or tag. Comments must be approved by the site administrator to appear on the site.

Additionally, the website allows users to submit an enquiry via the contact page. They will then get a reply to the email address they have indicated on the form, with a summary of their enquiry. Prior registration is not required to carry out this action.

## Site Demo
You can see the deployed version of the site [here](https://deevdz-final-project.herokuapp.com/).

## UX

## Features

#### Existing Features
* Responsive design ensures the website displays well on any screen size and device type.
* Homepage slider was created which allows the site administrator to add slides through the administration section of the site. This feature allows the administrator to add a title and subtitle, slider image, text that will be displayed on the button, the link for the button and the alignment of the text. The administrator also has the option to leave the slide as a draft or publish to the site.
* User authentication and authorisation - handling registration, logging in and logging out. Users who are not logged in will see Register and Log In options in the Navigation bar, but those who are logged in - will see a view orders and Log Out option instead. Administrators will be given extra options to create, update and delete posts.
* Contact form functionality allows users to fill out a form, which after submission will trigger an email to be sent to them using Gmail SMTP (and my own Gmail account). Logged in users will have the email field of the contact form automatically populated.
* Administrators have the option to Create, Update and Delete Blog posts from both the frontend and backend administration part of the site. Registered users are able to submit comments on individual blog posts. When a comment is submitted the site administrator is automatically emailed about the submission and prompted to review for approval. When a comment is approved it appears on the site. Blog posts can be searched and also filtered by category or tag. Pagination is in place and 4 posts are displayed per page.
* Product Pages - both a shop page and a workshop page was established on the site. Products were created using polymorphism. This allows the products to share common features but also allow products, in this case the workshops/events to have different product fields than other products. Workshops/Events have date and time fields, location of the event and the number of available places at this event.
* Cart and Checkout functionality - the Cart app stores the information of each product that is added to it and displays a cart total. Users can increase, decrease and remove items from the cart. In relation to workshops there is a check in place to see if there are enough places available on the workshop. The Checkout app also stores this information and displays a total but additionally sends the user to a Stripe form to enter payment details. On successfully completing their order users can view their order and any preious orders. 

#### Future Features
* Filtering the workshops by location or month when the workshop is occuring.
* Adding a shop that also sells physical products hence adding an option for shipping cost and shipping address


## Technologies Used

* [AWS Cloud 9](https://aws.amazon.com/cloud9/) - Was used to code this project.
* [GitHub](https://github.com/) - Remote repository for all project code with git version control.
* Adobe Photoshop & Illustrator - Design, crop and compresses images used on the site.

#### Front-End Technologies

* [HTML5](https://html.spec.whatwg.org/multipage/) - The fundamental code structure for all webpages.
* [CSS3](http://www.css3.info/) - CSS3 is the iteration of the CSS standard used in the styling and formatting of Web pages.
* [jQuery 3.2.1](https://blog.jquery.com/2017/03/20/jquery-3-2-1-now-available/) - Javascript framework used to implement custom code and initialize Bootsrtap functions.
* [Bootstrap](https://getbootstrap.com/) - Bootstrap is an open source toolkit for developing with HTML, CSS, and JS. 
* [Stripe](https://stripe.com/) - The Stripe API allows individuals and businesses to make and receive debit/credit card payments over the Internet.
* [Font Awesome](https://fontawesome.com/) - Used for Website Icons
* [Line Icons](https://lineicons.com/) - Used for Website Icons
* [Google Fonts](https://fontawesome.com/) - Used for website fonts Poppins and Prata
* [Vanilla Top](https://www.npmjs.com/package/vanillatop) - Script to allow users to return to top of page
* [Google Maps API](https://cloud.google.com/maps-platform/) - Used to display location on google maps

#### Back-End Technologies

**Heroku**

* [Heroku](http://ww.heroku.com) - Hosting the deployed version of this project.
* [Heroku Postgres - PostgreSQL](https://devcenter.heroku.com/categories/postgres-basics) is one of the world's most popular relational database management systems.

**Python**

* [Python 3.6.8](https://www.python.org/downloads/release/python-368/) - is an interpreted, high-level, general-purpose programming language that has gained popularity because of its clear syntax and readability and is the language used for all backend functions of this project.
* [Django 1.11](https://docs.djangoproject.com/en/3.0/releases/1.11/) - Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.

#### Amazon Web Services

* [Amazon S3](https://aws.amazon.com/free/storage/) - Amazon Simple Storage Service is a service offered by Amazon Web Services that provides object storage through a web service interface. Used to store staticfiles and media folders and files.

Further details on all Python packages used on this project can be found in the requirements.txt file. 

<details>
<summary>CLICK HERE to expand the full requirements.txt details.</summary>
<ul>
<li>boto3==1.10.28 - The AWS SDK for Python</li>
<li>botocore==1.13.28 - Foundation for AWS-CLI command line utilities</li>
<li>Django==1.11 - Used as my Python web framework.</li>
<li>django-tinymce4-lite==1.7.4 - A tinymce editor for text areas in forms</li>
<li>django-forms-bootstrap==3.1.0 -  A form filter for using Django forms with Bootstrap</li>
<li>django-crispy-forms==1.8.0 -  A form filter for using Django forms with Crispy Forms</li>
<li>django-allauth==0.40.0 - Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.</li>
<li>dj-database-url==0.5.0 - Utilizes the 12factor inspired DATABASE_URL environment variable to configure Django apps</li>
<li>django-polymorphic==2.1.2 - Use PolymorphicModel to create Products</li>
<li>django-storages==1.8 - Connects Django to S3 Buckets</li>
<li>django-taggit==0.24.0 - Is a reusable Django application for simple tagging.</li>
<li>pytz==2019.2 - Brings the Olson tz database into Python</li>
<li>chardet==3.0.4 - Universal Character Encoding Detector</li>
<li>colorama==0.3.7 - Cross-platform API to print colored terminal text from Python apps</li>
<li>docutils==0.14 - Modular system for processing documentation into useful formats</li>
<li>gunicorn==20.0.4 - A Python WSGI HTTP Server for UNIX</li>
<li>jmespath==0.9.3 - Allows you to declaratively specify how to extract elements from a JSON document</li>
<li>olefile==0.45.1 - Python package to parse, read and write Microsoft OLE2 files</li>
<li>Pillow==5.1.0 - Adds support for opening, manipulating, and saving many different image file formats</li>
<li>python-dateutil==2.6.1 - Extensions to the standard Python datetime module.</li>
<li>psycopg2-binary==2.8.3 - Python-PostgreSQL Database Adapter</li>
<li>requests==2.18.4 - Makes HTTP requests simpler and more human-friendly</li>
<li>six==1.11.0 - A Python 2 and 3 compatibility library</li>
<li>s3transfer==0.2.1 - Python library for managing Amazon S3 transfers</li>
<li>stripe==2.38.0 - Python library for Stripe’s API</li>
<li>urllib3==1.22 - Powerful, sanity-friendly HTTP client for Python</li>
</ul>
</summary>
</details>


## Testing

Testing for this project has been completed using both automated and manual methods. At the Code Insititute, we are encouraged to code using Test Driven Design methods. Automated testing has never been my strong point, but testing itself is important. For this project I have created automated tests, carried out extensive manual testing and passed the site code through validators.

### Automated Testing

Each app has their own tests created using Django TestCase class. All views, forms and pages were tested as much as possible using unit tests. In all, 24 tests were written. All tests pass successfully.

Travis-CI integration has been completed and also shows all tests completing successfully, with the project showing as "build: passing".

### Manual Testing

In conjunction with the automated testing the website was constantly tested during the development process. Browser developer tools were used to test HTML, CSS, JavaScript and responses from the server. Extensive manual testing has been completed to check that the site performs as it should in different environments and in different browsers.

<details>
<summary>Click to see details of manual testing below.</summary>
<ul>
<li></li>
</ul>
</summary>
</details>


### Validators

#### HTML

Both the Base HTML file and other HTML templates were passed through the [W3C Markup Validator](https://validator.w3.org/). Numerous errors were generated but this was expected as the validator is unable to process the Django templating that builds most aspects of the site. 

For the HTML that does not involve this templating, no errors were found.

#### CSS

The CSS3 code was passed through the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) and shows that there are no errors. A number of warnings were flagged and related to MS-Grid vendor prefixes.

#### Javascript

All Javascript code was passed through the [Esprima Syntax Validator](https://esprima.org/demo/validate.html) and was found to be syntactically valid.

#### Python

All Python code was passed through the [PEP8 Online validator](http://pep8online.com/) and is PEP8 compliant.


## Deployment

Having choosen Cloud9 as my IDE, the following steps were carried out:

* Install Python3 and Django to run the application.
* Create project - yogastudio
* Cloud9 included in the list of ALLOWED_HOSTS in staging settings, later heroku url will be added to ALLOWED_HOSTS
* Add run command to bashrc file 
* Create git repository - Initialise the repository, add files not required to the gitignore file. Carry out a `git add` and `git commit - "Initial Commit" `.
* Set up templates and static folders
* Create a env.py file containing the following environmental variables (add env.py file to the gitignore list):
 ```
STRIPE_PUBLISHABLE - Used solely to identify your account with Stripe; it isn't secret.
STRIPE_SECRET - Can perform any API request to Stripe without restriction.
DATABASE_URL - Remote PostgreSQL database link if using a remote database.
SECRET_KEY - Standard secret key, any value.
EMAIL_ADDRESS - to send correspondence from the site.
EMAIL_PASSWORD - authenticate email account.
AWS_ACCESS_KEY_ID - AWS user credentials.
AWS_SECRET_ACCESS_KEY - AWS S3 credentials.
```
* Generate a requirements.txt file so Heroku can install the required dependencies to run the app. `sudo pip3 freeze --local > requirements.txt`. The contents of the requirements.txt is referenced above.
* Python package gunicorn was installed
* Create a Procfile to tell Heroku what type of application is being deployed, and how to run it. `web: gunicorn yogastudio.wsgi:application`
* Create a new app on Heroku to host and run the site
* In Heroku go to resources and add a Postgres Database
* Retrieve the Postgres DB url and add to the env.py on cloud9
* In the settings.py file update the DB details to look at the DB hosted on Heroku
* This is followed by migrations `python3 manage.py makemigrations` and `python3 manage.py migrate` to  create tables on heroku database.
* Create a super user on the new DB `python3 manage.py createsuperuser`
* In Heroku, connect newly created app to the correct github repository.
* Set up config vars that are currently stored in our env.py file on Heroku.
* Create a bucket on Amazon S3, set up the appropriate permissions, groups, users and policies.
* In Cloud9 install the following: django-storages and boto3. `sudo pip3 install django-storages`, `sudo pip3 install boto3`, 
* Create a custom_storages.py file and add static file settings and media storage information to the setting.py file.
* Run `python3 manage.py collectstatic`
* Add DISABLE_COLLECTSTATIC with the value of 1 to the Config Variables on Heroku
* Enable automatic deploys from github to heroku.
* On completion of the project debug mode was set to False in the settings.py file.
 


## Credits

**Acknowledgements**

* I would like to thank my tutors and mentor at the Code Institute for all their help and support during the development of this project.
* Tutorials used to aid with the creation of this project - [Just Django](https://www.justdjango.com/learning-material), [Django Tutorials](https://manascode.com/), [Django Girls](https://djangogirls.org/resources/), [Polymorphic Products](https://django-polymorphic.readthedocs.io/en/stable/) and [Django Contact Forms](https://hellowebbooks.com/news/tutorial-setting-up-a-contact-form-with-django/).
* Code referenced for google map features [Google Map - Custom Style](https://snazzymaps.com/style/134/light-dream), [Google Map - Full width on contact page](https://mdbootstrap.com/docs/jquery/javascript/google-maps/) and [Google Map - Modal Box](https://embed.plnkr.co/plunk/ZDkUYz).

**Content:**

* All content is from the existing Headford Wellbeing Centre website which was written by the owner of the site and myself.

**Images:**

* Images acquired from [BigStockPhoto.com](https://www.bigstockphoto.com/) account, [Pexels](http://pexels.com), [Pixabay](https://pixabay.com/), [Unsplash](https://unsplash.com/) and [StockSnap](https://stocksnap.io/).
* Images from Owner of Headford Wellbeing Centre

**Contact**

Created by [Deirdre van der Zee](mailto:deirdrevanderzee@gmail.com).

