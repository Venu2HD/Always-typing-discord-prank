from scripts.install_requirements import install_requirements
from scripts.check_requirements import check_requirements
from json import load, JSONDecodeError
from requests import post
from time import sleep

install_requirements(check_requirements())

try:
	with open("settings.json", "r") as settings_opened:
		settings = load(settings_opened)
except FileNotFoundError:
	open("settings.json", "w").close()
	input("No settings file found!\nCreating new one...\nPress enter to exit...")
	exit()
except JSONDecodeError or not isinstance(settings["discord_token"], str) or isinstance(settings["channel_id"], int):
	with open("settings.json", "w") as settings_opened:
		settings_opened.write('{\n    "discord_token": "YOUR_DISCORD_TOKEN",\n    "channel_id": CHANNEL_ID_TO_BE_FAKE_TYPED_IN\n}')
	input("Invalid settings in settings.json, rewriting...\nPress enter to close the program")
	exit()

while True:
	response = post(url = f"https://discord.com/api/v9/channels/{settings['channel_id']}/typing", headers = {"authorization": settings["discord_token"]})
	if response.status_code != 204:
		print(f"Failed - {response.status_code}")
	else:
		print(f"Sent - {response.status_code}")
	sleep(9.8)