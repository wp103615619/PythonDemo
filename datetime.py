class BuildData:
    def __init__(self):
        self.date_list = self.create_dates()
        return
    '''get dates between two date'''
    def get_dates(self, start, end):
        date_start = datetime.datetime.strptime(start, '%Y-%m-%d')
        date_end = datetime.datetime.strptime(end, '%Y-%m-%d')
        date_list = []
        while date_start < date_end:
            date_start += datetime.timedelta(days=1)
            qu = date_start.strftime('%Y-%m-%d')
            date_list.append(qu)
        return date_list

    def create_dates(self):
        date_list = self.get_dates('1957-02-28', '2002-12-31')
        return date_list
