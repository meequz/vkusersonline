#! /usr/bin/env python
# coding: utf-8
import vk_api
import getpass
import time
from datetime import datetime
import sys
from vkuoconfig import *


def get_friends_online():
	response = vk.method('friends.getOnline', {})
	return len(response)

def get_group_members_online(groupid):
	response = vk.method('groups.getMembers', {'group_id': groupid, 'fields': 'online, online_mobile'})
	onlines = 0
	onlines_mobile = 0
	for user in response['users']:
		if user['online'] == 1: onlines += 1
		try:
			if user['online_mobile'] == 1: onlines_mobile += 1
		except KeyError:
			continue
	return onlines, onlines_mobile

def add_to_file(what_add, target_file, end=''):
	outfile = open(target_file, 'a+')
	outfile.write(str(what_add) + end)
	outfile.close()

def print_inplace(string):
	string = str(string) + '\r'
	sys.stdout.write(string)
	sys.stdout.flush()


login = input('email: ')
password = getpass.getpass('password: ')
timeout = time.time() + totaltime
started_at_unix = time.time()
started_at = datetime.fromtimestamp(started_at_unix).strftime('%Y-%m-%d %H:%M:%S')
print('started at {0} ({1})'.format(started_at, started_at_unix))

while True:
	vk = vk_api.VkApi(login, password)

	fr_onl = get_friends_online()
	string = '{0} {1}'.format(time.time(), fr_onl)
	add_to_file(string, 'myfriends_online.txt', end='\n')

	for idx, groupid in enumerate(groups):
		grname = grnames[idx]
		gr_onl, gr_mob_onl = get_group_members_online(groupid)
		string = '{0} {1} {2}'.format(time.time(), gr_onl, gr_mob_onl)
		add_to_file(string, 'club{0}_{1}_online.txt'.format(groupid, grname), end='\n')

	secsleft = timeout - time.time()
	timesleft = int(secsleft / period+1)
	print_inplace('{0} minutes left, {1} samples left           '.format(int(secsleft/60), timesleft))

	time.sleep(period)
	if time.time() > timeout: break

print()
