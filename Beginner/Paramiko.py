import paramiko


def ssh_cmd(ibox, cmd):
    """ssh to system(ibox) and issue the command(cmd)"""
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(key_filename='/root/.ssh/mfg_root_id', hostname=ibox)
    stdin, stdout, stderr = client.exec_command(cmd)
    opt = stdout.readlines()
    opt = "".join(opt)
    return(opt)