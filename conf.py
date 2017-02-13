# Limon
# Copyright (C) 2015 Monnappa
#
# This file is part of Limon.
#
# Limon is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Limon is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Limon.  If not, see <http://www.gnu.org/licenses/>.


"""
@author:       Monnappa K A
@license:      GNU General Public License 3.0
@contact:      monnappa22@gmail.com
@Description:  Configuration file for Limon sandbox
"""

##############[general variables]################################
py_path = r'/usr/bin/python'
report_dir = r'/home/ubuntu/limon_vmcode/limon/linux_reports'
dash_lines = "-" * 40
is_elf_file = False
virustotal_key = "e4e19dbc08d5c6f9502da196c05154ba61ed4e55e38e5ec3aaa58941b70b7dc0"

###############[vm variables]#####################################
host_analysis_vmpath = r'/root/virtual_machines/Ubuntu/Ubuntu.vmx'
host_vmrunpath = r'/usr/bin/vmrun'
host_vmtype = r'ws'

host_vm_type = r'vbox'
# ----------------------- VBOX CONFIG---------------------------------
host_vbox_guid = "{13d0f4f0-de32-4e07-9a5e-3e3dfe2ad715}"
analysis_agent_ip = "192.168.100.199"
analysis_agent_port = "8000"
# --------------------------------------------------------------------

analysis_username = "root"
analysis_password = "root0123456"
#analysis_clean_snapname = "system_copy_ok"
analysis_clean_snapname = "system_auth_bug"
analysis_mal_dir = r"/root/malware_analysis"
analysis_py_path = r'/usr/bin/python'
analysis_perl_path = r'/usr/bin/perl'
analysis_bash_path = r'/bin/bash'
analysis_sh_path = r'/bin/sh'
analysis_insmod_path = r'/sbin/insmod'
analysis_php_path = r'/usr/bin/php'


################[static analyis variables]##########################
yara_packer_rules = r'/home/ubuntu/limon_vmcode/limon/yara_rules/packer.yara'
yara_rules = r'/home/ubuntu/limon_vmcode/limon/yara_rules/capabilities.yara'

#################[network variables]#################################
analysis_ip = "192.168.100.199"
host_iface_to_sniff = "eth0"
host_tcpdumppath = "/usr/sbin/tcpdump"

#######################[memory anlaysis variables]##################

vol_path = r'/home/ubuntu/limon_vmcode/volatility-master/vol.py'
mem_image_profile = '--profile=LinuxUbuntu1404x64'

######################[inetsim variables]#########################
inetsim_path = r"/home/ubuntu/limon-sandbox/inetsim-1.2.6"
inetsim_log_dir = r"/home/ubuntu/limon-sandbox/inetsim-1.2.6/log"
inetsim_report_dir = r"/home/ubuntu/limon-sandbox/inetsim-1.2.6/report"

######################[monitoring varibales]##########################

analysis_sysdig_path = r'/usr/bin/sysdig'
host_sysdig_path = r'/usr/bin/sysdig'
analysis_capture_out_file = r'/root/logdir/capture.scap'

cap_format = "%proc.name (%thread.tid) %evt.dir %evt.type %evt.args"
cap_filter = r"""evt.type=clone or evt.type=execve or evt.type=chdir or evt.type=open or
evt.type=creat or evt.type=close or evt.type=socket or evt.type=bind or evt.type=connect or
evt.type=accept or evt.is_io=true or evt.type=unlink or evt.type=rename or evt.type=brk or
evt.type=mmap or evt.type=munmap or evt.type=kill or evt.type=pipe"""

analysis_strace_path = r'/usr/bin/strace'
strace_filter = r"-etrace=fork,clone,execve,chdir,open,creat,close,socket,connect,accept,bind,read,write,unlink,rename,kill,pipe,dup,dup2"
analysis_strace_out_file = r'/root/logdir/trace.txt'

analysis_log_outpath = r'/root/logdir'
params = []
