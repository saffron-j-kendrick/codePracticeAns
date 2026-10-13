import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    new_pd = pd.merge(person, address, how='left', on='personId')
    new_pd.drop(columns=["personId", "addressId"], inplace=True)
    return new_pd



person = pd.DataFrame({
    "firstName": ["Allen", "Bob"],
    "lastName": ["Wang", "Alice"],
    "personId": [1, 2]})

address = pd.DataFrame({
    "addressId": [1, 2],
    "personId": [2, 3],
    "city": ["New York City", "Leetcode"],
    "state": ["New York", "California"]})

if __name__ == "__main__":
    print(combine_two_tables(person, address))