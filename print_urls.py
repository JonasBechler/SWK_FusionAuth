from pathlib import Path
import json

main_config_path = Path.cwd().parent / "main_config.json"


with open(main_config_path) as file:
    config = json.load(file)

apps = ["login", "konrad", "handyticket"]

for app in apps:
	app_str = f"""
{app}:
	redirect-url:\t{config["device_ip"]}:{config[app]["port"]}/kn/login_callback
	logout-url:\t{config["device_ip"]}:{config[app]["port"]}
	"""
	print(app_str)
