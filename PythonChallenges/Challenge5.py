#Write a function that converts hours into seconds.

def HoursToSeconds(Hours):
    Seconds = Hours*60*60
    return Seconds

print("Hours to seconds: " + str(HoursToSeconds(3)))