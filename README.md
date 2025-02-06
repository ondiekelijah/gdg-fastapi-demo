## 🚀 Running the App Without Docker
To run the application locally without Docker:

### 1. 🐍 Set Up Virtual Environment
- **Create a virtual environment**:
```bash
   python3 -m venv venv
 ```

  ### Activate the Virtual Environment

- **On macOS and Linux:**

```
source venv/bin/activate
```

- **On Windows:**

```
. venv/Scripts/activate
```
2. 🛠️ Configure PostgreSQL

Update your PostgreSQL configuration in `alembic/env.py` and `src/core/config.py`.

3. 📦 Install Requirements

Use pip to install the necessary dependencies

```bash
pip install -r requirements.txt
```
4. ▶️ Run the Application

Use the start.sh script to initialize database migrations and start the application.

Development Mode:

```bash
alembic upgrade head
fastapi dev
```

Production Mode:

```bash
chmod 755 start.sh
sh start.sh
```

5. 🔍 Testing
API Documentation: Access the interactive API docs at `http://127.0.0.1:8000/docs` 📑

Swagger UI: Available at /docs endpoint