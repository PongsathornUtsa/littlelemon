# Little Lemon Restaurant API

Welcome to the Little Lemon Restaurant API! Below are the API endpoints that we need tested.

## API Endpoints

### Menu API
- **List All Menu Items**: `GET /restaurant/menu/`
  - Retrieves a list of all menu items.
- **Create Menu Item**: `POST /restaurant/menu/`
  - Create a new menu item. Requires title, price, and inventory data.
- **Get Single Menu Item**: `GET /restaurant/menu/{id}/`
  - Retrieves details of a specific menu item.
- **Update Menu Item**: `PUT /restaurant/menu/{id}/`
  - Updates an existing menu item.
- **Delete Menu Item**: `DELETE /restaurant/menu/{id}/`
  - Deletes a specific menu item.

### Booking API
- **List All Bookings**: `GET /restaurant/bookings/`
  - Retrieves a list of all bookings.
- **Create Booking**: `POST /restaurant/bookings/`
  - Create a new booking. Requires name, no_of_guests, and booking_date.
- **Get Single Booking**: `GET /restaurant/bookings/{id}/`
  - Retrieves details of a specific booking.
- **Update Booking**: `PUT /restaurant/bookings/{id}/`
  - Updates details of an existing booking.
- **Delete Booking**: `DELETE /restaurant/bookings/{id}/`
  - Cancels a specific booking.

## Authentication Endpoints

### User Registration
- **Endpoint**: `POST /auth/users/`
- **Payload**: `{ "username": "user", "email": "user@example.com", "password": "securepassword" }`
- **Description**: Register a new user.

### Obtain Token
- **Endpoint**: `POST /auth/token/login/`
- **Payload**: `{ "username": "user", "password": "securepassword" }`
- **Description**: Obtain an authentication token for a registered user.

### Current User Info
- **Endpoint**: `GET /auth/users/me/`
- **Headers**: `{ "Authorization": "Token <your_token_here>" }`
- **Description**: Retrieve information about the current authenticated user.

### Logout (Token Invalidate)
- **Endpoint**: `POST /auth/token/logout/`
- **Headers**: `{ "Authorization": "Token <your_token_here>" }`
- **Description**: Logout the current user and invalidate the token.

### Change Password
- **Endpoint**: `POST /auth/users/set_password/`
- **Headers**: `{ "Authorization": "Token <your_token_here>" }`
- **Payload**: `{ "current_password": "oldpassword", "new_password": "newsecurepassword" }`
- **Description**: Change the password for the current authenticated user.  