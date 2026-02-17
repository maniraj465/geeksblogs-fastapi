from fastapi import FastAPI, HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException as StarletteHTTPException

from schemas import PostCreate, PostResponse
from datetime import date
import random

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


# Get all posts - UI
@app.get("/", include_in_schema=False, name="home")
@app.get("/posts", include_in_schema=False, name="posts")
def home(request: Request):
    return templates.TemplateResponse(
        request,
        "home.html",
        {"posts": posts, "title": "Home"},
    )

# Get post by ID - UI
@app.get("/posts/{post_id}", include_in_schema=False)
def post_page(request: Request, post_id: int):
    for post in posts:
        if post.get("id") == post_id:
            title = post["title"][:50]
            return templates.TemplateResponse(
                request,
                "post.html",
                {"post": post, "title": title},
            )
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found",)

# Get all posts - JSON
@app.get("/api/posts", response_model=list[PostResponse])
def get_posts():
    return posts

# Create post
@app.post(
    "/api/posts",
    response_model=PostResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_post(post: PostCreate):
    new_id = max(p["id"] for p in posts) + 1 if posts else 1
    new_post = {
        "id": new_id,
        "author": post.author,
        "title": post.title,
        "content": post.content,
        "date_posted": date.today().strftime("%B %d, %Y"),
        "profile_pic": 'g' + str(random.randint(1, 10)) + '.png'
    }
    posts.append(new_post)
    return new_post


@app.get("/api/posts/{post_id}", response_model=PostResponse)
def get_post(post_id: int):
    for post in posts:
        if post.get("id") == post_id:
            return post
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")


@app.exception_handler(StarletteHTTPException)
def general_http_exception_handler(request: Request, exception: StarletteHTTPException):
    message = (
        exception.detail
        if exception.detail
        else "An error occurred. Please check your request and try again."
    )

    if request.url.path.startswith("/api"):
        return JSONResponse(
            status_code=exception.status_code,
            content={"detail": message},
        )

    return templates.TemplateResponse(
        request,
        "error.html",
        {
            "status_code": exception.status_code,
            "title": exception.status_code,
            "message": message,
        },
        status_code=exception.status_code,
    )


@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exception: RequestValidationError):
    if request.url.path.startswith("/api"):
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            content={"detail": exception.errors()},
        )

    return templates.TemplateResponse(
        request,
        "error.html",
        {
            "status_code": status.HTTP_422_UNPROCESSABLE_CONTENT,
            "title": status.HTTP_422_UNPROCESSABLE_CONTENT,
            "message": "Invalid request. Please check your input and try again.",
        },
        status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
    )





posts: list[dict] = [
  {
    "id": 1,
    "author": "Sneha Kapoor",
    "title": "UI/UX Design Principles",
    "content": "Designing intuitive and user-friendly applications.",
    "date_posted": "February 5, 2026",
    "profile_pic": "g3.png"
  },
  {
    "id": 2,
    "author": "Rahul Mehta",
    "title": "CI/CD with Jenkins",
    "content": "Automating builds and deployments using Jenkins.",
    "date_posted": "January 24, 2026",
    "profile_pic": "b8.png"
  },
  {
    "id": 3,
    "author": "Neha Gupta",
    "title": "Next.js Server Rendering",
    "content": "SEO-friendly apps using Next.js SSR.",
    "date_posted": "February 11, 2026",
    "profile_pic": "g6.png"
  },
  {
    "id": 4,
    "author": "Vikram Singh",
    "title": "Microservices Architecture",
    "content": "Building scalable systems using microservices.",
    "date_posted": "January 14, 2026",
    "profile_pic": "b3.png"
  },
  {
    "id": 5,
    "author": "Shalini Arora",
    "title": "Progressive Web Apps",
    "content": "Offline-first web apps with PWA features.",
    "date_posted": "February 15, 2026",
    "profile_pic": "g8.png"
  },
  {
    "id": 6,
    "author": "Arjun Kumar",
    "title": "Spring Boot Fundamentals",
    "content": "Introduction to Spring Boot with real-world examples.",
    "date_posted": "January 10, 2026",
    "profile_pic": "b1.png"
  },
  {
    "id": 7,
    "author": "Ishita Banerjee",
    "title": "Testing Frontend Apps",
    "content": "End-to-end testing with Cypress and Jest.",
    "date_posted": "February 19, 2026",
    "profile_pic": "g10.png"
  },
  {
    "id": 8,
    "author": "Amit Verma",
    "title": "Kafka Messaging Systems",
    "content": "Event-driven communication using Apache Kafka.",
    "date_posted": "January 20, 2026",
    "profile_pic": "b6.png"
  },
  {
    "id": 9,
    "author": "Meera Ishan",
    "title": "State Management with Redux",
    "content": "Centralized state handling in frontend apps.",
    "date_posted": "February 17, 2026",
    "profile_pic": "g9.png"
  },
  {
    "id": 10,
    "author": "Rohit Sharma",
    "title": "REST API Design Basics",
    "content": "Understanding REST principles and best practices.",
    "date_posted": "January 12, 2026",
    "profile_pic": "b2.png"
  },
  {
    "id": 11,
    "author": "Kavya Reddy",
    "title": "TypeScript for Beginners",
    "content": "Strong typing and better tooling for JavaScript.",
    "date_posted": "February 7, 2026",
    "profile_pic": "g4.png"
  },
  {
    "id": 12,
    "author": "Suresh Patel",
    "title": "Docker for Java Developers",
    "content": "Containerizing Java applications using Docker.",
    "date_posted": "January 16, 2026",
    "profile_pic": "b4.png"
  },
  {
    "id": 13,
    "author": "Ritu Chawla",
    "title": "Web Accessibility Standards",
    "content": "Making applications usable for everyone.",
    "date_posted": "February 13, 2026",
    "profile_pic": "g7.png"
  },
  {
    "id": 14,
    "author": "Karan Malhotra",
    "title": "Hibernate ORM Guide",
    "content": "Mapping Java objects to relational databases.",
    "date_posted": "January 18, 2026",
    "profile_pic": "b5.png"
  },
  {
    "id": 15,
    "author": "Ananya Rao",
    "title": "Angular UI Development",
    "content": "Building dynamic user interfaces with Angular.",
    "date_posted": "February 1, 2026",
    "profile_pic": "g1.png"
  },
  {
    "id": 16,
    "author": "Nikhil Joshi",
    "title": "Unit Testing with JUnit",
    "content": "Writing reliable unit tests for Java applications.",
    "date_posted": "January 22, 2026",
    "profile_pic": "b7.png"
  },
  {
    "id": 17,
    "author": "Pooja Malhotra",
    "title": "Frontend Performance Optimization",
    "content": "Speeding up web apps using modern techniques.",
    "date_posted": "February 9, 2026",
    "profile_pic": "g5.png"
  },
  {
    "id": 18,
    "author": "Deepak Iyer",
    "title": "Spring Security Essentials",
    "content": "Implementing authentication and authorization.",
    "date_posted": "January 26, 2026",
    "profile_pic": "b9.png"
  },
  {
    "id": 19,
    "author": "Manoj Kulkarni",
    "title": "GraphQL with Java",
    "content": "Querying APIs efficiently using GraphQL.",
    "date_posted": "January 28, 2026",
    "profile_pic": "b10.png"
  },
  {
    "id": 20,
    "author": "Priya Nair",
    "title": "React Hooks Deep Dive",
    "content": "State and lifecycle management using React Hooks.",
    "date_posted": "February 3, 2026",
    "profile_pic": "g2.png"
  }
]

