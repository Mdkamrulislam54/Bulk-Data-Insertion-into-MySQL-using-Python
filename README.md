# 🚀 Bulk Data Insertion into MySQL using Python

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/MySQL-8.0+-4479A1?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License" />
</div>

<p align="center">
  <strong>Efficiently insert large CSV datasets into MySQL database with proper data type handling and error management.</strong>
</p>

---

## 📖 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Database Schema](#database-schema)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

This project demonstrates how to perform **bulk data insertion** from CSV files into MySQL databases using Python. It handles common issues like date format conversion, data type validation, and efficient batch processing for large datasets.

**Use Case:** Coffee Shop Sales Data Analysis - Insert transaction records into MySQL for further analysis and reporting.

---

## ✨ Features

✅ **Bulk Insert** - Efficiently insert thousands of records using `executemany()`  
✅ **Date Format Conversion** - Automatically converts DD/MM/YYYY to MySQL-compatible YYYY-MM-DD format  
✅ **Error Handling** - Comprehensive error catching and logging  
✅ **Data Validation** - Pre-insertion data quality checks  
✅ **Progress Tracking** - Real-time insertion progress updates  
✅ **Configurable** - Easy configuration through external config file  

---

## 📋 Prerequisites

Before running this project, ensure you have:

- **Python 3.8+** installed
- **MySQL Server 8.0+** running
- **pip** package manager
- Basic knowledge of SQL and Python

---

## 🔧 Installation

### Method 1: Clone the Repository (Recommended)

```bash
git clone https://github.com/Mdkamrulislam54/bulk-data-insertion-mysql.git
cd bulk-data-insertion-mysql
```

### Method 2: Download and Setup Manually

1. **Download** the repository as ZIP or create a new folder
2. **Open VS Code** → File → Open Folder → Select your project folder
3. **Place your CSV file** in the project folder

### Step 1: Install Required Packages

Open **Terminal** in VS Code (`Ctrl + ` ` or View → Terminal) and run:

```bash
pip install pandas mysql-connector-python
```

Or install all at once:

```bash
pip install pandas mysql-connector-python pymysql sqlalchemy
```

**Verify Installation:**
```bash
pip list
```

You should see:
- pandas
- mysql-connector-python
- pymysql (optional)
- sqlalchemy (optional)

### Step 2: Configure Your Script

Update the file path in your Python script to match your CSV location:

```python
# If CSV is in the same folder as your script
df = pd.read_csv("CoffeeShopSales.csv")

# Or use full path
df = pd.read_csv(r"C:\Users\Sajib\Desktop\Interactive Cares\Vs Code+Python\CoffeeShopSales.csv")
```

### Step 3: Update Database Credentials

```python
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="your_password",  # Change this!
    database="RFM"
)
```

---

## 🚀 Usage

### Step 1: Set Up MySQL Database

```sql
-- Create database
CREATE DATABASE IF NOT EXISTS RFM;
USE RFM;

-- Create table
CREATE TABLE transactions (
    transaction_id INT PRIMARY KEY,
    transaction_date DATE,
    transaction_time TIME,
    transaction_qty INT,
    store_id INT,
    store_location VARCHAR(100),
    product_id INT,
    unit_price DECIMAL(10, 2),
    product_category VARCHAR(100),
    product_type VARCHAR(100),
    product_detail VARCHAR(255)
);
```

### Step 2: Configure Database Connection

Edit `scripts/config.py`:

```python
DB_CONFIG = {
    "host": "127.0.0.1",
    "user": "your_username",
    "password": "your_password",
    "database": "RFM"
}
```

### Step 3: Run the Script

```bash
python scripts/bulk_insert.py
```

---

## 📊 Database Schema

```
transactions table
├── transaction_id (INT, PRIMARY KEY)
├── transaction_date (DATE)
├── transaction_time (TIME)
├── transaction_qty (INT)
├── store_id (INT)
├── store_location (VARCHAR)
├── product_id (INT)
├── unit_price (DECIMAL)
├── product_category (VARCHAR)
├── product_type (VARCHAR)
└── product_detail (VARCHAR)
```

---

## ⚙️ Configuration

### Database Settings

Modify `config.py` to match your MySQL setup:

```python
DB_CONFIG = {
    "host": "localhost",      # MySQL host
    "user": "root",           # MySQL username
    "password": "password",   # MySQL password
    "database": "RFM",        # Database name
    "port": 3306             # MySQL port (default: 3306)
}
```

### Data File Path

Update the CSV file path in `bulk_insert.py`:

```python
df = pd.read_csv("data/CoffeeShopSales.csv")
```

---

## 🐛 Troubleshooting

### Issue 1: Date Format Error

**Error:** `Incorrect date value: '01/01/2023'`

**Solution:** The script automatically converts dates from DD/MM/YYYY to YYYY-MM-DD format.

### Issue 2: Connection Refused

**Error:** `Can't connect to MySQL server`

**Solution:** 
- Verify MySQL is running: `mysql -u root -p`
- Check host and port in config.py
- Ensure firewall allows MySQL connections

### Issue 3: Module Not Found

**Error:** `ModuleNotFoundError: No module named 'mysql.connector'`

**Solution:**
```bash
pip install mysql-connector-python
```

### Issue 4: Access Denied

**Error:** `Access denied for user 'root'@'localhost'`

**Solution:** Verify username and password in config.py

---

## 📈 Performance Tips

🚀 **For Large Datasets (100K+ rows):**

1. **Increase Batch Size:** Modify `executemany()` batch size
2. **Disable Indexes:** Drop indexes before insertion, recreate after
3. **Use LOAD DATA INFILE:** For millions of rows, MySQL's native loader is faster
4. **Adjust MySQL Settings:**
   ```sql
   SET autocommit=0;
   SET unique_checks=0;
   SET foreign_key_checks=0;
   ```

---

## 📸 Screenshots

### Before Insertion
![Database Empty](images/before.png)

### After Successful Insertion
![Data Loaded](images/after.png)

### Console Output
```
Loading data from CSV...
✓ Data loaded successfully: 149,116 rows
Converting date formats...
✓ Date conversion completed
Connecting to MySQL database...
✓ Connected successfully
Inserting data...
Progress: [████████████████████] 100% Complete
✓ Bulk insert completed successfully!
Total records inserted: 149,116
Time taken: 45.3 seconds
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Md. Kamrul Islam**

- GitHub: [@Mdkamrulislam54](https://github.com/Mdkamrulislam54)
- LinkedIn: [Md. Kamrul Islam](https://www.linkedin.com/in/mdkamrulislam665)
- Email: kamrulislamsajib65@gmail.com

---

## 🙏 Acknowledgments

- Coffee Shop Sales dataset for testing
- MySQL and Python communities for excellent documentation
- Pandas library for efficient data manipulation

---

<div align="center">
  <p>If you find this project helpful, please ⭐ star this repository!</p>
  <img src="https://img.shields.io/github/stars/Mdkamrulislam54/bulk-data-insertion-mysql?style=social" alt="GitHub Stars" />
</div>
