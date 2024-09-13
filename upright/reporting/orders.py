class Order:

    def __init__(self, client, time_start, time_end):
        self.client = client
        self.time_start = time_start
        self.time_end = time_end

    def paid_orders(self, payment_status):
        """
        Returns all paid orders created within the timeframe
        """
        params = {
            'time_start' : self.time_start,
            'time_end' : self.time_end,
            'payment_status' : payment_status
        }
        return self.client.get("reports/paid_orders", params=params)
    
    def order_items(self):
        """
        Returns all ordered items paid within a timeframe
        """
        params = {
            'time_start' : self.time_start,
            'time_end' : self.time_end
        }
        return self.client.get("reports/order_items", params=params)
