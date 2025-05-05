# django-CRM

## 🛠️ Requirements

- Python 3.x
- MySQL Server (local or remote)
- Python package: `mysql-connector-python`

---

## 🔧 Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/keyurbhatiya/django-CRM.git
   cd django-CRM
   ```


2. **Install Required Python Package**

   ```bash
   pip install mysql-connector-python
   ```

---

## ⚙️ Configuration

Before running the script, make sure to update your MySQL credentials in `mydb.py`:

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="your_mysql_username",
  password="your_mysql_password",
  database="your_database_name"  # optional if you're creating a new one
)
```

---

## ▶️ Run the Script

To execute the Python script and run database operations:

```bash
python mydb.py
```

The output will show connection success and any operations like database/table creation or data manipulation.

---

## 💡 Example Code Snippet

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="yourpassword"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase")
```

---

## 🐞 Troubleshooting

* **Access Denied:** Ensure correct MySQL username/password.
* **Connection Error:** Check if MySQL server is running.
* **Module Not Found:** Reinstall `mysql-connector-python`.

---

## 👨‍💻 Author

**Keyur Bhatiya**
[GitHub Profile](https://github.com/keyurbhatiya)

