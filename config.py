FILE_PATH = "AB_NYC_2019.csv"
COLUMN_NAMES_BY_CATEGORY = {
            'name': 'name', 
            'host': ('host_id', 'host_name'), 
            'neighbourhood': ('neighbourhood_group', 'neighbourhood'), 
            'coordinates': ('latitude', 'longitude'), 
            'room type': 'room_type', 
            'price': 'price',
            'minimum nights': 'minimum_nights', 
            'reviews': ('number_of_reviews', 'last_review', 'reviews_per_month'), 
            'calculated host listing count': 'calculated_host_listings_count', 
            'availability': 'availability_365'
            }

COLUMNS_IN_SHOW = ['id', 'name', 'host_name', 'neighbourhood', 'price']

COLUMNS_IN_SEARCH = ['id', 'name', 'neighbourhood', 'room_type', 'price', 'minimum_nights', 'availability_365']
COLUMNS_IN_SEARCH_MINIMAL = ['id', 'name', 'neighbourhood']