from scraper_live_streams import scraper_streams
from scraper_stream_products import scraper_products
import pathlib
from dotenv import dotenv_values 

if __name__ == "__main__":

    script_path = pathlib.Path(__file__).parent.parent.resolve()
    config = dotenv_values(f"{script_path}/configuration.env")
    data_level = config["raw_data_directory"]

    scraper_streams(data_level=data_level)
    scraper_products(data_level=data_level)



    

