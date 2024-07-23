# LittleLemon

/restaurant/bookings/tables/ => GET: "All of bookings" POST:"Create new book"(*requierment Authentication)

/restaurant/bookings/tables/{id}/ => GET: "Single book" ,PUT & PATCH: "Change data from specific ID", DELETE: "delete menu item by ID"

/restaurant/menu/ => GET: "All of menu items", POST: "Create new menu item"

/restaurant/menu/{id} => GET: "Single item",PUT & PATCH: "Change data from specific ID",DELETE: "delete menu item by ID"

/api-token-auth/ => POST: "Login with username and password and get Token"

/auth/users/ => GET: "Get all users", POST: "Create new user"

/auth/token/login => POST: "Login with username and password and get Token"


TIP: Do not forget to add your user and password of your database in the settings.py of project