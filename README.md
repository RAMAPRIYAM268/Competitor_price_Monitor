#  Competitor Price Monitoring System

> **An end-to-end data analytics solution developed using Python, BeautifulSoup, SQLite, Pandas, and Excel to automate product price collection, monitor inventory availability, and generate business reports for competitive market analysis.**

---

#  Overview

The **Competitor Price Monitoring System** is a web scraping and analytics solution designed to automate the collection of product information from an e-commerce website.

The project demonstrates a complete data pipeline that extracts product details, cleans and transforms the data, stores it in a relational database, and generates analytical reports for business decision-making.

Using **Python, BeautifulSoup, Pandas, SQLite, and Excel**, the solution enables organizations to monitor competitor pricing, evaluate product availability, analyze pricing trends, and support pricing strategy through automated reporting.

---

#  Business Problem

In highly competitive retail markets, pricing plays a significant role in influencing customer purchasing decisions.

Businesses need timely access to competitor pricing and inventory information to remain competitive.

Manual monitoring of competitor websites presents several challenges:

- Time-consuming price tracking
- Inconsistent data collection
- Limited visibility into market pricing
- Difficulty monitoring inventory availability
- Lack of centralized reporting

Without automation, businesses may miss pricing opportunities and struggle to make informed pricing decisions.

---

#  Solution

This project automates competitor product monitoring by collecting product information from an online bookstore and transforming it into structured business data.

The solution performs the following tasks:

- Extract product information from the website
- Clean and standardize collected data
- Store structured data in SQLite
- Generate CSV and Excel reports
- Produce SQL-based business summaries
- Support pricing and inventory analysis

---

#  Business Objectives

- Automate competitor price collection.
- Monitor product pricing efficiently.
- Track product availability.
- Store structured data for future analysis.
- Generate automated business reports.
- Demonstrate an end-to-end web scraping and analytics workflow.

---

# Project Workflow

##  Data Collection

- Web scraping using **Python Requests**
- HTML parsing using **BeautifulSoup**

---

##  Data Cleaning

- Remove currency symbols
- Convert prices into numeric format
- Remove unnecessary spaces
- Standardize product information

---

##  Data Storage

- Export cleaned dataset to CSV
- Store structured data in SQLite database
- Maintain organized product records

---

##  Business Reporting

Generate business reports including:

- Top Costliest Products
- Average Product Price
- Rating Distribution
- Product Availability

---

##  Report Export

Generate Excel reports for business users.

---

#  Business Process

```text
Website
   │
   ▼
Web Scraping
(Python + BeautifulSoup)
   │
   ▼
Data Cleaning
(Pandas)
   │
   ▼
SQLite Database
   │
   ▼
SQL Analysis
   │
   ▼
CSV Report
   │
   ▼
Excel Report
```

---

#  Key Performance Indicators (KPIs)

| KPI | Description |
|------|-------------|
| Total Products | Number of products scraped |
| Average Price | Average product price |
| Highest Price | Highest-priced product |
| Lowest Price | Lowest-priced product |
| Product Availability | Products currently in stock |
| Rating Distribution | Products grouped by rating |

---

#  Business Insights

The generated reports help answer important business questions, including:

- Which products have the highest prices?
- What is the average market price?
- Which products are currently available?
- How are products distributed across rating categories?
- Which products should be monitored for price changes?
- What pricing patterns exist across the catalog?

---

#  SQL Reports

The project automatically generates SQL reports including:

- Top 5 Costliest Products
- Average Product Price
- Rating-wise Product Count

These reports demonstrate how structured databases support business intelligence and operational reporting.

---

#  Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Web Scraping & Automation |
| Requests | HTTP Requests |
| BeautifulSoup | HTML Parsing |
| Pandas | Data Cleaning & Transformation |
| SQLite | Database Storage |
| SQL | Data Analysis |
| Excel | Business Reporting |

---

#  Project Structure

```text
Competitor_Price_Monitor/
│
├── app.py
├── requirements.txt
├── products.db
│
├── data/
│   └── products.csv
│
├── reports/
│   └── Daily_Report.xlsx
│
└── README.md
```

---

#  Installation

### Clone the repository

```bash
git clone https://github.com/RAMAPRIYAM268/Competitor_Price_Monitor.git
```

### Navigate to the project directory

```bash
cd Competitor_Price_Monitor
```

### Create a virtual environment

```bash
python -m venv scrap_env
```

### Activate the virtual environment

**Windows**

```bash
scrap_env\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

---

#  Output Files

After execution, the project automatically generates:

- [**products.csv**](data/products.csv) — Cleaned product dataset
- [**products.db**](products.db) — SQLite database
- [**Daily_Report.xlsx**](reports/Daily_Report.xlsx) — Excel business report
- SQL summary reports displayed in the console

---

# Future Enhancements

- Multi-page website scraping
- Automated daily price monitoring
- Historical price tracking
- Competitor price comparison dashboard
- Email notifications for price changes
- Scheduled execution using Task Scheduler or Cron
- Interactive Power BI dashboard
- Cloud database integration

---

#  Business Value

The **Competitor Price Monitoring System** demonstrates how web scraping and data analytics can automate market intelligence.

By integrating **data collection, cleaning, database storage, SQL analysis, and reporting** into a single workflow, the project enables businesses to:

- Monitor competitor pricing
- Analyze product availability
- Generate automated reports
- Support pricing strategy
- Improve data-driven decision-making

---

#  Author

**Ramapriya M**

**Aspiring Data Analyst | Python | SQL | Power BI | Excel | Streamlit**



