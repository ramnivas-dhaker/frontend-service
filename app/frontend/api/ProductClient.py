import requests

# host_url = 'http://0.0.0.0:5558'
host_url = 'http://product:5558'

class ProductClient:

    @staticmethod
    def get_product(slug):
        response = requests.request(method="GET", url=f'{host_url}/api/product/' + slug)
        print("--------------product----------------",response )

        product = response.json()
        return product

    @staticmethod
    def get_products():
        r = requests.get(f'{host_url}/api/products')
        products = r.json()
        print("--------------products----------------",products )

        return products
