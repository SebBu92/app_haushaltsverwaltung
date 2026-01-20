class CheckDate:
    @staticmethod
    def is_valid_date(date):
        if len(date) != 10:
            return False

        if date[4] != "-" or date[7] != "-":
            return False

        try:
            year = int(date[0:4])
            month = int(date[5:7])
            day = int(date[8:10])
        except ValueError:
            return False

        if not (1 <= month <= 12):
            return False

        if not (1 <= day <= 31):
            return False

        return True