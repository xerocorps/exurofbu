import json
import threading
import argparse

# Function to search for matches for a bucket
def search_matches(bucket, matches, urls):
    print(f"Searching for matches in '{urls_file}' for bucket '{bucket}'...")
    for line in urls:
        if bucket in line:
            matches.append(line.strip())
    print(f"Found {len(matches)} match(es) for bucket '{bucket}'")

# Main function
def main(buckets_file, urls_file, output_file):
    # Read bucket names from the file
    print(f"Reading bucket names from '{buckets_file}'...")
    with open(buckets_file, 'r') as f:
        bucket_names = [line.strip() for line in f if line.strip()]

    # Read URLs file into memory
    print(f"Reading URLs from '{urls_file}'...")
    with open(urls_file, 'r') as f:
        urls = f.readlines()

    # Create a list to hold threads
    threads = []

    # Create a dictionary to store bucket matches
    report_data = []

    # Iterate over each bucket name and create a thread to search for matches
    print("Searching for matches for each bucket...")
    for bucket in bucket_names:
        matches = []
        thread = threading.Thread(target=search_matches, args=(bucket, matches, urls))
        threads.append((bucket, thread, matches))
        thread.start()

    # Wait for all threads to complete
    for bucket, thread, matches in threads:
        thread.join()
        if matches:
            report_data.append({
                "bucket": bucket,
                "matches": matches
            })

    # Write report data to JSON file
    print(f"Writing report to '{output_file}'...")
    with open(output_file, 'w') as f:
        json.dump(report_data, f, indent=4)

    print("Report generation completed successfully.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a report of matches for AWS S3 buckets.")
    parser.add_argument("buckets_file", help="Path to the file containing bucket names.")
    parser.add_argument("urls_file", help="Path to the file containing URLs to search for matches.")
    parser.add_argument("output_file", help="Path to the output JSON file.")
    args = parser.parse_args()

    main(args.buckets_file, args.urls_file, args.output_file)
