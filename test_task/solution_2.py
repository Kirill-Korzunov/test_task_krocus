import csv
import calendar


class Department:
    def __init__(self, start_year, end_year, name):
        self.start_year = start_year
        self.end_year = end_year
        self.name = name
        self.income_year_to_month = {k: {k: 0 for k in range(1, 13)} for k in range(start_year, end_year + 1)}

    def sum_income_month(self, year: int, month: int, income):
        self.income_year_to_month[year][month] = self.income_year_to_month[year].get(month) + income


with open('test_task/task_2/departments.csv', encoding='UTF-8') as f_dep,\
        open('test_task/task_2/operations.csv', encoding='UTF-8') as f_operate:
    data = {}
    for department in csv.DictReader(f_dep):
        dep = Department(
            int(department['start_year']),
            int(department['end_year']),
            department['name'],
        )
        data.update({department['id']: dep})

    for operate in csv.DictReader(f_operate):
        if operate:
            id = operate['department_id']
            month = int(operate['month'])
            year = int(operate['year'])
            day = int(operate['day'])
            income = int(operate['income'])
            if (id in data.keys()) and (0 < month < 13) and (data[id].start_year <= year <= data[id].end_year)\
                and (0 < day <= calendar.monthrange(year, month)[-1]):

                data[id].sum_income_month(year, month, income)

    start = (min(data.values(), key=lambda x: x.start_year).start_year)
    end = (max(data.values(), key=lambda x: x.end_year).end_year)
    for year in range(start, end + 1):
        for month in range(1, 13):
            for index in data:
                if data[index].income_year_to_month.get(year) is not None:
                    print(year, month, data[index].name, data[index].income_year_to_month[year][month])
