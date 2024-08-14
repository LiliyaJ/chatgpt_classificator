# Project: BigQuery Cloud Functions for Content Classification

This project provides Python scripts (`main.py` and `helper.py`) designed to classify webpage content within a BigQuery workflow. This is particularly useful for analyzing and visualizing the performance of webpages based on their content categories.

## Files Overview

- **`main.py`**:
- This script is optimized to be deployed as a Google Cloud Function. It takes URLs and a set of classes as input from BigQuery, processes them, and returns the content classification. The classification result can then be used in BigQuery tables for further analysis and visualization.

- **`helper.py`**:
- Contains two functions:

  - `get_content(url)`: Scrapes the content from the provided URL, removes HTML tags, and extracts the plain text.
  - `get_class(url, classes)`: Utilizes `get_content(url)` to retrieve the page content and then invokes a classification service (e.g., ChatGPT) to classify the content into one of the specified classes.

- **`requirements.txt`**:
- Lists the Python dependencies necessary to run the project.

## Installation and Setup

1. **Clone the Repository**:

- Clone the project repository to your local environment.

2. **Install Dependencies**:

- Navigate to the project directory and install the required dependencies with:

  ```sh
  pip install -r requirements.txt
  ```

3. **Deploy Cloud Function**:

- Deploy `main.py` as a Cloud Function. You can do this using the Google Cloud Console or Google Cloud CLI. The function should be set up to trigger via HTTP requests.

4. **BigQuery Integration**:

- Link the Cloud Function with your BigQuery SQL module. This setup allows BigQuery to pass URLs and classification parameters to the Cloud Function and receive the classification result as part of your data processing pipeline.

## Usage

1. **BigQuery Workflow**:

- Use the deployed Cloud Function within your BigQuery SQL queries. This is done by invoking the function with URLs and content classes as inputs. The function processes the request and returns the classification, which is then used to enrich your BigQuery tables.

2. **Sample Use Case**:

- For example, a client wants to classify webpages and this classification cannot be done technically with url (e.g., "SEO", "SEA", "Web Analytics") and then analyze how each type is performing based on metrics like page views, bounce rates, etc.

- **Input**:

  - `url`: "https://example.com/blog_article_about_marketing"
  - `classes`: "SEO", "SEA", "Web Analytics"

- **Output**:

  - The function returns a classification like "SEA".

- This result can then be stored in a BigQuery table and used for further analysis or visualization in tools like Google Data Studio.

## Example BigQuery SQL Query

Here’s an example of how you might use the Cloud Function within a BigQuery SQL query:

```sql
SELECT
 url,
 page_views,
 bounce_rate,
 invoke_function('YOUR_CLOUD_FUNCTION_URL', url, "SEO", "SEA", "Web Analytics") as content_type
FROM
 `your_project.your_dataset.your_table`

**Explanation**:
- The `invoke_function` placeholder represents the mechanism BigQuery uses to call the Cloud Function. Replace it with the actual method for invoking HTTP functions in BigQuery.
- The Cloud Function returns the `content_type` based on the provided URL and classes.

```
