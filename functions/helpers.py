
def pause_for(secs, msg=None):
    """
        Pauses the execution of the script for X number of seconds
    """
    import time

    if msg is not None:
        print(msg + " for %s secs.\n" % secs)
    else:
        print("Wait %s secs...." % secs)
    time.sleep(float(secs * 1000) / 1000)

def get_date(date_format, days_add_remove=0):
    """
    date_format = 1 prints: "MM/DD/YYYY"
    date_format = 2 prints: "Jul 31, 2014" or "Aug 01, 2014"
    date_format = 3 prints: "July 31, 2014"
    date_format = 4 prints: "Thursday Jul" (This is using in course card, date of course discount)
    date_format = 5 prints: "07-31-2014"
    date_format = 6 prints: "Jul 31, 2014" or "Aug 1, 2014"
    date_format = 7 prints: "July 31, 2014" or "August 1, 2014"
    date_format = 8 prints: "12/08/2014"
    date_format = 9 prints: "2014-08-12"
    date_format = 10 prints: "25-Jun-17"
    date format = 11 prints "7 July 2017"
    date_format = 14 prints "2018/03/06
    date_format = 15 prints "2018/03/6
    date_format = 16 prints "January"
    date_format = 17 prints: "July 31, 2014" or "August  1, 2014"    (2 spaces in single digit dates)
    """
    import datetime
    date_now = datetime.date.today() + datetime.timedelta(days=int(days_add_remove))

    if date_format == 1:
        return date_now.strftime("%m/%d/%Y")

    elif date_format == 2:
        return date_now.strftime("%b %d, %Y")

    elif date_format == 3:
        return date_now.strftime("%B %d, %Y")

    elif date_format == 4:
        return date_now.strftime("%A %b")

    elif date_format == 5:
        return date_now.strftime("%m-%d-%Y")

    elif date_format == 6:
        day = date_now.strftime("%d")
        return date_now.strftime("%b " + str(int(day)) + ", %Y")

    elif date_format == 7:
        day = date_now.strftime("%d")
        return date_now.strftime("%B " + str(int(day)) + ", %Y")

    elif date_format == 8:
        return date_now.strftime("%d/%m/%Y")  # 17/09/2014

    elif date_format == 9:
        return date_now.strftime("%Y-%m-%d")

    elif date_format == 10:
        return date_now.strftime("%d-%b-%y")

    elif date_format == 11:
        day = date_now.strftime("%d")
        return date_now.strftime(str(int(day)) + " %B %Y")

    elif date_format == 12:
        year = int(date_now.strftime("%Y"))
        month = int(date_now.strftime("%m"))
        day = int(date_now.strftime("%d"))

        return year, month, day
    elif date_format == 13:
        return date_now.strftime("%H:%M:%S")
    elif date_format == 14:
        return date_now.strftime("%Y/%m/%d")  # 17/09/2014
    elif date_format == 15:
        day = date_now.strftime("%d")
        return date_now.strftime("%Y/%m/" + str(int(day)))  # 17/09/2014
    elif date_format == 16:
        month = date_now.strftime("%B")
        return month
    elif date_format == 17:
        day = date_now.strftime("%d")
        if int(day) < 10:
            return date_now.strftime("%B  " + str(int(day)) + ", %Y")
        else:
            return date_now.strftime("%B " + str(int(day)) + ", %Y")
    else:
        return date_now

def login_in_with_role(role):
    pass