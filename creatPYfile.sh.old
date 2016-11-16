#!/bin/bash

#File Name:creatPYfile
#Author:pengyicheng
#Version:1.0
#Create time:20161101
#Description:

[ $# -ne 1 ] && \
     echo -e "This script is used to create the file head for a new python script;\nYou must bring a parameter as the prefix of the new script name." && \
     exit 2

echo -e "#!/usr/bin/env python\n# -*- coding: UTF-8 -*- \n\n#File Name:$1.py\n#Author:pengyicheng\n#Version:1.0\n#Create Time:`date '+%Y%m%d'`\n#Description:\n\n\n\n\n" >$1.py
chmod +x $1.py
echo -e "\033[31m$1.py creation success!\033[0m"

exit 0



exit 0
