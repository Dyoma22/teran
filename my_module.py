from keyboard import*
from random import *
def start() :
	"""teeme valik kellega mängime
	tagastame m muutuja int formaadis

	:rtype: int
	"""

	print("Kivi, Käärid, Paber")
	m=3
	while m not in [1,2]:
		try:
			m=int(input("Kellega mängime?\n1-Botid - \n2-Robotiga - "))
		except:
			ValueError
	return m

def bot_vs_bot(v1:list,v2:list):
	while True:
		print("Kas mängime? esc - Väljä, enter - Mängime")
		if read_key()=="esc":
			break
		elif read_key()=="enter":
			p1=choice(v1)
			print("Esimene bot: ",p1)
			p2=choice(v2)
			print("Teine bot: ",p2)
			if p1==p2:
			   print("Viik")
		elif p1==v1[0] and p2==v2[1] or p1==v1[2] and p2==v2[0] or p1==v1[1] and p2==v2[2]:
			print("Vöitis 1")
		else:
			print("Vöitis 2")
