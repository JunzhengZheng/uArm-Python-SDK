#!/usr/bin/env python3
# Software License Agreement (BSD License)
#
# Copyright (c) 2018, UFACTORY, Inc.
# All rights reserved.
#
# Author: Vinman <vinman.wen@ufactory.cc> <vinman.cub@gmail.com>

from serial.tools import list_ports


def get_ports():
    ports = []
    for i in list_ports.comports():
        if i.pid is not None:
            ports.append({
                'pid': '{:04x}'.format(i.pid),
                'vid': '{:04x}'.format(i.vid),
                'device': i.device,
                'serial_number': i.serial_number,
                'hwid': i.hwid,
                'name': i.name,
                'description': i.description,
                'interface': i.interface,
                'location': i.location,
                'manufacturer': i.manufacturer,
                'product': i.product
            })
    return ports


def select_port(filters, connect_ports=[]):
    port = None
    for i in list_ports.comports():
        if i.pid is None:
            continue
        if i.device in connect_ports:
            continue
        if not isinstance(filters, dict):
            port = i.device
            break
        is_match = True
        for k, v in filters.items():
            if not hasattr(i, k):
                continue
            a = getattr(i, k)
            if not a:
                a = ''
            if a.find(v) == -1:
                is_match = False
                break
        if is_match:
            port = i.device
            break
    return port