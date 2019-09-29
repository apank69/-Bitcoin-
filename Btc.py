from multiprocessing.pool import ThreadPool
theme: jekyll-theme-hacker
import os,time,sys,shutil
import autobot.py
import

class Main:

	def __init__(self):
		self.detekos()

	def menu(self):
                  print("""
☜☆☞☜☆☞☜☆☞☜☆☞☜☆☞☜☆☞☜☆☞☜☆☞☜☆☞☜☆☞☜☆☞☜☆☞☜☆☞☜☆☞☜☆☞☜☆☞☜☆☞☜☆☞☜☆☞☜☆☞
☜☆☞        ꧁☆☬κɪɴɢ☬☆꧂            ☜☆☞
☜☆☞                        of                             ☜☆☞
☜☆☞         ◌⑅♡⋆♡LOVE♡⋆♡●⑅◌           ☜☆☞
☜☆☞                                                        ☜☆☞
☜☆☞☜☆☞☜☆☞☜☆☞☜☆☞☜☆☞☜☆☞☜☆☞☜☆☞☜☆☞☜☆☞☜☆☞☜☆☞☜☆☞☜☆☞☜☆☞☜☆☞☜☆☞☜☆☞☜☆☞


1.Star hack

""")

                     pilih=int(input ('/Go :'))

if pilih == 1 :
import config.php

def detekos(self):
		#remove cache
		try:
			shutil.rmstart("src/__pycache__")
		except: pass

		if os.name in ['nt','win32']:
			os.system('cls')
		else: os.system('clear')
		self.menu()

try:
	Main()
except KeyboardInterrupt:
	exit('[Exit] Key interrupt')
except Exception as F:
	print('Err: %s'%(F))
