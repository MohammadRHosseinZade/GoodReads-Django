# GoodReads-Django


This is a Django REST API for managing books, reviews, and genres. It includes features for listing, creating, retrieving, updating, and deleting books and reviews. It also supports querying books by genre and recommending books based on user reviews.

## Table of Contents

- [Features](#features)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Swagger Documentation](#swagger-documentation)

## Features

- CRUD operations for books
- CRUD operations for reviews
- Query books by genre
- Recommend books based on user reviews
- JWT authentication for secure endpoints
- Swagger documentation for API endpoints
- Dockerized services for deployment

## Dependencies

- Docker
  
## Installation

1. **Clone the repository:**

   ```
   git clone https://github.com/MohammadRHosseinZade/GoodReads-Django.git
   cd GoodReads-Django
   ```
2.  **Run the project using docker:**
    ```
    docker compose up --build -d
    ```

## API Endpoints  
# Book Endpoints

- List and Create Books
- GET /books/
- POST /books/
- Retrieve, Update, and Delete a Book

- GET /books/{id}/
- PUT /books/{id}/
- PATCH /books/{id}/
- DELETE /books/{id}/
- Get Books by Genre
- GET /books/by-genre/?genre={genre_name}

# Review Endpoints
- List and Create Reviews

- GET /reviews/
- POST /reviews/
- Retrieve, Update, and Delete a Review

- GET /reviews/{id}/
- PUT /reviews/{id}/
- PATCH /reviews/{id}/
- DELETE /reviews/{id}/
 
 
 ##  Swagger Documentation

 http://127.0.0.1:8010/swagger/

 ## Default username and password

- Admin username: NetBanSharif
- Admin password: NetBan123

