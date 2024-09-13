class Listing:

    def __init__(self, client, time_start, time_end):
        self.time_start = time_start
        self.time_end = time_end
        self.client = client

    def goodwillfinds(self):
        """
        Returns all Goodwillfinds listings created within the timeframe 
        """
        params = {
            'time_start' : self.time_start,
            'time_end' : self.time_end
        }
        return self.client.get("reports/listings/goodwillfinds", params=params)
    
    def shopgoodwill(self):
        """
        Returns all Shopgoodwill listings created within the timeframe 
        """
        params = {
            'time_start' : self.time_start,
            'time_end' : self.time_end
        }
        return self.client.get("reports/listings/shopgoodwill", params=params)

    def ebay(self):
        """
        Returns all eBay listings created within the timeframe
        """
        params = {
            'time_start' : self.time_start,
            'time_end' : self.time_end
        }
        return self.client.get("reports/listings/ebay", params=params)
    
    def shopify(self):
        """
        Returns all Shopify listings created within the timeframe
        """
        params = {
            'time_start' : self.time_start,
            'time_end' : self.time_end
        }
        return self.client.get("reports/listings/shopify", params=params)