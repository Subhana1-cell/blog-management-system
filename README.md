# BlogSphere - Role-Based Blog Management System

BlogSphere is a dynamic role-based blog management system developed using Python and Django. The system allows public users to view blogs, browse blogs by category, search blogs, and read full blog details. It also includes an admin panel where authorized users can manage blogs, categories, users, roles, and permissions.

## Features

- Public homepage with featured and latest blogs
- All blogs page
- Blog detail page
- Category-wise blog filtering
- Blog search functionality
- Blog image support
- Dark 3D glassmorphism frontend design
- Responsive Bootstrap layout
- Django admin panel
- Blog management
- Category management
- User management
- Role management
- Permission-based access control
- Pagination
- Related blogs section
- Reading time display

## Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Web Framework | Django |
| Database | MySQL / SQLite for development |
| Frontend | HTML, CSS, Bootstrap 5 |
| Template Engine | Django Template Language |
| Admin Panel | Django Admin |
| Authentication | Django Authentication System |
| Authorization | Django Groups and Permissions |
| Version Control | Git and GitHub |
| IDE | Visual Studio Code |

## Why Django?

Django was selected because it provides many built-in features required for this project, including an admin panel, authentication, user management, groups, permissions, database models, routing, templates, and security features. These built-in tools made it easier to develop the blog management system quickly and efficiently.

## User Roles

| Role | Access |
|---|---|
| Super Admin | Full access to everything |
| Admin | Can manage blogs, categories, users, and roles |
| Editor | Can add and update blogs and categories |
| Author | Can add and update blogs |
| Viewer | Can only view blogs and categories |

## Main Modules

### Blog Module

The blog module manages blog posts with title, slug, content, category, author, image, status, created date, and updated date.

### Category Module

The category module organizes blogs into different categories. Users can browse blogs category-wise.

### User Management Module

User management is handled through Django’s built-in User model. Admin can create, update, delete, activate, and assign users to groups.

### Role and Permission Module

Role management is implemented using Django Groups. Permission management is implemented using Django’s built-in permission system.

### Search Module

Users can search blogs by title using the search feature.

## Project Folder Structure

```text
blog-management-system/
│
├── blog_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── blogs/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── templates/
│   ├── base.html
│   └── blogs/
│       ├── home.html
│       ├── blog_list.html
│       ├── blog_detail.html
│       ├── category_blogs.html
│       └── search.html
│
├── media/
│   └── blog_images/
│
├── manage.py
├── requirements.txt
└── README.md

URL Structure
URL	Purpose
/	Homepage
/blogs/	All blogs page
/blogs/<slug>/	Blog detail page
/category/<slug>/	Category-wise blog page
/search/	Search page
/admin/	Admin panel
Installation and Setup
1. Clone the repository
git clone https://github.com/Subhana1-cell/blog-management-system.git
cd blog-management-system
2. Create virtual environment
python -m venv venv
3. Activate virtual environment

For Windows:

venv\Scripts\activate
4. Install dependencies
pip install -r requirements.txt
5. Run migrations
python manage.py migrate
6. Create superuser
python manage.py createsuperuser
7. Run the server
python manage.py runserver

Open the website:

http://127.0.0.1:8000/

Open admin panel:

http://127.0.0.1:8000/admin/
Database

The project can work with SQLite during development. MySQL can also be configured in settings.py for final deployment or production use.

Example MySQL configuration:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog_db',
        'USER': 'root',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
Screenshots to Add

Screenshots can be added for:

Homepage
All Blogs page
Blog Detail page
Category page
Search page
Admin panel
Blog management page
Category management page
User management page
Group/role management page
Future Improvements
Comment system
Like and share feature
Rich text editor
Author dashboard
Blog approval workflow
Advanced search and filtering
Deployment to live server
Developer

Developed by Subhana Shakil