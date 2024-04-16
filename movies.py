"""Identify the most popular movie ratings based on data in two CSV files."""

from argparse import ArgumentParser
import pandas as pd
import sys


# Replace this comment with your implementation of best_movies().
def best_movies(movies_file, ratings_file):
    
    movies_df = pd.read_csv(movies_file)
    ratings_df = pd.read_csv(ratings_file)

    merged_df  = pd.merge(movies_df, ratings_df, left_on='movie id', right_on='item id', how='inner') 

    average_ratings = merged_df.groupby('movie title')['rating'].mean()
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
