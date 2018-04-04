#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 22:04:43 2018

@author: monilshah
"""
import sys
import csv
from datetime import datetime, timedelta
TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
session = dict()
track_session = dict()

def createSession(log,inactivity_time):
    """ Get values from each row from the input and create a session for each ip"""
    ip=log['ip']
    curr_time = datetime.strptime(log['date']+' '+log['time'],TIME_FORMAT)
    end_session = curr_time+timedelta(seconds=int(inactivity_time)+1)
    if end_session not in track_session.keys():
        track_session[end_session]=[ip]   
    else:
        if ip not in track_session[end_session]:
            track_session[end_session].append(ip)
    return ip,curr_time,end_session,track_session    
    
def removeSession(ip,curr_time,end_session,track_session,inactivity_time):
    """ Remove session for the ip's whose session has been inactive for inactivity time period"""
    if curr_time in track_session.keys():
            temp = set(track_session[curr_time])
            for index in temp:
                if session[index]['end'] == curr_time-timedelta(seconds=int(inactivity_time)+1):
                        logOutput(session,index)                   
                        track_session[curr_time].remove(index)
                        del session[index]
    if ip not in session:
        session[ip] = {'start':curr_time,'end':curr_time,'duration':1,'requests':1}
    else:
        session[ip]['requests'] += 1
        session[ip]['end'] = curr_time
        session[ip]['duration'] = int((session[ip]['end'] - session[ip]['start']).total_seconds())+1
    return track_session,session
    
def updateSession(track_session,session):
    """ Update the session at the end with all the expiring sessions"""
    update = []
    for key,values in track_session.items():
        for value in values:
            if value not in update:
                logOutput(session,value)
                update.append(value)

def logOutput(session,index):
    """Print final output to a new file sessionation.txt"""
    with open(sys.argv[3],'a') as final:
                    writer = csv.writer(final)
                    output = [index,session[index]['start'].strftime('%Y-%m-%d %H:%M:%S'),session[index]['end'].strftime('%Y-%m-%d %H:%M:%S'),session[index]['duration'],session[index]['requests']]
                    writer.writerow(output)

try:
    open(sys.argv[3],'w').close()  #deleting old sessionization.txt for new input
    with open(sys.argv[2]) as a:
        inactivity = a.readlines()
        inactivity_time = inactivity[0]
    
    with open(sys.argv[1]) as b:
        log = csv.DictReader(b)
        for l in log:
            ip,curr_time,end_session,track_session = createSession(l,inactivity_time)
            track_session,session = removeSession(ip,curr_time,end_session,track_session,inactivity_time)
    updateSession(track_session,session)
except IOError as e:
    print('Operation failed: %s') % e.strerror
