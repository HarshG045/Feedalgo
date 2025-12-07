"""UI Styling and themes"""

import config


class UIStyle:
	"""UI styling constants"""

	COLORS = config.COLORS
	FONTS = config.FONTS

	@staticmethod
	def button_style():
		return {
			"bg": config.COLORS["bg_secondary"],
			"fg": config.COLORS["text_primary"],
			"activebackground": config.COLORS["accent"],
			"activeforeground": config.COLORS["bg_primary"],
			"border": 0,
			"cursor": "hand2",
		}
