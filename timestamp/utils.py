def human_time(time_passed):
    seconds = time_passed.total_seconds()
    hours = int(seconds // 3600)
    seconds = seconds - (hours * 3600)
    minutes = int(seconds // 60)
    seconds = int(seconds - (minutes * 60))
    return ('{}h {}m {}s'.format(hours, minutes, seconds))