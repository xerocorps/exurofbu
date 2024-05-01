## Overview
AWS S3 Bucket Matcher is a tool designed to generate reports of matches between AWS S3 bucket names and URLs found in a given file. This tool is useful for cybersecurity analysts and bug hunters who need to quickly identify potential security risks or misconfigurations related to AWS S3 buckets.

## Features
- Efficiently searches for matches between AWS S3 bucket names and URLs
- Multithreaded processing for improved performance
- Customizable input and output file paths using command-line flags
- Generates a detailed JSON report of matched bucket names and URLs

## Requirements
- Python 3.x

## Usage
1. Clone the repository:
   ```
   git clone https://github.com/xerocorps/exurofbu.git
   ```

2. Navigate to the project directory:
   ```
   cd exurofbu
   ```

3. Run the tool with the following command:
   ```
   python exurofbu.py <buckets_file> <urls_file> <output_file>
   ```

   Replace `<buckets_file>`, `<urls_file>`, and `<output_file>` with the paths to your input files and desired output file.

## Example
```
python exurofbu.py buckets.txt urls.txt report.json
```

This command will read bucket names from `buckets.txt`, search for matches in `urls.txt`, and generate the report in `report.json`.
