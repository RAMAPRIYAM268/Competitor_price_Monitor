# ==========================================
# Book Scraper Project
# Website -> Python -> Pandas -> SQL -> Excel
# ==========================================

import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
import os

# ------------------------------------------
# Create folders
# ------------------------------------------

os.makedirs("data", exist_ok=True)
os.makedirs("reports", exist_ok=True)

# ------------------------------------------
# Step 1 : Scrape Website
# ------------------------------------------

def scrape():

    url = "https://books.toscrape.com/"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    products = soup.find_all("article", class_="product_pod")

    product_list = []

    for product in products:

        name = product.h3.a["title"]

        price = product.find(
            "p",
            class_="price_color"
        ).text

        rating = product.find(
            "p",
            class_="star-rating"
        )["class"][1]

        availability = product.find(
            "p",
            class_="instock availability"
        ).text.strip()

        product_list.append({
            "Book Name": name,
            "Price": price,
            "Rating": rating,
            "Availability": availability
        })

    return pd.DataFrame(product_list)


# ------------------------------------------
# Step 2 : Clean Data
# ------------------------------------------

def clean(df):

    # Remove Pound symbol
    df["Price"] = (
        df["Price"]
        .str.replace("£", "", regex=False)
        
    )

    # Remove extra spaces
    df["Book Name"] = df["Book Name"].str.strip()
    df["Availability"] = df["Availability"].str.strip()

    return df


# ------------------------------------------
# Step 3 : Save CSV
# ------------------------------------------

def save_csv(df):

    df.to_csv(
        "data/products.csv",
        index=False
    )

    print("CSV Saved Successfully")


# ------------------------------------------
# Step 4 : Save Database
# ------------------------------------------

def save_database(df):

    conn = sqlite3.connect("products.db")

    df.to_sql(
        "products",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()

    print("Database Saved Successfully")


# ------------------------------------------
# Step 5 : SQL Report
# ------------------------------------------

def report():

    conn = sqlite3.connect("products.db")

    print("\n==========================")
    print("SQL REPORT")
    print("==========================")

    print("\nTop 5 Costliest Books\n")

    query1 = """
    SELECT *
    FROM products
    ORDER BY Price DESC
    LIMIT 5
    """

    print(pd.read_sql(query1, conn))

    print("\nAverage Price\n")

    query2 = """
    SELECT AVG(Price) AS Average_Price
    FROM products
    """

    print(pd.read_sql(query2, conn))

    print("\nRating Count\n")

    query3 = """
    SELECT Rating,
           COUNT(*) AS Total
    FROM products
    GROUP BY Rating
    """

    print(pd.read_sql(query3, conn))

    conn.close()


# ------------------------------------------
# Step 6 : Export Excel
# ------------------------------------------

def save_excel(df):

    df.to_excel(
        "reports/Daily_Report.xlsx",
        index=False
    )

    print("Excel Report Generated")


# ------------------------------------------
# Main Function
# ------------------------------------------

def main():

    print("Scraping Website...")

df = scrape()

print(df.head())

print("\nCleaning Data...")

df = clean(df)

save_csv(df)

save_database(df)

save_excel(df)

report()

print("\nProject Completed Successfully")


# ------------------------------------------
# Run Program
# ------------------------------------------

if __name__ == "__main__":
    main()

