from datetime import datetime
def delta_day(d1, d2):
    start_date = datetime.strptime(d1, "%d/%m/%Y")
    print(start_date)
    end_date = datetime.strptime(d2, "%d/%m/%Y")
    print(end_date)
    return (end_date-start_date).days
print(delta_day('30/11/2019', '31/10/2022'))