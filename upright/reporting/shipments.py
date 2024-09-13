class Shipment:

    def __init__(self, client, time_start, time_end):
        self.client = client
        self.time_start = time_start
        self.time_end = time_end

    def shipments(self):
        """
        Returns all shipments created within the timeframe
        """
        params = {
            'time_start' : self.time_start,
            'time_end' : self.time_end
        }
        return self.client.get("reports/shipments", params=params)