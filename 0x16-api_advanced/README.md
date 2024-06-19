# 0x16-api_advanced

This directory contains Python scripts that interact with the Reddit API to perform various tasks using advanced API features.

## Contents

- **count_words.py**: A Python script that recursively queries the Reddit API, parses the titles of all hot articles, and prints a sorted count of specified keywords.

- **recurse.py**: A Python script that recursively queries the Reddit API to retrieve the titles of all hot articles for a given subreddit.

## Scripts

### 1. count_words.py

This script recursively queries the Reddit API to count occurrences of specified keywords in the titles of hot articles for a given subreddit. It handles pagination and prints results sorted by count (descending) and word (ascending).

#### Usage:

```bash
python3 count_words.py <subreddit> <word1> <word2> ...
```

- `<subreddit>`: The name of the subreddit to query.
- `<word1> <word2> ...`: Keywords to count occurrences in titles. Separate multiple words with spaces.

#### Example:

```bash
python3 count_words.py python javascript java
```

### 2. recurse.py

This script recursively queries the Reddit API to retrieve the titles of all hot articles for a given subreddit. It handles pagination and prints the titles of hot articles.

#### Usage:

```bash
python3 recurse.py <subreddit>
```

- `<subreddit>`: The name of the subreddit to query.

#### Example:

```bash
python3 recurse.py python
```

## Requirements

- Python 3.x
- Requests library (`pip install requests`)

Ensure that your Python environment has the necessary dependencies installed before running the scripts.

---

Feel free to adjust the paths, descriptions, or examples based on your specific implementation details or preferences. This README provides a structured overview of the scripts in the `0x16-api_advanced` directory, their purpose, how to use them, and any necessary dependencies.
