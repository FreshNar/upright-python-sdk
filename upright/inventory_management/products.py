class Product:

    def __init__(self, client):
        self.client = client

    def list_products(self, tags, query):
        """
        Returns a list of products
        """
        params = {
            'tags' : tags,
            'query' : query
        }
        return self.client.get("v5/products", params=params)