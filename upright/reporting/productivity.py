class Productivity:

    def __init__(self, client, time_start, time_end):
        self.client = client
        self.time_start = time_start
        self.time_end = time_end

    def operational(self, interval, user_id=None):
        """
        Returns operational productivity stats recorded in the timeframe grouped by interval

        **Params**
            `time_start`: String
            `time_end`: String

            `interval`: String - hour, day, week, month, quarter, year; What timeframe to group stats by.

            `user_id`: Integer (optional) - Filter data by a particular user; defaults to all.
        """
        params = {
            'time_start' : self.time_start,
            'time_end' : self.time_end,
            'interval' : interval,
            'user_id' : user_id,
        }
        return self.client.get("reports/productivity/operational", params=params)
    

    def user(self, hide_inactive_users=False):
        """
        Returns user productivity stats recorded in the timeframe
        """
        params = {
            'time_start' : self.time_start,
            'time_end' : self.time_end,
            'hide_inactive_users' : hide_inactive_users,
        }
        return self.client.get("reports/productivity/user", params=params)