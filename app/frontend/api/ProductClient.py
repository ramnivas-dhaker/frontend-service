import requests

host_url = 'http://product:5558'
# host_url = 'http://172.17.0.1:5558'
# host_url = 'http://frontend-service_order-network:5558'

class ProductClient:

    @staticmethod
    def get_product(slug):
        response = requests.request(method="GET", url=f'{host_url}/api/product/' + slug)

        product = response.json()
        return product

    @staticmethod
    def get_products():
        print("------", f"{host_url}/api/products")
        r = requests.get(f'{host_url}/api/products')
        products = r.json()
        print("**************", products)

        return products
