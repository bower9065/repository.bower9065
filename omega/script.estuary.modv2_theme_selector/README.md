**Estuary MOD V2 Theme Selector**

Change theme settings for Bower9065's mod of Estuary Mod V2 from Home Assistant using Kodi integration.
Toggle themes, string lights, characters and snow effect.

Accepted  holiday commands:

    'ValentinesDay'
    'StPatricksDay'
    'Easter', 
    '4thofJuly'
	'Halloween'
	'Thanksgiving'
	'Chrtistmas'
	'NewYearsEve
	'Spring'
	'Summer'
	'Autumn'
	'Winter'

Example call-service:
Change theme

	alias: Kodi Themes - 4th of July
	target:
	  entity_id:
	    - media_player.kodi_pc
	data:
	  method: Addons.ExecuteAddon
	  addonid: script.estuary.modv2_theme_selector
	  params:
	    type: Holiday
	    command: 4thOfJuly
	action: kodi.call_method
Turn off "Themes"

	alias: Kodi Themes - Turn off Themes
	target:
	  entity_id:
	    - media_player.kodi_pc
	data:
	  method: Addons.ExecuteAddon
	  addonid: script.estuary.modv2_theme_selector
	  params:
	    type: Themes_on
	    command: "false"
	action: kodi.call_method
Turn on "String Lights"

	alias: Kodi Themes - Turn on String Lights
	target:
	  entity_id:
	    - media_player.kodi_pc
	data:
	  method: Addons.ExecuteAddon
	  addonid: script.estuary.modv2_theme_selector
	  params:
	    type: String_Lights_on
	    command: "true"
	action: kodi.call_method
Turn off "Characters"

	alias: Kodi Themes - Turn off characters
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
Turn on "Snow Effect"

	alias: Kodi Themes - Turn on Snow Effect
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