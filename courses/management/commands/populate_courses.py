from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils.text import slugify
from courses.models import Subject, Course, Module, Text, Video


class Command(BaseCommand):
    help = "Populate database with sample Computer Science courses"

    def handle(self, *args, **kwargs):
        self.stdout.write("Populating database with Computer Science courses...")

        # Get or create admin user as course owner
        admin_user, created = User.objects.get_or_create(
            username="admin",
            defaults={
                "email": "admin@masomo.com",
                "is_staff": True,
                "is_superuser": True,
            },
        )
        if created:
            admin_user.set_password("admin")
            admin_user.save()
            self.stdout.write(self.style.SUCCESS("Created admin user"))

        # Create Computer Science subjects
        subjects_data = [
            {"title": "Web Development", "slug": "web-development"},
            {"title": "Data Science", "slug": "data-science"},
            {"title": "Machine Learning", "slug": "machine-learning"},
            {"title": "Computer Networks", "slug": "computer-networks"},
            {"title": "Database Systems", "slug": "database-systems"},
        ]

        subjects = {}
        for subject_data in subjects_data:
            subject, created = Subject.objects.get_or_create(
                slug=subject_data["slug"], defaults={"title": subject_data["title"]}
            )
            subjects[subject_data["slug"]] = subject
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Created subject: {subject_data['title']}")
                )

        # Create courses with modules
        courses_data = [
            {
                "subject": "web-development",
                "title": "Full Stack Web Development with Django",
                "overview": "Learn to build complete web applications using Django framework. Master both frontend and backend development, database integration, and deployment strategies.",
                "modules": [
                    {
                        "title": "Introduction to Django",
                        "description": "Getting started with Django framework, understanding MVT architecture, and setting up your development environment.",
                        "contents": [
                            {
                                "type": "text",
                                "title": "What is Django?",
                                "content": "Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development.",
                            },
                            {
                                "type": "video",
                                "title": "Django Tutorial",
                                "url": "https://www.youtube.com/watch?v=F5mRW0jo-U4",
                            },
                        ],
                    },
                    {
                        "title": "Models and Databases",
                        "description": "Understanding Django ORM, creating models, and working with databases.",
                        "contents": [
                            {
                                "type": "text",
                                "title": "Django Models",
                                "content": "Models define the structure of your database. Each model is a Python class that subclasses django.db.models.Model. Each attribute of the model represents a database field.",
                            }
                        ],
                    },
                    {
                        "title": "Views and Templates",
                        "description": "Creating dynamic views and rendering templates in Django.",
                        "contents": [
                            {
                                "type": "text",
                                "title": "Understanding Views",
                                "content": "A view is a Python function that takes a web request and returns a web response. Views contain the logic that processes requests and returns responses.",
                            }
                        ],
                    },
                ],
            },
            {
                "subject": "data-science",
                "title": "Python for Data Science and Analytics",
                "overview": "Master data analysis and visualization using Python. Learn pandas, NumPy, Matplotlib, and apply statistical methods to real-world datasets.",
                "modules": [
                    {
                        "title": "Introduction to Data Science",
                        "description": "Understanding data science fundamentals and the Python ecosystem for data analysis.",
                        "contents": [
                            {
                                "type": "text",
                                "title": "What is Data Science?",
                                "content": "Data Science combines statistics, mathematics, programming, and domain expertise to extract insights from data. Python has become the leading language for data science due to its powerful libraries.",
                            },
                            {
                                "type": "video",
                                "title": "Data Science Overview",
                                "url": "https://www.youtube.com/watch?v=ua-CiDNNj30",
                            },
                        ],
                    },
                    {
                        "title": "NumPy and Pandas Basics",
                        "description": "Learning the fundamental libraries for data manipulation in Python.",
                        "contents": [
                            {
                                "type": "text",
                                "title": "Introduction to NumPy",
                                "content": "NumPy is the fundamental package for scientific computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with mathematical functions.",
                            }
                        ],
                    },
                    {
                        "title": "Data Visualization",
                        "description": "Creating meaningful visualizations using Matplotlib and Seaborn.",
                        "contents": [
                            {
                                "type": "text",
                                "title": "Visualization Best Practices",
                                "content": "Effective data visualization helps communicate insights clearly. Learn to choose the right chart type for your data and tell compelling stories with visualizations.",
                            }
                        ],
                    },
                ],
            },
            {
                "subject": "machine-learning",
                "title": "Machine Learning Fundamentals",
                "overview": "Dive into machine learning algorithms, supervised and unsupervised learning, model evaluation, and practical implementation using scikit-learn.",
                "modules": [
                    {
                        "title": "Introduction to Machine Learning",
                        "description": "Understanding ML concepts, types of learning, and the ML workflow.",
                        "contents": [
                            {
                                "type": "text",
                                "title": "What is Machine Learning?",
                                "content": "Machine Learning is a subset of artificial intelligence that enables systems to learn and improve from experience without being explicitly programmed. It focuses on developing computer programs that can access data and use it to learn.",
                            },
                            {
                                "type": "video",
                                "title": "Machine Learning Basics",
                                "url": "https://www.youtube.com/watch?v=ukzFI9rgwfU",
                            },
                        ],
                    },
                    {
                        "title": "Supervised Learning",
                        "description": "Learning classification and regression algorithms.",
                        "contents": [
                            {
                                "type": "text",
                                "title": "Classification vs Regression",
                                "content": "Supervised learning involves learning from labeled data. Classification predicts discrete categories while regression predicts continuous values. Both are fundamental to machine learning.",
                            }
                        ],
                    },
                    {
                        "title": "Model Evaluation",
                        "description": "Techniques for evaluating and improving model performance.",
                        "contents": [
                            {
                                "type": "text",
                                "title": "Cross-Validation",
                                "content": "Cross-validation is a technique to evaluate model performance by splitting data into training and testing sets multiple times. This helps ensure your model generalizes well to new data.",
                            }
                        ],
                    },
                ],
            },
            {
                "subject": "computer-networks",
                "title": "Computer Networks and Security",
                "overview": "Understand networking fundamentals, protocols, network architecture, and cybersecurity principles. Learn about TCP/IP, routing, and network security.",
                "modules": [
                    {
                        "title": "Network Fundamentals",
                        "description": "Introduction to computer networks, OSI model, and basic networking concepts.",
                        "contents": [
                            {
                                "type": "text",
                                "title": "What is a Computer Network?",
                                "content": "A computer network is a set of computers sharing resources located on or provided by network nodes. Networks enable communication and resource sharing between devices.",
                            },
                            {
                                "type": "video",
                                "title": "Networking Basics",
                                "url": "https://www.youtube.com/watch?v=3QhU9jd03a0",
                            },
                        ],
                    },
                    {
                        "title": "TCP/IP Protocol Suite",
                        "description": "Understanding the TCP/IP model and internet protocols.",
                        "contents": [
                            {
                                "type": "text",
                                "title": "TCP/IP Layers",
                                "content": "The TCP/IP model consists of four layers: Application, Transport, Internet, and Network Access. Each layer has specific responsibilities in data transmission.",
                            }
                        ],
                    },
                    {
                        "title": "Network Security",
                        "description": "Introduction to cybersecurity, encryption, and secure network design.",
                        "contents": [
                            {
                                "type": "text",
                                "title": "Security Principles",
                                "content": "Network security involves protecting data during transmission and storage. Key principles include confidentiality, integrity, and availability (CIA triad).",
                            }
                        ],
                    },
                ],
            },
            {
                "subject": "database-systems",
                "title": "Database Design and SQL",
                "overview": "Master database concepts, SQL queries, normalization, and database design. Learn to work with relational databases and optimize queries for performance.",
                "modules": [
                    {
                        "title": "Database Fundamentals",
                        "description": "Introduction to databases, DBMS, and relational database concepts.",
                        "contents": [
                            {
                                "type": "text",
                                "title": "What is a Database?",
                                "content": "A database is an organized collection of structured information or data. Database Management Systems (DBMS) provide tools to create, manage, and query databases efficiently.",
                            },
                            {
                                "type": "video",
                                "title": "Database Introduction",
                                "url": "https://www.youtube.com/watch?v=wR0jg0eQsZA",
                            },
                        ],
                    },
                    {
                        "title": "SQL Basics",
                        "description": "Learning SQL syntax for querying and manipulating data.",
                        "contents": [
                            {
                                "type": "text",
                                "title": "SQL Commands",
                                "content": "SQL (Structured Query Language) is used to communicate with databases. Basic commands include SELECT for querying, INSERT for adding data, UPDATE for modifying, and DELETE for removing data.",
                            }
                        ],
                    },
                    {
                        "title": "Database Design",
                        "description": "Normalization, relationships, and schema design best practices.",
                        "contents": [
                            {
                                "type": "text",
                                "title": "Normalization",
                                "content": "Database normalization organizes data to reduce redundancy and improve data integrity. Normal forms (1NF, 2NF, 3NF) provide guidelines for effective database design.",
                            }
                        ],
                    },
                ],
            },
        ]

        for course_data in courses_data:
            subject = subjects[course_data["subject"]]
            slug = slugify(course_data["title"])

            course, course_created = Course.objects.get_or_create(
                slug=slug,
                defaults={
                    "owner": admin_user,
                    "subject": subject,
                    "title": course_data["title"],
                    "overview": course_data["overview"],
                },
            )

            if course_created:
                self.stdout.write(
                    self.style.SUCCESS(f"Created course: {course_data['title']}")
                )

                #  modules and content
                for module_data in course_data["modules"]:
                    module = Module.objects.create(
                        course=course,
                        title=module_data["title"],
                        description=module_data["description"],
                    )

                    #  content items
                    for content_data in module_data["contents"]:
                        if content_data["type"] == "text":
                            Text.objects.create(
                                owner=admin_user,
                                title=content_data["title"],
                                content=content_data["content"],
                            )
                        elif content_data["type"] == "video":
                            Video.objects.create(
                                owner=admin_user,
                                title=content_data["title"],
                                url=content_data["url"],
                            )

                    self.stdout.write(f"  - Created module: {module_data['title']}")

        self.stdout.write(
            self.style.SUCCESS(
                "\nSuccessfully populated database with Computer Science courses!"
            )
        )
        self.stdout.write(
            self.style.SUCCESS(
                f"Created {Course.objects.count()} courses across {Subject.objects.count()} subjects"
            )
        )
