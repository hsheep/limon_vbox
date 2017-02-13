import os
import socket
import subprocess
from SimpleXMLRPCServer import SimpleXMLRPCServer
import signal
import xmlrpclib
import json
import stat

BIND_IP = "0.0.0.0"
BIND_PORT = 8000


class Agent(object):
    def __init__(self):
        self.pid_list = {}
        self.logs = []

    def copyto(self, data, dst_path):
        try:
            self.print_log("copyto => %s" % dst_path)
            with open(dst_path, "wb") as sample:
                sample.write(data.data)
            os.chmod(dst_path, stat.S_IRWXU|stat.S_IRWXG|stat.S_IRWXO)
        except Exception as e:
            self.print_log("copyto exception => %s" % e)
            return False
        return True

    def copyfrom(self, dst_path):
        try:
            self.print_log("copyfrom => %s" % dst_path)
            with open(dst_path, "rb") as sample:
                return xmlrpclib.Binary(sample.read())
        except Exception as e:
            self.print_log("copyfrom exception => %s" % e)
        return None

    def listDirectoryInGuest(self, dst_dir):
        dir_list = []
        self.print_log("listDirectoryInGuest => %s" % dst_dir)
        yid = os.walk(dst_dir)
        for rootDir, pathList, fileList in yid:
            for file in fileList:
                root_path = os.path.join(rootDir, file)
                dir_list.append(root_path[len(dst_dir):])
        return dir_list

    def killProcessInGuest(self, pid):
        if str(pid) not in self.pid_list:
            self.print_log("killProcessInGuest: pid %s is not found" % pid)
            return False
        self.print_log("killProcessInGuest: terminate pid %s" % pid)
        ps = self.pid_list[str(pid)]
        ps.terminate()
        ps.wait()

    def runProgramInGuest(self, program, arg=[]):
        cmd = [program]
        cmd.extend(arg)
        self.print_log("runProgramInGuest => %s" % cmd)
        sp = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        self.pid_list[str(sp.pid)] = sp
        return sp.pid

    def print_log(self, log_str):
        print log_str
        self.logs.append(log_str)

    def get_logs(self):
        return self.logs


if __name__ == "__main__":
    try:
        if not BIND_IP:
            BIND_IP = socket.gethostbyname(socket.gethostname())

        print("[+] Starting agent on %s:%s ..." % (BIND_IP, BIND_PORT))

        # Disable DNS lookup, by Scott D.
        def FakeGetFQDN(name=""):
            return name

        socket.getfqdn = FakeGetFQDN

        server = SimpleXMLRPCServer((BIND_IP, BIND_PORT), allow_none=True)
        server.register_instance(Agent())
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
