#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1


def findAdmin():
	f = open("alp1x-list.txt","r");
	link = raw_input("Site Adresini Girin \n Ornek : hedefsite.com veya www.hedefsite.com ): ")
	print "\n\nTaraniyor : \n"
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "Bulundu --> ",req_link

def Credit():
	Space(9); print "#####################################"
	Space(9); print "#       Admin Panel Finder alp1x    #"
	Space(9); print "#                                   #"
	Space(9); print "#                                   #"
	Space(9); print "#####################################"
	

Credit()
findAdmin()
