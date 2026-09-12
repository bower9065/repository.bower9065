import xbmc
import urllib.parse
import sys
from datetime import date, datetime, timedelta

ALL_THEMES = ['ValentinesDay', 'StPatricksDay', 'Easter', '4thOfJuly', 'Halloween',
              'Thanksgiving', 'Christmas', 'NewYearsEve', 'Spring', 'Summer',
              'Autumn', 'Winter', 'Beach', 'SkinDefault']


def set_theme(winning_theme):
    """Turn off all themes, then turn on the winner. Only called once we know
    the full operation can complete, so we never leave everything blanked out."""
    for theme in ALL_THEMES:
        xbmc.executebuiltin(f'Skin.SetBool({theme},False)')
    if winning_theme:
        xbmc.executebuiltin(f'Skin.SetBool({winning_theme},True)')
        xbmc.log(f'----(Theme Selector)...Changing theme to {winning_theme}', xbmc.LOGINFO)


def get_easter_days(year, now):
    a = year % 19
    b = year // 100
    c = year % 100
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
    return (date(year, month, day) - now).days


def get_election_days(year, now):
    first_day = date(year, 11, 1)
    day_of_week = first_day.weekday()
    first_monday_date = first_day + timedelta(days=(7 - day_of_week) % 7)
    tuesday_date = first_monday_date + timedelta(days=1)
    return (tuesday_date - now).days


def get_thanksgiving_days(year, now):
    first_day = date(year, 11, 1)
    day_of_week = first_day.weekday()
    fourth_thursday_date = first_day + timedelta(days=((3 - day_of_week) % 7) + 21)
    return (fourth_thursday_date - now).days


def get_days_until(year, month, day, now):
    return (date(year, month, day) - now).days


def run_auto_theme():
    """Compute which theme should be active. Raises on any failure — caller
    decides what to do if this can't complete (e.g. mid profile-switch)."""
    current_year = datetime.now().year
    next_year = current_year + 1
    now = date.today()

    easter = get_easter_days(current_year, now)
    if easter < 0:
        easter = get_easter_days(next_year, now)

    election_day = get_election_days(current_year, now)
    if election_day < 0:
        election_day = get_election_days(next_year, now)

    thanksgiving = get_thanksgiving_days(current_year, now)
    if thanksgiving < 0:
        thanksgiving = get_thanksgiving_days(next_year, now)

    valentines_day = get_days_until(current_year, 2, 14, now)
    if valentines_day < 0:
        valentines_day = get_days_until(next_year, 2, 14, now)

    st_papatricks_day = get_days_until(current_year, 3, 17, now)
    if st_papatricks_day < 0:
        st_papatricks_day = get_days_until(next_year, 3, 17, now)

    independence_day = get_days_until(current_year, 7, 4, now)
    if independence_day < 0:
        independence_day = get_days_until(next_year, 7, 4, now)

    halloween = get_days_until(current_year, 10, 31, now)
    if halloween < 0:
        halloween = get_days_until(next_year, 10, 31, now)

    christmas = get_days_until(current_year, 12, 25, now)
    if christmas < 0:
        christmas = get_days_until(next_year, 12, 25, now)

    new_years_eve = get_days_until(current_year, 12, 31, now)
    if new_years_eve < 0:
        new_years_eve = get_days_until(next_year, 12, 31, now)

    # Decide the winner first — nothing gets turned off until we know this.
    winning_theme = None
    if 0 <= valentines_day < 10:
        winning_theme = 'ValentinesDay'
    elif 0 <= st_papatricks_day < 10:
        winning_theme = 'StPatricksDay'
    elif 0 <= easter < 14:
        winning_theme = 'Easter'
    elif 0 <= independence_day < 10:
        winning_theme = '4thOfJuly'
    elif election_day == 0:
        winning_theme = '4thOfJuly'
    elif 0 <= halloween < 31:
        winning_theme = 'Halloween'
    elif 0 <= thanksgiving < 31:
        winning_theme = 'Thanksgiving'
    elif 0 <= christmas < 31:
        winning_theme = 'Christmas'
    elif 0 <= new_years_eve < 7:
        winning_theme = 'NewYearsEve'
    else:
        if date(current_year, 3, 19) <= now <= date(current_year, 6, 20):
            winning_theme = 'Spring'
        elif date(current_year, 6, 21) <= now <= date(current_year, 8, 31):
            winning_theme = 'Summer'
        elif date(current_year, 9, 1) <= now <= date(current_year, 12, 20):
            winning_theme = 'Autumn'
        else:
            winning_theme = 'Winter'

    return winning_theme


def main():
    try:
        params = urllib.parse.parse_qs('&'.join(sys.argv[1:]))
        command = params.get('command', None)
        type_param = params.get('type', None)
    except Exception:
        command = None
        type_param = None

    if command and type_param:
        kind = type_param[0]

        if kind == 'Holiday':
            command_val = command[0]
            set_theme(command_val)
            return

        if kind == 'Themes_on':
            command_val = command[0]
            xbmc.executebuiltin(f'Skin.SetBool(holidaythemes,{command_val})')
            xbmc.log(f'----(Theme Selector)...Themes on = {command_val}', xbmc.LOGINFO)
            return

        if kind == 'Snow_Effect_on':
            command_val = command[0]
            xbmc.executebuiltin(f'Skin.SetBool(enablesnoweffect,{command_val})')
            xbmc.log(f'----(Theme Selector)...Snow Effect on = {command_val}', xbmc.LOGINFO)
            return

        if kind == 'Character_on':
            command_val = command[0]
            xbmc.executebuiltin(f'Skin.SetBool(enablecharacter,{command_val})')
            xbmc.log(f'----(Theme Selector)...Characters on = {command_val}', xbmc.LOGINFO)
            return

        if kind == 'String_Lights_on':
            command_val = command[0]
            xbmc.executebuiltin(f'Skin.SetBool(enablestringlights,{command_val})')
            xbmc.log(f'----(Theme Selector)...String Lights on = {command_val}', xbmc.LOGINFO)
            return

    # Auto-run: triggered by skin onload with no command, e.g. on profile
    # switch. Compute the winning theme BEFORE touching any Skin.SetBool
    # calls, so if this gets interrupted (e.g. interpreter torn down mid
    # profile switch) we never leave the skin with every theme blanked out —
    # whatever theme was already active just stays put until the next
    # successful run.
    if command is None:
        winning_theme = run_auto_theme()
        set_theme(winning_theme)


try:
    main()
except Exception as e:
    try:
        xbmc.log(f'----(Theme Selector) aborted, likely mid profile-switch: {e}', xbmc.LOGWARNING)
    except Exception:
        pass