'''
This is a CISCO IOSXE EEM auto backup script for device configration.
[YESLAB]
'''

import os
import cli

output = cli.cli('show run')
os.chdir("/bootflash/enaui_backup/")
f = open("show_run.cfg","w")
f.write(output)
f.close
os.system("git add .")
os.system("git commit -am 'commited by Automation' ")