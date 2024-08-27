# Amazon Product Scraper

A Python tool for scraping Amazon product titles and prices, saving the results in an Excel file. Uses `requests`, `BeautifulSoup`, and `pandas` for efficient data extraction.

## Features

- Scrapes product titles and prices from Amazon search results.
- Saves the data in an Excel file (`data.xlsx`).
- Customizable for different search queries.

## Installation

### Prerequisites

- Python 3.x
- `pip` (Python package installer)

### Install Required Packages

Run the following command to install the necessary Python packages:

```bash
pip install requests beautifulsoup4 pandas openpyxl
```
## Usage

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/amazon-product-scraper.git
   cd amazon-product-scraper
2. **Run the scraper**:
   ```bash
   python ecom.py
   ```
3. **Output: The scraped data will be saved in data.xlsx in the same directory.**

## Example Output
| Title  | Price |
| ------------- | ------------- |
| ASUS ROG Zephyrus G14  | ₹1,50,000 |
| ASUS ROG Zephyrus G14 (2nd Gen)  | ₹1,70,000  |


## Limitations
* The script may not work if Amazon changes its HTML structure.
* Amazon may block requests from automated scripts, so consider using proxies or a headless browser for more complex scraping tasks.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
