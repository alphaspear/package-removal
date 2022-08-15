import json
import os
file = open('AppList.json')
App_to_remove = json.load(file)
command_prefix = "adb shell pm uninstall --user 0 "
for i in App_to_remove:
    print("removing " + i)
    command = command_prefix + i
    os.system(command)
file.close()
print("\n\nTASK COMPLETED")