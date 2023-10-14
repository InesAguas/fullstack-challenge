### Recruitment Challenge

The aim of this challenge is to add features to an existing simplified meal ordering platform, which, in the current state, looks like shown in screenshots below.

![image](https://github.com/kevin-kessler/origin-full-stack-restaurant-challenge/assets/13378028/40bf6fd0-9a43-4ea8-842e-9b5007834c86)

![image](https://github.com/kevin-kessler/origin-full-stack-restaurant-challenge/assets/13378028/abd6ecc6-ab03-4845-86e0-9b4aa0722b33)

Please use the code provided in this repository as the base for your solution and extend it by the requested features mentioned below.

Your implementation should have a clean code structure, follow best practices, and optionally include some test coverage.

The challenge comprises the following tasks:

#### 1. **User Authentication:**
   - Create a client-side modal for login and registration.
   - Implement new endpoints on the server side to handle login and registration.
   - Set up the necessary database structures (i.e. a `User` table) and persist user data upon registration.

#### 2. **Dish Orders:**
   - Users should be able to order dishes
      1. By first putting dishes into a shopping cart.
      2. And then submitting the content of the shopping cart as order to the server.
      3. The server then should persist that order in the database.

#### 3. **Dish Reviews:**
   - Users should be able to:
      1. Provide a rating for a dish from 1 to 5.
      2. Leave a comment alongside their rating.
      3. View the average rating of the dish.
      4. View comments and associated ratings of other users.
   - Constraint: One user can only give one review per dish, and only after having ordered that dish.
   - Reviews (rating and comments) should be persisted in the database.

#### 4. **User-Restaurant Chat:**
   - Implement an interactive chat feature between user and restaurant employee. The content of the employee's responses don't need to make sense and can be hardcoded/scripted.
   - Allow users to:
      1. Initiate and end chat conversations.
      2. The chat should automatically end if the customer is inactive for a predetermined period.
   - There is no need to persist chat conversations in the database.

#### 5. **Order Page:**
   - Ensure users can only view their own order history.
   - Implement an order tracking feature that allows to view the status/progress of a user's orders.
   - An order can be in either of the following states:
      - **Submitted:** User submitted the order. Restaurant is reviewing.
      - **Approved:** Restaurant approved the order
      - **Rejected:** Restaurant rejected the order
      - **Canceled:** User canceled the order
      - **In Preparation:** Restaurant is preparing the order
      - **In Delivery:** The order is out for delivery
      - **Delivered:** The order has been delivered
   - In your solution, please explain the transitions between these states and create a state machine to manage them.
   - For simplicity, allow users to trigger all actions in the UI, but ensure these actions adhere to the state transitions defined.
   - Note: A user can only cancel an order as long as the order is not yet in preparation.
   - Make sure to extend the database schema to be able to persist and update an order's status.


### How to run the app
We assume you have docker desktop installed. Next, run the setup script which will create a docker volume and create SSL certificates for you to develop locally your app (follow the instructions given by the `setup.sh` script):

`./scripts/setup.sh`

After doing so, just run the following command to run the current application stack:

`docker compose --profile app up -d`

This command will launch 4 containers:
- Python server using FastAPI framework
- Vue client development server
- Postgres Database
- Traefik Proxy

The whole stack comes with hot-reloading enabled so you should be able to write code and see the result automatically without any compilation or relaunch steps.

You will be able to access:
- Client: `https://localhost:8443/client/`
- Server API: `https://localhost:8443/api`
- Server Docs: `https://localhost:8443/api/docs`

Please let us know if you encounter any issue while trying to launch the current application.

### Rules
- Please implement your solution with the Vue.js (v3) and FastAPI frameworks.
- Please only use packages that are being shipped with this challenge. This concerns both, front-end and back-end. For example, the front-end includes the packages `primeflex`, `primeicons` and `primevue` which should be sufficient for completing this challenge.

### Submission
- Please submit your solution as a zip file. It should contain the entire repository, including your .git folder.
- Please name your zip file by the following format: firstname_lastname.zip, where firstname is your first name and lastname is your last name.
- Please make sure to submit your solution before the deadline. The deadline as well as the location for the submission are mentioned in the e-Mail which invited you to this challenge.
