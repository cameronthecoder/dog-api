# doggos 🐶
This is a small web application that shows cute dogs. For the frontend, it uses Vue.js and for the backend it uses the FastAPI micro-framework.

# Server
To get the server up and running, follow these steps:
1. Make sure you have Python installed
2. ``cd`` into the ``backend`` folder:
   ```bash
   cd backend
   ```
3. Create a virtual environment:
   ```bash
   $ python3 -m venv venv
   ```
4. Use the virtual environment you just created to install the dependencies:
   ```bash
   $ source venv/bin/activate
   $ pip install -r requirements.txt
   ```
5. Start the server:
   ```bash
   $ uvicorn app:app --reload
   ```


# Client
To get the client up and running, follow these steps:
1. ``cd`` into the ``frontend`` folder:
   ```bash
   $ cd frontend
   ```
2. Install the dependencies using either ``yarn`` or ``npm``
   ```bash
   $ yarn install
   ```
   or
   ```bash
   $ npm install
   ```
3. Start the server:
   ```bash
   $ yarn dev
   ```
   or
      ```bash
   $ npm dev
   ```
4. Add some dogos 🐕

# Contributions
If you would like to contribute to this project, feel free to do so by opening a pull request :)