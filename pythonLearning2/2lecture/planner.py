from crontab import CronTab
import datetime

with open('dateInfo', 'a') as file:
    file.write('\n' + str(datetime.datetime.now()))

# Доступ к cron пользователя:
myCron = CronTab(user='vlad')

for job in myCron:
    print(job)


