# Python---Netflix-Analysis-of-1990-s-movies
Data analysis using Python of Netflix movies data

## Project Overview

This project focuses on exploring Netflix data, specifically analyzing movies released during the 1990s. As a production company specializing in nostalgic styles, the objective is to better understand trends in movie durations and genres during this decade.

## Dataset

The analysis uses the `netflix_data.csv` dataset, which contains the following columns:

| Column         | Description                           |
|----------------|---------------------------------------|
| `show_id`      | The ID of the show                   |
| `type`         | Type of show                         |
| `title`        | Title of the show                    |
| `director`     | Director of the show                 |
| `cast`         | Cast of the show                     |
| `country`      | Country of origin                    |
| `date_added`   | Date added to Netflix                |
| `release_year` | Year of Netflix release              |
| `duration`     | Duration of the show in minutes      |
| `description`  | Description of the show              |
| `genre`        | Show genre                           |

## Analysis Steps

1. **Filter Movies Released in the 1990s**
   - Filtered the dataset to include only rows where `type` is "Movie" and `release_year` is between 1990 and 1999 (inclusive).

2. **Find the Most Frequent Movie Duration**
   - Grouped the movies by `duration` and identified the most common movie length during the 1990s.

3. **Count Short Action Movies**
   - Filtered the 1990s movies to include only those in the "Action" genre.
   - Counted the number of short action movies (duration <= 90 minutes).

## Results

1. The most frequent movie duration in the 1990s is **94 minutes**.
2. The number of short action movies (duration <= 90 minutes) from the 1990s is **7**.

## How to Use the Code

### Prerequisites
1. Ensure you have Python installed (version 3.7 or later).
2. Install the required library `pandas` if not already installed. You can do this using:
   ```bash
   pip install pandas
   ```
### Steps
1. Place the `netflix_data.csv` file in the same directory as the Python script.
2. Copy and paste the provided Python code into a `.py` file (e.g., `netflix_analysis.py`).
3. Run the script using the command:
   ```bash
   python netflix_analysis.py
   ```
4. The output will display the most frequent movie duration in the 1990s and the count of short action movies from that decade.

## Insights and Next Steps

- The data reveals that movies in the 1990s tended to have a typical duration of around 94 minutes.
- Short action movies were relatively uncommon, with only 7 identified in the dataset.

### Further Exploration
- Analyze other genres for trends in durations or popularity during the 1990s.
- Compare the findings for 1990s movies with those from other decades to observe changes in trends over time.
- Investigate regional differences in movie characteristics by analyzing the `country` column.


