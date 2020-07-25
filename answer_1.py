import datetime

def difference_in_months(start, end):
    if start.year == end.year:
        months = end.month - start.month
    else:
        months = (12 - start.month) + (end.month)
    if start.day > end.day:
        months = months - 1
    return months

def server_cost(d1, m1, y1, d2, m2, y2):
    created_on = datetime.date(y1, m1, d1)
    deleted_on = datetime.date(y2, m2, d2)
    diff_in_days = (deleted_on - created_on).days
    diff_in_months = difference_in_months(created_on, deleted_on)

    if diff_in_days == 0:
        return 20
    elif diff_in_days <= 30: # assuming 1 month = 30 days
        return 30 * diff_in_days
    elif diff_in_days <= 365:
        return 1000 * diff_in_months
    else:
        return 20000

if __name__ == '__main__':
    print(server_cost(6, 6, 2020, 6, 6, 2020))
    
    print(server_cost(6, 6, 2020, 9, 6, 2020))

    print(server_cost(6, 6, 2020, 9, 12, 2020))

    print(server_cost(6, 6, 2020, 9, 6, 2021))
