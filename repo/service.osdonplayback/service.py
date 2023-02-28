#!/usr/bin/python

import os
import xbmc
import xbmcaddon
import xbmcgui
from xbmcaddon import Addon

class OSDonPlayback(xbmc.Player):
    def __init__(self, *args, **kwargs):
        xbmc.Player.__init__(self)
        self.run = True
        
    def onPlayBackStarted(self):
        if self.isPlayingVideo() and Addon().getSettingBool("osdonplayback_enable"):
                #if the file that is playing is a video file and 'OSD'onPlayback is enabled in addon settings            
            if not xbmc.getCondVisibility("Window.IsActive(seekbar)"):
                    #if seekbar is not active
                xbmc.sleep(200)
                #small pause
                xbmc.executebuiltin('Action(ShowTime)')
                    #opens Video OSD
                xbmc.log("'OSD'onPlayback: Displaying Video OSD", xbmc.LOGINFO)
                    #creates log entry
        video = (xbmc.getInfoLabel("Player.Title()"))
            #sets currently playing Video Title = video
        while video == (xbmc.getInfoLabel("Player.Title()")):              
            #while video = currenty playing video title
            if (int(xbmc.getInfoLabel("Player.Time(secs)"))) >= (Addon().getSettingInt("osdonplayback_seconds")): 
                   #if currently playing video elapsed time is >= Addon setting
                if xbmc.getCondVisibility("Window.IsActive(seekbar)"):
                        #if seekbar is active
                    xbmc.executebuiltin('Action(ShowTime)')
                        #closes Video OSD            
                    xbmc.log("'OSD'onPlayback: Closing Video OSD", xbmc.LOGINFO)
                        #creates log entry   
                    break
        try:
            monitor.waitForAbort(3)
        except:
            pass
        else:
            xbmc.log("'OSD'onPlayback: Not a video file, finishing", xbmc.LOGINFO)

monitor = xbmc.Monitor()
class OSDonPlayback:
    player = OSDonPlayback()
    while not monitor.abortRequested():
        monitor.waitForAbort(1)
    del player
                    
                    