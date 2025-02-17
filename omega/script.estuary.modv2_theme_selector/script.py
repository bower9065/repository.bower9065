import xbmc
import urllib.parse
import sys
from datetime import date, datetime, timedelta

#if triggered by outside command
try:
        params = urllib.parse.parse_qs('&'.join(sys.argv[1:]))
        command = params.get('command',None)
        type = params.get('type',None)
except:
        command = None    
#Switch Holidays
if command and type[0] == 'Holiday':
    #Turn off all themes
    xbmc.executebuiltin('Skin.SetBool(ValentinesDay,False)')
    xbmc.executebuiltin('Skin.SetBool(StPatricksDay,False)')
    xbmc.executebuiltin('Skin.SetBool(Easter,False)')
    xbmc.executebuiltin('Skin.SetBool(4thOfJuly,False)')
    xbmc.executebuiltin('Skin.SetBool(Halloween,False)')
    xbmc.executebuiltin('Skin.SetBool(Thanksgiving,False)')
    xbmc.executebuiltin('Skin.SetBool(Christmas,False)')
    xbmc.executebuiltin('Skin.SetBool(NewYearsEve,False)')
    xbmc.executebuiltin('Skin.SetBool(Spring,False)')  
    xbmc.executebuiltin('Skin.SetBool(Summer,False)')
    xbmc.executebuiltin('Skin.SetBool(Autumn,False)')
    xbmc.executebuiltin('Skin.SetBool(Winter,False)')
    xbmc.executebuiltin('Skin.SetBool(Beach,False)')  
    xbmc.executebuiltin('Skin.SetBool(SkinDefault,False)')     
    command = command[0]
    xbmc.executebuiltin('Skin.SetBool(' + command + ',True)')
    xbmc.log('----(Theme Selector)...Changing theme to 'f'{command}', xbmc.LOGINFO)
#Toggle Themes    
if command and type[0] == 'Themes_on':
    command = command[0]
    xbmc.executebuiltin('Skin.SetBool(holidaythemes,' + command + ')')
    xbmc.log('----(Theme Selector)...Themes on = 'f'{command}', xbmc.LOGINFO)
#Toggle Snow Effect
if command and type[0] == 'Snow_Effect_on':
    command = command[0]
    xbmc.executebuiltin('Skin.SetBool(enablesnoweffect,' + command + ')')
    xbmc.log('----(Theme Selector)...Snow Effect on = 'f'{command}', xbmc.LOGINFO)
#Toggle Character Art
if command and type[0] == 'Character_on':
    command = command[0]
    xbmc.executebuiltin('Skin.SetBool(enablecharacter,' + command + ')')
    xbmc.log('----(Theme Selector)...Characters on = 'f'{command}', xbmc.LOGINFO)
#Toggle String Lights
if command and type[0] == 'String_Lights_on':
    command = command[0]
    xbmc.executebuiltin('Skin.SetBool(enablestringlights,' + command + ')')
    xbmc.log('----(Theme Selector)...String Lights on = 'f'{command}', xbmc.LOGINFO)
    
#if triggered by auto change holidays
if  command == None:
    #Turn off all themes
    xbmc.executebuiltin('Skin.SetBool(ValentinesDay,False)')
    xbmc.executebuiltin('Skin.SetBool(StPatricksDay,False)')
    xbmc.executebuiltin('Skin.SetBool(Easter,False)')
    xbmc.executebuiltin('Skin.SetBool(4thOfJuly,False)')
    xbmc.executebuiltin('Skin.SetBool(Halloween,False)')
    xbmc.executebuiltin('Skin.SetBool(Thanksgiving,False)')
    xbmc.executebuiltin('Skin.SetBool(Christmas,False)')
    xbmc.executebuiltin('Skin.SetBool(NewYearsEve,False)')
    xbmc.executebuiltin('Skin.SetBool(Spring,False)')  
    xbmc.executebuiltin('Skin.SetBool(Summer,False)')
    xbmc.executebuiltin('Skin.SetBool(Autumn,False)')
    xbmc.executebuiltin('Skin.SetBool(Winter,False)')
    xbmc.executebuiltin('Skin.SetBool(Beach,False)')  
    xbmc.executebuiltin('Skin.SetBool(SkinDefault,False)')     
    #Get Holiday dates
    current_year = datetime.now().year
    next_year = current_year + 1
    now = date.today()

    #Days till Easter
    a = current_year % 19
    b = current_year // 100
    c = current_year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month = (h + l - 7 * m + 114) // 31
    day = ((h + l - 7 * m + 114) % 31) + 1
    date_string = str(current_year) + "-" + str(month) + "-" + str(day)  # Result: "2025-02-16"
    date_object = datetime.strptime(date_string, "%Y-%m-%d")
    easter = date_object.date() - now
    easter = easter.days
    if easter < 0:
        a = next_year % 19
        b = next_year // 100
        c = next_year % 100
        d = b // 4
        e = b % 4
        f = (b + 8) // 25
        g = (b - f + 1) // 3
        h = (19 * a + b - d - g + 15) % 30
        i = c // 4
        k = c % 4
        l = (32 + 2 * e + 2 * i - h - k) % 7
        m = (a + 11 * h + 22 * l) // 451
        month = (h + l - 7 * m + 114) // 31
        day = ((h + l - 7 * m + 114) % 31) + 1
        date_string = str(next_year) + "-" + str(month) + "-" + str(day)  # Result: "2025-02-16"
        date_object = datetime.strptime(date_string, "%Y-%m-%d")
        easter = date_object.date() - now
        easter = easter.days

    #Days till Election Day
    first_day = date(current_year, 11, 1)
    day_of_week = first_day.weekday()
    first_monday_date = first_day + timedelta(days=(7 - day_of_week) % 7)
    tuesday_date = first_monday_date + timedelta(days=1)
    election_day = tuesday_date - now
    election_day = election_day.days
    if election_day < 0:
        first_day = date(next_year, 11, 1)
        day_of_week = first_day.weekday()
        first_monday_date = first_day + timedelta(days=(7 - day_of_week) % 7)
        tuesday_date = first_monday_date + timedelta(days=1)
        election_day = tuesday_date - now
        election_day = election_day.days

    #Days till Thanksgiving
    first_day = date(current_year, 11, 1)
    day_of_week = first_day.weekday() 
    fourth_thursday_date = first_day + timedelta(days=((3 - day_of_week) % 7) + 21)
    thanksgiving = fourth_thursday_date - now
    thanksgiving = thanksgiving.days
    if thanksgiving < 0:
        first_day = date(next_year, 11, 1)
        day_of_week = first_day.weekday()
        fourth_thursday_date = first_day + timedelta(days=((3 - day_of_week) % 7) + 21)
        thanksgiving = fourth_thursday_date - now
        thanksgiving = thanksgiving.days

    #Days till Valentine's Day
    datetime_string = "{}-02-14"
    datetime_object = datetime.strptime(datetime_string.format(current_year), "%Y-%m-%d")
    valentines_day = datetime_object.date() - now
    valentines_day = valentines_day.days
    if valentines_day < 0:
        datetime_object = datetime.strptime(datetime_string.format(next_year), "%Y-%m-%d")
        valentines_day = datetime_object.date() - now
        valentines_day = valentines_day.days

    #Days till St. Patricks Day
    datetime_string = "{}-03-17"
    datetime_object = datetime.strptime(datetime_string.format(current_year), "%Y-%m-%d")
    st_papatricks_day = datetime_object.date() - now
    st_papatricks_day = st_papatricks_day.days
    if st_papatricks_day < 0:
        datetime_object = datetime.strptime(datetime_string.format(next_year), "%Y-%m-%d")
        st_papatricks_day = datetime_object.date() - now
        st_papatricks_day = st_papatricks_day.days

    #Days till 4th of July
    datetime_string = "{}-07-4"
    datetime_object = datetime.strptime(datetime_string.format(current_year), "%Y-%m-%d")
    independence_day = datetime_object.date() - now
    independence_day = independence_day.days
    if independence_day < 0:
        datetime_object = datetime.strptime(datetime_string.format(next_year), "%Y-%m-%d")
        independence_day = datetime_object.date() - now
        independence_day = independence_day.days

    #Days till Halloween
    datetime_string = "{}-10-31"
    datetime_object = datetime.strptime(datetime_string.format(current_year), "%Y-%m-%d")
    halloween = datetime_object.date() - now
    halloween = halloween.days
    if halloween < 0:
        datetime_object = datetime.strptime(datetime_string.format(next_year), "%Y-%m-%d")
        halloween = datetime_object.date() - now
        halloween = halloween.days

    #Days till Christmas
    datetime_string = "{}-12-25"
    datetime_object = datetime.strptime(datetime_string.format(current_year), "%Y-%m-%d")
    christmas = datetime_object.date() - now
    christmas = christmas.days
    if christmas < 0:
        datetime_object = datetime.strptime(datetime_string.format(next_year), "%Y-%m-%d")
        christmas = datetime_object.date() - now
        christmas = christmas.days

    #Days till New Year's Eve
    datetime_string = "{}-12-31"
    datetime_object = datetime.strptime(datetime_string.format(current_year), "%Y-%m-%d")
    new_years_eve = datetime_object.date() - now
    new_years_eve = new_years_eve.days
    if new_years_eve < 0:
        datetime_object = datetime.strptime(datetime_string.format(next_year), "%Y-%m-%d")
        new_years_eve = datetime_object.date() - now
        new_years_eve = new_years_eve.days

    if valentines_day < 10:
        xbmc.executebuiltin('Skin.SetBool(ValentinesDay,True)')
        xbmc.log('----(Theme Selector)...Changing theme to ValentinesDay', xbmc.LOGINFO)
    elif st_papatricks_day < 10:
        xbmc.executebuiltin('Skin.SetBool(StPatricksDay,True)')
        xbmc.log('----(Theme Selector)...Changing theme to StPatricksDay', xbmc.LOGINFO)
    elif easter < 14:
        xbmc.executebuiltin('Skin.SetBool(Easter,True)')
        xbmc.log('----(Theme Selector)...Changing theme to Easter', xbmc.LOGINFO)
    elif independence_day < 10:
        xbmc.executebuiltin('Skin.SetBool(4thOfJuly,True)')
        xbmc.log('----(Theme Selector)...Changing theme to 4thOfJuly', xbmc.LOGINFO)
    elif halloween < 31:
        xbmc.executebuiltin('Skin.SetBool(Halloween,True)')
        xbmc.log('----(Theme Selector)...Changing theme to Halloween', xbmc.LOGINFO)
    elif election_day == 0:
        xbmc.executebuiltin('Skin.SetBool(4thOfJuly,True)')
        xbmc.log('----(Theme Selector)...Changing theme to 4thOfJuly', xbmc.LOGINFO)
    elif thanksgiving < 31:
        xbmc.executebuiltin('Skin.SetBool(Thanksgiving,True)')
        xbmc.log('----(Theme Selector)...Changing theme to Thanksgiving', xbmc.LOGINFO)
    elif christmas < 31:
        xbmc.executebuiltin('Skin.SetBool(Christmas,True)')
        xbmc.log('----(Theme Selector)...Changing theme to Christmas', xbmc.LOGINFO)
    elif new_years_eve < 7:
        xbmc.executebuiltin('Skin.SetBool(NewYearsEve,True)')
        xbmc.log('----(Theme Selector)...Changing theme to NewYearsEve', xbmc.LOGINFO)
    else:
        #Spring
        start_date = date(current_year, 3, 19)
        end_date = date(current_year, 6, 20)
        if start_date <= now <= end_date:
            xbmc.executebuiltin('Skin.SetBool(Spring,True)')
            xbmc.log('----(Theme Selector)...Changing theme to Spring', xbmc.LOGINFO)
        #Summer
        start_date = date(current_year, 6, 21)
        end_date = date(current_year, 8, 31)
        if start_date <= now <= end_date:
            xbmc.executebuiltin('Skin.SetBool(Summer,True)')
            xbmc.log('----(Theme Selector)...Changing theme to Summer', xbmc.LOGINFO)
        #Autumn
        start_date = date(current_year, 9, 1)
        end_date = date(current_year, 12, 20)
        if start_date <= now <= end_date:
            xbmc.executebuiltin('Skin.SetBool(Autumn,True)')
            xbmc.log('----(Theme Selector)...Changing theme to Autumn', xbmc.LOGINFO)
        #Winter
        start_date = date(current_year, 12, 21)
        end_date = date(current_year, 12, 31)
        if start_date <= now <= end_date:
            xbmc.executebuiltin('Skin.SetBool(Winter,True)')
            xbmc.log('----(Theme Selector)...Changing theme to Winter', xbmc.LOGINFO)
        #Winter
        start_date = date(current_year, 1, 1)
        end_date = date(current_year, 3, 18)
        if start_date <= now <= end_date:
            xbmc.executebuiltin('Skin.SetBool(Winter,True)')
            xbmc.log('----(Theme Selector)...Changing theme to Winter', xbmc.LOGINFO)        
    