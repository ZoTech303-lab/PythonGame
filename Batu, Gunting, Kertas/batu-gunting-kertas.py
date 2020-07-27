import random
import os


clear = lambda: os.system('clear')
clear()


pembuat_script = '''
====================================
=   Nama   : Rian Prastio          =
=   Umur   : 15 Tahun              =
=   kelas  : X (10)smk             =
=   sekolah: SMK Tanjung Priok 2   =
====================================\n'''


#menang = 0
#kalah = 0
#seri = 0

game = ['Batu', 'Gunting', 'Kertas']

print '\nPembuat script ini: '
print pembuat_script

score1 = 0
score2 = 0

while True:
	bot = random.choice(game).lower()
	pemain = str(raw_input('''\nGame:
--------------
  1.Batu
  2.Gunting
  3.Kertas
--------------

-------------------
  4.Exit / Keluar
-------------------
		
>> ''')).lower()
	
	
	
	if len(pemain) == 0:
		pemain = random.choice(game).lower()
		print '\nJawaban random:', pemain
	
		# Batu
		if pemain == 'batu' and bot == 'gunting':
			clear()
			print '\nJawaban random:', pemain
			print '\n----------------------'
			print '-  Kamu menang!      -'
			print '-  Komputer kalah!   -'
			print '----------------------'
			score1 = score1 + 1
	
		elif pemain == 'batu' and bot == 'kertas':
			clear()
			print '\nJawaban random:', pemain
			print '\n----------------------'
			print '-  Kamu kalah!       -'
			print '-  Komputer menang!  -'
			print '----------------------'
			score2 = score2 + 1
	
		elif pemain == 'batu' and bot == 'batu':
			clear()
			print '\nJawaban random:', pemain
			print '\n-----------------------'
			print '-        Seri!        -'
			print '-----------------------'
	
	
			# Gunting
		elif pemain == 'gunting' and bot == 'batu':
			clear()
			print '\nJawaban random:', pemain
			print '\n----------------------'
			print '-  Kamu kalah!       -'
			print '-  Komputer menang!  -'
			print '----------------------'
			score2 = score2 + 1
	
	
		elif pemain == 'gunting' and bot == 'kertas':
			clear()
			print '\nJawaban random:', pemain
			print '\n----------------------'
			print '-  Kamu menang!      -'
			print '-  Komputer kalah!   -'
			print '----------------------'
			score1 = score1 + 1
	
	
		elif pemain == 'gunting' and bot == 'gunting':
			clear()
			print '\nJawaban random:', pemain
			print '\n-----------------------'
			print '-        Seri!        -'
			print '-----------------------'
		
		# Kertas
		elif pemain == 'kertas' and bot == 'gunting':
			clear()
			print '\nJawaban random:', pemain
			print '\n----------------------'
			print '-  Kamu kalah!       -'
			print '-  Komputer menang!  -'
			print '----------------------'
			score2 = score2 + 1
	
	
		elif pemain == 'kertas' and bot == 'batu':
			clear()
			print '\nJawaban random:', pemain
			print '\n----------------------'
			print '-  Kamu menang!      -'
			print '-  Komputer kalah!   -'
			print '----------------------'
			score1 = score1 + 1
	
	
		elif pemain == 'kertas' and bot == 'kertas':
			clear()
			print '\nJawaban random:', pemain
			print '\n-----------------------'
			print '-        Seri!        -'
			print '-----------------------'
	
		else:
			print 'Error!!'
	
		
	elif pemain == '1' or pemain == 'batu':
		pemain = 'batu'
	
	
		if pemain == 'batu' and bot == 'kertas':
			clear()
			print '\n----------------------'
			print '-  Kamu kalah!       -'
			print '-  Komputer menang!  -'
			print '----------------------'
			score2 = score2 + 1
	
	
		elif pemain == 'batu' and bot == 'gunting':
			clear()
			print '\n----------------------'
			print '-  Kamu menang!      -'
			print '-  Komputer kalah!   -'
			print '----------------------'
			score1 = score1 + 1
	
	
		elif pemain == 'batu' and bot == 'batu':
			clear()
			print '\n-----------------------'
			print '-        Seri!        -'
			print '-----------------------'
	
	
		else:
			print '\nError!!'
		
	
	elif pemain == '2' or pemain == 'gunting':
		pemain = 'gunting'
	
	
		if pemain == 'gunting' and bot == 'batu':
			clear()
			print '\n----------------------'
			print '-  Kamu kalah!       -'
			print '-  Komputer menang!  -'
			print '----------------------'
			score2 = score2 + 1
	
	
		elif pemain == 'gunting' and bot == 'kertas':
			clear()
			print '\n----------------------'
			print '-  Kamu menang!      -'
			print '-  Komputer kalah!   -'
			print '----------------------'
			score1 = score1 + 1
	
	
		elif pemain == 'gunting' and bot == 'gunting':
			clear()
			print '\n-----------------------'
			print '-        Seri!        -'
			print '-----------------------'
	
	
		else:
			print 'Error!!'
	
	
	elif pemain == '3' or pemain == 'kertas':
		pemain = 'kertas'
	

		if pemain == 'kertas' and bot == 'gunting':
			clear()
			print '\n----------------------'
			print '-  Kamu kalah!       -'
			print '-  Komputer menang!  -'
			print '----------------------'
			score2 = score2 + 1
	
	
		elif pemain == 'kertas' and bot == 'batu':
			clear()
			print '\n----------------------'
			print '-  Kamu menang!      -'
			print '-  Komputer kalah!   -'
			print '----------------------'
			score1 = score1 + 1
	
	
		elif pemain == 'kertas' and bot == 'kertas':
			clear()
			print '\n-----------------------'
			print '-        Seri!        -'
			print '-----------------------'
	
	elif pemain == '4':
		clear()
		print pembuat_script
		print '\nScore: '
		print '\nKamu', score1
		print 'Komputer', score2
		print '\nTerima kasih telah memakai script ini ^_^'
		exit()



	elif pemain == 'exit':
		clear()
		print pembuat_script
		print '\nScore: '
		print '\nKamu', score1
		print 'Komputer', score2
		print '\nTerima kasih telah memakai script ini ^_^'
		exit()
	
	
	elif pemain == 'keluar':
		clear()
		print pembuat_script
		print '\nScore: '
		print '\nKamu', score1
		print 'Komputer', score2
		print '\nTerima kasih telah memakai script ini ^_^'
		exit()
	
		
	else:
		clear()
		print '\nPembuat script ini: '
		print pembuat_script
		print 'Upss perintah tidak cocok!\n'
		break
		
	
	print '\nKamu     :', pemain
	print 'Komputer :', bot

	print '\n\nScore:'
	print '\nKamu', score1
	print 'Komputer', score2
	
#		menang = 0
#		if menang == True:
#			print 'score kamu:', menang + 1
#
#			if True:
#				menang += 1
#	
#			else:
#				menang -= 1
#	
#	
#		else:
#			print 'score kamu:', menang - 1
#			if True:
#				menang -= 1
#
#			else:
#				menang += 1
#	
#		kalah = 0
#		seri = 0