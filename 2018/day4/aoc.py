from datetime import datetime, timedelta


def parse_log(log):
    date, event = log.replace('[', '').strip().split(']')

    date = datetime.strptime(date, "%Y-%m-%d %H:%M")

    if event.count("wakes") > 0:
        event = 'W'
    elif event.count("falls") > 0:
        event = 'F'
    else:
        event = event.split()[1]

    return [date, event]


def guard_report():
    LOG_LIST = [parse_log(log) for log in sorted(open("input.txt", 'r'))]
    date_sleep = None
    guard_report = dict()
    current_guard = None
    for date, event in LOG_LIST:
        if event == 'F':
            date_sleep = date
        elif event == 'W':
            guard_report[current_guard].extend(list(range(date_sleep.minute, date.minute)))
        else:
            current_guard = event
            if event not in guard_report:
                guard_report[current_guard] = list()
    return guard_report

def part_one(guard_report):
    _max = 0
    final_guard = ''
    for guard, sleep_time in guard_report.items():
        if _max < len(sleep_time):
            _max = len(sleep_time)
            final_guard = guard

    most_common_minute = 0
    _max = 0
    for minute in {minute for minute in guard_report[final_guard]}:
        count = guard_report[final_guard].count(minute)
        if _max < count:
            _max = count
            most_common_minute = minute

    print("1: " + str(most_common_minute * int(final_guard[1:])))

def part_two(guard_report):
    _max = 0
    final_guard = ''
    most_common_minute = 0
    for guard, sleep_time in guard_report.items():
        for minute in {minute for minute in sleep_time}:
            count = sleep_time.count(minute)
            if _max < count:
                _max = count
                most_common_minute = minute
                final_guard = guard

    print("2: " + str(int(final_guard[1:]) * most_common_minute))


if __name__ == '__main__':
    guard_report = guard_report()
    part_one(guard_report) 
    part_two(guard_report) 
