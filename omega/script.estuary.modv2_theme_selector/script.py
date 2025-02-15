import xbmc
import urllib.parse

try:
        params = urllib.parse.parse_qs('&'.join(sys.argv[1:]))
        command = params.get('command',None)
        type = params.get('type',None)
except:
        command = None    
#Holidays
if command and type[0] == 'Holiday':
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
#Toggle Themes    
if command and type[0] == 'Themes_on':
    command = command[0]
    xbmc.executebuiltin('Skin.SetBool(holidaythemes,' + command + ')')
#Toggle Snow Effect
if command and type[0] == 'Snow_Effect_on':
    command = command[0]
    xbmc.executebuiltin('Skin.SetBool(enablesnoweffect,' + command + ')')
#Toggle Character Art
if command and type[0] == 'Character_on':
    command = command[0]
    xbmc.executebuiltin('Skin.SetBool(enablecharacter,' + command + ')')
#Toggle String Lights
if command and type[0] == 'String_Lights_on':
    command = command[0]
    xbmc.executebuiltin('Skin.SetBool(enablestringlights,' + command + ')')
