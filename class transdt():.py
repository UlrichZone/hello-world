class transdt():
    def transtime(self, datetime):
        if datetime:
            if datetime == 'None':
                return None
            for fmt in ["%Y-%m-%d %H:%M:%S", "%Y-%m-%d",]:
                try:
                    if fmt == "%Y-%m-%d %H:%M:%S":
                        datetime = datetime.datetime.strptime(datetime, format)
                    if fmt == "%Y-%m-%d":
                        datetime = datetime.datetime.strptime(str(datetime), fmt).date()
                    if td:
                        datetime = datetime + td
                except ValueError:
                    continue
        return x
        self.__name = datetime

    def trans_datetime(x, format, td=datetime.timedelta(hours=8)):
    if x:
        if x == 'None':
            return None
        for fmt in ["%Y-%m-%d %H:%M:%S", "%Y-%m-%d"]:
            try:
                if fmt == "%Y-%m-%d %H:%M:%S":
                    x = datetime.datetime.strptime(x, format)
                if fmt == "%Y-%m-%d":
                    x = datetime.datetime.strptime(str(x), fmt).date()
                if td:
                    x = x + td
            except ValueError:
                continue
    return x