"""Identify the most popular movie ratings based on data in two CSV files."""

from argparse import ArgumentParser
import pandas as pd
import sys


def best_movies(movies_file, ratings_file):
    """Identify the most popular movie ratings based on data in two CSV files.
    
    Args:
        movies_file (str): Path to the CSV file containing movie data.
        ratings_file (str): Path to the CSV file containing ratings.
        
    Returns:
        pandas.Series: Series containing average ratings for each movie title, sorted in descending order.
    """
    movies_dataframe = pd.read_csv(movies_file)
    ratings_dataframe = pd.read_csv(ratings_file)

    merged_dataframe = pd.merge(movies_dataframe, ratings_dataframe, left_on='movie id', right_on='item id', how='inner')

    average_ratings = merged_dataframe.groupby('movie title')['rating'].mean()
    return average_ratings.sort_values(ascending=False)


def parse_args(arglist):
    """ Parse command-line arguments.
    
    Args:
        arglist (list of str): a list of command-line arguments.
    
    Returns:
        namespace: the parsed command-line arguments as a namespace with
        variables movie_csv and rating_csv.
    """
    parser = ArgumentParser()
    parser.add_argument("movie_csv", help="CSV containing movie data")
    parser.add_argument("rating_csv", help="CSV containing ratings")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    movies = best_movies(args.movie_csv, args.rating_csv)
    print(movies.head())

