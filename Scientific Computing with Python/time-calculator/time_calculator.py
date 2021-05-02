def add_time(start, duration, *args):
    
    # convert input time into minutes
    new_time = start[:-3].split(':')
    if start[-2:] == "AM":
        new_time = int(new_time[0]) % 12 * 60 + int(new_time[1])
    elif start[-2:] == "PM":
        new_time = (int(new_time[0]) % 12 + 12) * 60 + int(new_time[1])

    # add duration in minutes
    add = duration.split(':')
    add = int(add[0]) * 60 + int(add[1])
    new_time += add

    # compute the new day, hour, min
    new_day = new_time // 1400
    new_hour = (new_time - new_day * 1440) // 60
    new_min = new_time % 60

    # format new_time for output
    new_min = ['0' + str(new_min) if new_min < 10 else str(new_min)][0]

    if new_hour == 0:
        new_time = str(12) + ':' + new_min + ' AM'
    elif new_hour < 12:
        new_time = str(new_hour) + ':' + new_min + ' AM'
    elif new_hour == 12:
        new_time = str(new_hour) + ':' + new_min + ' PM'
    else:
        new_time = str(new_hour-12) + ':' + new_min + ' PM'

    # add day in week if opt arg is provided
    if len(args) > 0:
        week = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday', 0: 'Sunday'}

        outday_key = [k for k, v in week.items() if v == args[0].capitalize()][0] + new_day
        new_time += ', ' + week[outday_key % 7]

    # add day elapsed if needed
    if new_day == 1:
        new_time += ' (next day)'
    elif new_day > 1:
        new_time += ' (' + str(new_day) + ' days later)'

    return new_time