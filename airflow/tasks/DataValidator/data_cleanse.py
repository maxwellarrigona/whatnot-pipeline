import pandas as pd

def data_cleaning(storage_url:str, container_name:str, data_level:str, filename:str):

    df = pd.read_csv(f'{storage_url}{container_name}/{data_level}/{filename}',encoding="utf-8")

    df["colorsNumber"] = df["colorsNumber"].str.replace(" colors","")
    df["colorsNumber"] = df["colorsNumber"].str.replace(" Color","")

    df["modelName"] = df["modelName"].fillna("No Data")
    df["lensColor"] = df["lensColor"].fillna("No Data")
    df["localizedColorLabel"] = df["localizedColorLabel"].fillna("No Data")

    df["listPrice"] = df["listPrice"].replace({'\$':''}, regex = True).str.replace(",","").astype(float)
    df["offerPrice"] = df["offerPrice"].replace({'\$':''}, regex = True).str.replace(",","").astype(float)

    df.drop(['name'], axis=1, inplace=True)

    df.columns = df.columns.str.lower()

    print("Data cleanse succesful")

    return df.to_dict("records")
