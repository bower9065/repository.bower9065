import xbmc
import urllib.parse
import sys
import time
import xbmcaddon
try:
        params = urllib.parse.parse_qs('&'.join(sys.argv[1:]))
        command = params.get('command',None)
except:
        command = None

if command and command[0] == 'Holiday Themes on':
    xbmc.executebuiltin('Skin.SetBool(holidaythemes,True)')
if command and command[0] == 'Holiday Themes off':
    xbmc.executebuiltin('Skin.SetBool(holidaythemes,False)')      
    
if command and command[0] == 'Snow Effect on':
    xbmc.executebuiltin('Skin.SetBool(enablesnoweffect,True)')
if command and command[0] == 'Snow Effect off':
    xbmc.executebuiltin('Skin.SetBool(enablesnoweffect,False)') 

if command and command[0] == 'Character on':
    xbmc.executebuiltin('Skin.SetBool(enablecharacter,True)')
if command and command[0] == 'Character off':
    xbmc.executebuiltin('Skin.SetBool(enablecharacter,False)') 

if command and command[0] == 'String Lights on':
    xbmc.executebuiltin('Skin.SetBool(enablestringlights,True)')
if command and command[0] == 'String Lights off':
    xbmc.executebuiltin('Skin.SetBool(enablestringlights,False)')

if command and command[0] == 'Valentines Day':
    xbmc.executebuiltin('Skin.SetBool(ValentinesDay,True)')

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
    
if command and command[0] == 'St Patricks Day':
    xbmc.executebuiltin('Skin.SetBool(StPatricksDay,True)')

    xbmc.executebuiltin('Skin.SetBool(ValentinesDay,False)')
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
  
if command and command[0] == 'Easter':
    xbmc.executebuiltin('Skin.SetBool(Easter,True)')

    xbmc.executebuiltin('Skin.SetBool(ValentinesDay,False)')
    xbmc.executebuiltin('Skin.SetBool(StPatricksDay,False)')
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
  
if command and command[0] == '4th of July':
    xbmc.executebuiltin('Skin.SetBool(4thOfJuly,True)')

    xbmc.executebuiltin('Skin.SetBool(ValentinesDay,False)')
    xbmc.executebuiltin('Skin.SetBool(StPatricksDay,False)')
    xbmc.executebuiltin('Skin.SetBool(Easter,False)')
    xbmc.executebuiltin('Skin.SetBool(Halloween,False)')
    xbmc.executebuiltin('Skin.SetBool(Thanksgiving,False)')
    xbmc.executebuiltin('Skin.SetBool(Christmas,False)')
    xbmc.executebuiltin('Skin.SetBool(NewYearsEve,False)')
    xbmc.executebuiltin('Skin.SetBool(Spring,False)')  
    xbmc.executebuiltin('Skin.SetBool(Summer,False)')
    xbmc.executebuiltin('Skin.SetBool(Autumn,False)')
    xbmc.executebuiltin('Skin.SetBool(Winter,False)') 
    xbmc.executebuiltin('Skin.SetBool(Beach,False)')  

if command and command[0] == 'Halloween':
    xbmc.executebuiltin('Skin.SetBool(Halloween,True)')

    xbmc.executebuiltin('Skin.SetBool(ValentinesDay,False)')
    xbmc.executebuiltin('Skin.SetBool(StPatricksDay,False)')
    xbmc.executebuiltin('Skin.SetBool(Easter,False)')
    xbmc.executebuiltin('Skin.SetBool(4thOfJuly,False)')
    xbmc.executebuiltin('Skin.SetBool(Thanksgiving,False)')
    xbmc.executebuiltin('Skin.SetBool(Christmas,False)')
    xbmc.executebuiltin('Skin.SetBool(NewYearsEve,False)')
    xbmc.executebuiltin('Skin.SetBool(Spring,False)')  
    xbmc.executebuiltin('Skin.SetBool(Summer,False)')
    xbmc.executebuiltin('Skin.SetBool(Autumn,False)')
    xbmc.executebuiltin('Skin.SetBool(Winter,False)')     
    xbmc.executebuiltin('Skin.SetBool(Beach,False)')  
    
if command and command[0] == 'Thanksgiving':
    xbmc.executebuiltin('Skin.SetBool(Thanksgiving,True)')

    xbmc.executebuiltin('Skin.SetBool(ValentinesDay,False)')
    xbmc.executebuiltin('Skin.SetBool(StPatricksDay,False)')
    xbmc.executebuiltin('Skin.SetBool(Easter,False)')
    xbmc.executebuiltin('Skin.SetBool(4thOfJuly,False)')
    xbmc.executebuiltin('Skin.SetBool(Halloween,False)')
    xbmc.executebuiltin('Skin.SetBool(Christmas,False)')
    xbmc.executebuiltin('Skin.SetBool(NewYearsEve,False)')
    xbmc.executebuiltin('Skin.SetBool(Spring,False)')  
    xbmc.executebuiltin('Skin.SetBool(Summer,False)')
    xbmc.executebuiltin('Skin.SetBool(Autumn,False)')
    xbmc.executebuiltin('Skin.SetBool(Winter,False)')  
    xbmc.executebuiltin('Skin.SetBool(Beach,False)')  
    
if command and command[0] == 'Christmas':
    xbmc.executebuiltin('Skin.SetBool(Christmas,True)')

    xbmc.executebuiltin('Skin.SetBool(ValentinesDay,False)')
    xbmc.executebuiltin('Skin.SetBool(StPatricksDay,False)')
    xbmc.executebuiltin('Skin.SetBool(Easter,False)')
    xbmc.executebuiltin('Skin.SetBool(4thOfJuly,False)')
    xbmc.executebuiltin('Skin.SetBool(Halloween,False)')
    xbmc.executebuiltin('Skin.SetBool(Thanksgiving,False)')
    xbmc.executebuiltin('Skin.SetBool(NewYearsEve,False)')
    xbmc.executebuiltin('Skin.SetBool(Spring,False)')  
    xbmc.executebuiltin('Skin.SetBool(Summer,False)')
    xbmc.executebuiltin('Skin.SetBool(Autumn,False)')
    xbmc.executebuiltin('Skin.SetBool(Winter,False)')  
    xbmc.executebuiltin('Skin.SetBool(Beach,False)')  

if command and command[0] == 'New Years Eve':
    xbmc.executebuiltin('Skin.SetBool(NewYearsEve,True)')

    xbmc.executebuiltin('Skin.SetBool(ValentinesDay,False)')
    xbmc.executebuiltin('Skin.SetBool(StPatricksDay,False)')
    xbmc.executebuiltin('Skin.SetBool(Easter,False)')
    xbmc.executebuiltin('Skin.SetBool(4thOfJuly,False)')
    xbmc.executebuiltin('Skin.SetBool(Halloween,False)')
    xbmc.executebuiltin('Skin.SetBool(Thanksgiving,False)')
    xbmc.executebuiltin('Skin.SetBool(Christmas,False)')
    xbmc.executebuiltin('Skin.SetBool(Spring,False)')  
    xbmc.executebuiltin('Skin.SetBool(Summer,False)')
    xbmc.executebuiltin('Skin.SetBool(Autumn,False)')
    xbmc.executebuiltin('Skin.SetBool(Winter,False)') 
    xbmc.executebuiltin('Skin.SetBool(Beach,False)')  

if command and command[0] == 'Spring':
    xbmc.executebuiltin('Skin.SetBool(Spring,True)')

    xbmc.executebuiltin('Skin.SetBool(ValentinesDay,False)')
    xbmc.executebuiltin('Skin.SetBool(StPatricksDay,False)')
    xbmc.executebuiltin('Skin.SetBool(Easter,False)')
    xbmc.executebuiltin('Skin.SetBool(4thOfJuly,False)')
    xbmc.executebuiltin('Skin.SetBool(Halloween,False)')
    xbmc.executebuiltin('Skin.SetBool(Thanksgiving,False)')
    xbmc.executebuiltin('Skin.SetBool(Christmas,False)')
    xbmc.executebuiltin('Skin.SetBool(NewYearsEve,False)')  
    xbmc.executebuiltin('Skin.SetBool(Summer,False)')
    xbmc.executebuiltin('Skin.SetBool(Autumn,False)')
    xbmc.executebuiltin('Skin.SetBool(Winter,False)')    
    xbmc.executebuiltin('Skin.SetBool(Beach,False)')  
    
if command and command[0] == 'Summer':
    xbmc.executebuiltin('Skin.SetBool(Summer,True)')

    xbmc.executebuiltin('Skin.SetBool(ValentinesDay,False)')
    xbmc.executebuiltin('Skin.SetBool(StPatricksDay,False)')
    xbmc.executebuiltin('Skin.SetBool(Easter,False)')
    xbmc.executebuiltin('Skin.SetBool(4thOfJuly,False)')
    xbmc.executebuiltin('Skin.SetBool(Halloween,False)')
    xbmc.executebuiltin('Skin.SetBool(Thanksgiving,False)')
    xbmc.executebuiltin('Skin.SetBool(Christmas,False)')
    xbmc.executebuiltin('Skin.SetBool(NewYearsEve,False)')  
    xbmc.executebuiltin('Skin.SetBool(Spring,False)')
    xbmc.executebuiltin('Skin.SetBool(Autumn,False)')
    xbmc.executebuiltin('Skin.SetBool(Winter,False)')  
    xbmc.executebuiltin('Skin.SetBool(Beach,False)')  
    
if command and command[0] == 'Autumn':
    xbmc.executebuiltin('Skin.SetBool(Autumn,True)')

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
    xbmc.executebuiltin('Skin.SetBool(Winter,False)')     
    xbmc.executebuiltin('Skin.SetBool(Beach,False)')  
    
if command and command[0] == 'Winter':
    xbmc.executebuiltin('Skin.SetBool(Winter,True)')

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
    xbmc.executebuiltin('Skin.SetBool(Beach,False)')      

if command and command[0] == 'Beach':
    xbmc.executebuiltin('Skin.SetBool(Beach,True)')

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
    
if command and command[0] == 'Skin Default':
    xbmc.executebuiltin('Skin.SetBool(SkinDefault,True)')
    
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