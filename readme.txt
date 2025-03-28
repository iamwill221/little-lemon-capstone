LITTLE LEMON API DOCUMENTATION

AUTHENTICATION ENDPOINTS
* Register a new user: POST /auth/users/
* Obtain authentication token: POST /auth/token/login/
* Alternative endpoint to obtain auth token: POST /restaurant/api-token-auth/

MENU ENDPOINTS
* List all menu items: GET /restaurant/menu/
* Add a new menu item: POST /restaurant/menu/
* Get specific menu item: GET /restaurant/menu/<id>
* Update specific menu item: PUT /restaurant/menu/<id>
* Delete specific menu item: DELETE /restaurant/menu/<id>

BOOKING ENDPOINTS (REQUIRES AUTHENTICATION)
* List all bookings: GET /restaurant/booking/tables/
* Create new booking: POST /restaurant/booking/tables/
* Get specific booking: GET /restaurant/booking/tables/<id>
* Update specific booking: PUT /restaurant/booking/tables/<id>
* Delete specific booking: DELETE /restaurant/booking/tables/<id>