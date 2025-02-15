# Estuary MOD V2 Theme Selector

Change theme settings for Bower9065's mod of Estuary Mod V2 from Home Assistant using Kodi integration.
Toggle theme, string lights, characters and snow effect.
Accepted holiday commands:
    'ValentinesDay' 
    'StPatricksDay'
    'Easter',
	'4thofJuly'
	'Halloween'
	'Thanksgiving'
	'Chrtistmas'
	'NewYearsEve'
	'Spring'
	'Summer'
	'Autumn'
	'Winter'

Example call-service:

Change theme
	alias: Kodi Themes - Valentines Day
	target:
	  entity_id:
		- media_player.kodi_pc
	data:
	  method: Addons.ExecuteAddon
	  addonid: script.estuary.modv2_theme_selector
	  params:
		type: Holiday
		command: ValentinesDay
	action: kodi.call_method

Turn snow effect on
	alias: Kodi Themes - Valentines Day
	target:
	  entity_id:
		- media_player.kodi_pc
	data:
	  method: Addons.ExecuteAddon
	  addonid: script.estuary.modv2_theme_selector
	  params:
		type: Snow_Effect_on
		command: "true"
	action: kodi.call_method

Turn string lights off
	alias: Kodi Themes - Valentines Day
	target:
	  entity_id:
		- media_player.kodi_pc
	data:
	  method: Addons.ExecuteAddon
	  addonid: script.estuary.modv2_theme_selector
	  params:
		type: String_Lights_on
		command: "false"
	action: kodi.call_method
	
Turn themes on
	alias: Kodi Themes - Valentines Day
	target:
	  entity_id:
		- media_player.kodi_pc
	data:
	  method: Addons.ExecuteAddon
	  addonid: script.estuary.modv2_theme_selector
	  params:
		type: Themes_on
		command: "true"
	action: kodi.call_method
	
Turn characters and trees off
	alias: Kodi Themes - Valentines Day
	target:
	  entity_id:
		- media_player.kodi_pc
	data:
	  method: Addons.ExecuteAddon
	  addonid: script.estuary.modv2_theme_selector
	  params:
		type: Character_on
		command: "false"
	action: kodi.call_method