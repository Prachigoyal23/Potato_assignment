# Twitter Query API

This project is a Flask application that allows you to query tweets about Britney Spears from a TSV file. You can search for specific terms and retrieve various metrics related to the tweets.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [API Endpoint](#api-endpoint)
- [Example Queries](#example-queries)
- [License](#license)

## Features
- Count of tweets containing a search term by day.
- Number of unique users posting tweets with the term.
- Average likes for tweets containing the term.
- Place IDs from where the tweets were posted.
- Time of day when the tweets were posted.
- User who posted the most tweets containing the term.

## Requirements
- Python 3.7 or higher
- Flask
- pandas

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
