
Estuary MOD V2 Theme Selector

Change theme settings for Bower9065's mod of Estuary Mod V2 from Home Assistant using Kodi integration.

Accepted commands:

    'Valentines Day' 
    'St Patricks Day'
    'Easter', '4th of July'
	'Halloween'
	'Thanksgiving'
	'Chrtistmas'
	'New Years Eve'
	'Spring'
	'Summer'
	'Autumn'
	'Winter'
	'Holiday Themes on'
	'Holiday Themes off'
	'String Lights on'
	'String Lights off'
	'Snow Effect on' 
	'Snow Effect off'
	'Character on'
	'Character off'

Example call-service:

	alias: Kodi Themes - Thanksgiving
	service: kodi.call_method
	target:
	entity_id:
		- media_player.kodi_pc
		- media_player.kodi_bedroom
		- media_player.kodi_living_room
	data:
		method: Addons.ExecuteAddon
		addonid: script.estuary.mod_v2_theme_selector
		params:
		command: Thanksgiving