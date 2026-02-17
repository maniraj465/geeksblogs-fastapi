from fastapi import Depends, FastAPI, Request, HTTPException, status
from fastapi.exceptions import RequestValidationError
from fastapi.exception_handlers import (
    http_exception_handler,
    request_validation_exception_handler,
)
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()

templates = Jinja2Templates(directory="templates")


app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", include_in_schema=False)
@app.get("/home", include_in_schema=False, name="home")
async def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts": posts, "title": "Home"})

@app.get("/api/posts", name="post")
async def post(request: Request):
    return posts


@app.get("/posts", include_in_schema=False, name="post")
async def post(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts": posts, "title": "Posts"})


@app.get("/users/{user_id}/posts", include_in_schema=False, name="user_posts")
async def user_posts_page(request: Request, user_id: int):
    return templates.TemplateResponse(
        request,
        "post.html",
        {"posts": posts, "user": posts[user_id]['author'], "title": f"{posts[user_id]['author']}'s Posts"})

@app.get("/api/posts/{post_id}")
async def post_page(request: Request, post_id: int):
    for post in posts:
        if (post['id'] == post_id):
            return post

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")


@app.get("/posts/{post_id}", include_in_schema=False)
async def post_page(request: Request, post_id: int):
    for post in posts:
        if (post['id'] == post_id):
            title = post['title'][:50]
            return templates.TemplateResponse(request, "post.html", {"post": post, "title": title})

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")


@app.get("/login", include_in_schema=False)
async def login_page(request: Request):
    return templates.TemplateResponse(
        request,
        "login.html",
        {"title": "Login"},
    )


@app.get("/register", include_in_schema=False)
async def register_page(request: Request):
    return templates.TemplateResponse(
        request,
        "register.html",
        {"title": "Register"},
    )


@app.get("/account", include_in_schema=False)
async def account_page(request: Request):
    return templates.TemplateResponse(
        request,
        "account.html",
        {"title": "Account"},
    )


@app.exception_handler(StarletteHTTPException)
async def general_http_exception_handler(
    request: Request,
    exception: StarletteHTTPException,
):
    if request.url.path.startswith("/api"):
        return await http_exception_handler(request, exception)

    message = (
        exception.detail
        if exception.detail
        else "An error occurred. Please check your request and try again."
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
async def validation_exception_handler(
    request: Request,
    exception: RequestValidationError,
):
    if request.url.path.startswith("/api"):
        return await request_validation_exception_handler(request, exception)

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
    "author": "Maniraj 1",
    "title": "One day Crash Course Hands-on 1",
    "content": "This is FastAPI Crash Course 1",
    "date_posted": "February 15, 2026"
    },
    {
    "id": 2,
    "author": "Maniraj 2",
    "title": "One day Crash Course Hands-on 2",
    "content": "This is FastAPI Crash Course 2",
    "date_posted": "February 15, 2026"
    },
    {
    "id": 3,
    "author": "Maniraj 3",
    "title": "One day Crash Course Hands-on 3",
    "content": "This is FastAPI Crash Course 3",
    "date_posted": "February 15, 2026"
    },
    {
    "id": 4,
    "author": "Maniraj 4",
    "title": "One day Crash Course Hands-on 4",
    "content": "This is FastAPI Crash Course 4",
    "date_posted": "February 15, 2026"
    },
    {
    "id": 5,
    "author": "Maniraj 5",
    "title": "One day Crash Course Hands-on 5",
    "content": "This is FastAPI Crash Course 5",
    "date_posted": "February 15, 2026"
    },
    {
    "id": 6,
    "author": "Maniraj 6",
    "title": "One day Crash Course Hands-on 6",
    "content": "This is FastAPI Crash Course 6",
    "date_posted": "February 15, 2026"
    },
    {
    "id": 7,
    "author": "Maniraj 7",
    "title": "One day Crash Course Hands-on 7",
    "content": "This is FastAPI Crash Course 7",
    "date_posted": "February 15, 2026"
    },
    {
    "id": 8,
    "author": "Maniraj 8",
    "title": "One day Crash Course Hands-on 8",
    "content": "This is FastAPI Crash Course 8",
    "date_posted": "February 15, 2026"
    },
    {
    "id": 9,
    "author": "Maniraj 9",
    "title": "One day Crash Course Hands-on 9",
    "content": "This is FastAPI Crash Course 9",
    "date_posted": "February 15, 2026"
    },
    {
    "id": 10,
    "author": "Maniraj 10",
    "title": "One day Crash Course Hands-on 10",
    "content": "This is FastAPI Crash Course 10",
    "date_posted": "February 15, 2026"
    },
    {
    "id": 11,
    "author": "Maniraj 11",
    "title": "One day Crash Course Hands-on 11",
    "content": "This is FastAPI Crash Course 11",
    "date_posted": "February 15, 2026"
    },
    {
    "id": 12,
    "author": "Maniraj 12",
    "title": "One day Crash Course Hands-on 12",
    "content": "This is FastAPI Crash Course 12",
    "date_posted": "February 15, 2026"
    },
    {
    "id": 13,
    "author": "Maniraj 13",
    "title": "One day Crash Course Hands-on 13",
    "content": "This is FastAPI Crash Course 13",
    "date_posted": "February 15, 2026"
    },
    {
    "id": 14,
    "author": "Maniraj 14",
    "title": "One day Crash Course Hands-on 14",
    "content": "This is FastAPI Crash Course 14",
    "date_posted": "February 15, 2026"
    },
    {
    "id": 15,
    "author": "Maniraj 15",
    "title": "One day Crash Course Hands-on 15",
    "content": "This is FastAPI Crash Course 15",
    "date_posted": "February 15, 2026"
    },
    {
    "id": 16,
    "author": "Maniraj 16",
    "title": "One day Crash Course Hands-on 16",
    "content": "This is FastAPI Crash Course 16",
    "date_posted": "February 15, 2026"
    },
    {
    "id": 17,
    "author": "Maniraj 17",
    "title": "One day Crash Course Hands-on 17",
    "content": "This is FastAPI Crash Course 17",
    "date_posted": "February 15, 2026"
    },
    {
    "id": 18,
    "author": "Maniraj 18",
    "title": "One day Crash Course Hands-on 18",
    "content": "This is FastAPI Crash Course 18",
    "date_posted": "February 15, 2026"
    }
]




postsold: list[dict] = [
    {
    "id": "1",
    "title": "Fix login bug",
    "description": "Users cannot log in with special characters in password",
    "priority": "high",
    "status": "closed"
    },
    {
    "id": "2",
    "title": "Fix login bug2",
    "description": "Users cannot log in with special characters in password 2",
    "priority": "high",
    "status": "open"
    },
    {
    "id": "3",
    "title": "Fix login bug3",
    "description": "Users cannot log in with special characters in password 3",
    "priority": "high",
    "status": "open"
    },
    {
    "id": "4",
    "title": "Fix login bug4",
    "description": "Users cannot log in with special characters in password 4",
    "priority": "high",
    "status": "open"
    },
    {
    "id": "5",
    "title": "Fix login bug5",
    "description": "Users cannot log in with special characters in password 5",
    "priority": "high",
    "status": "open"
    }
]