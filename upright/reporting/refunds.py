class Refund:

    def __init__(self, client, time_start, time_end):
        self.client = client
        self.time_start = time_start
        self.time_end = time_end

    def refunds(self):
        """
        Returns all refunds submitted within the timeframe
        """
        params = {
            'time_start' : self.time_start,
            'time_end' : self.time_end
        }

        return self.client.get("reports/refunds", params=params)