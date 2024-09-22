# Social Media API

This project is a Django-based Social Media API with user authentication, registration, and profile management.

## Features

- User registration with automatic token generation
- User login with token authentication
- User profile management (view and update)
- Custom user model with additional fields (bio, profile picture, followers)

## Technologies Used

- Django
- Django REST Framework
- Token Authentication

## Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd social_media_api
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```
   python manage.py makemigrations accounts
   python manage.py migrate
   ```

5. Create a superuser (for admin access):
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

## API Endpoints

- Register: `POST /api/accounts/register/`
  - Fields: username, email, password, bio (optional), profile_picture (optional)
  - Returns: token

- Login: `POST /api/accounts/login/`
  - Fields: username, password
  - Returns: token

- Profile: 
  - Get: `GET /api/accounts/profile/`
  - Update: `PUT /api/accounts/profile/`
  - Fields: bio, profile_picture

## Usage

### Registration

To register a new user, send a POST request to `/api/accounts/register/` with the following JSON body:

```json
{
  "username": "newuser",
  "email": "newuser@example.com",
  "password": "securepassword",
  "bio": "Hello, I'm new here!",
  "profile_picture": null
}
```

### Login

To login, send a POST request to `/api/accounts/login/` with the following JSON body:

```json
{
  "username": "newuser",
  "password": "securepassword"
}
```

### Authentication

For authenticated requests, include the token in the Authorization header:

```
Authorization: Token <your-token-here>
```

### Update Profile

To update a user's profile, send a PUT request to `/api/accounts/profile/` with the desired fields to update:

```json
{
  "bio": "Updated bio information"
}
```


### Posts

- List/Create Posts: `GET/POST /api/posts/`
- Retrieve/Update/Delete Post: `GET/PUT/DELETE /api/posts/<id>/`
- Search Posts: `GET /api/posts/?search=<query>`

### Comments

- List/Create Comments: `GET/POST /api/comments/`
- Retrieve/Update/Delete Comment: `GET/PUT/DELETE /api/comments/<id>/`

## Usage Examples

### Creating a Post

To create a new post, send a POST request to `/api/posts/` with the following JSON body:

```json
{
  "title": "My First Post",
  "content": "This is the content of my first post."
}
```

### Creating a Comment

To create a new comment, send a POST request to `/api/comments/` with the following JSON body:

```json
{
  "post": 1,
  "content": "This is a comment on the first post."
}
```

### Searching Posts

To search for posts, send a GET request to `/api/posts/?search=query`, replacing "query" with your search term.

## Development

This project uses a custom user model (`CustomUser`) which extends Django's `AbstractUser`. The model includes additional fields for `bio`, `profile_picture`, and a many-to-many relationship for `followers`.

## Testing

To run tests (once implemented):

```
python manage.py test
```