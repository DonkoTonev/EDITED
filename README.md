# MarksAndSpencer Spider

This Scrapy spider, `MarksAndSpencerSpider`, is designed to scrape product information from the Marks & Spencer website. The spider navigates through various sections of the site, specifically targeting the "Easy Iron Geometric Print Shirt" in the "Casual shirts" category under the Men's section, and extracts details such as product name, price, available sizes, color, and reviews.

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/marksandspencer-spider.git
   cd marksandspencer-spider
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. **Install the required dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. **Navigate to the project directory:**
   ```sh
   cd EDITED_task
   cd EDITED_task
   cd spiders
   ```

2. **Run the spider:**
   ```sh
   scrapy crawl marksandspencer
   ```
This command will execute the spider and save the scraped data to output.json.


