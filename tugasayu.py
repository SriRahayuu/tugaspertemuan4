class Benda(object):
	def __init__ (self, k, m, p ):
		self.kursi = k
		self.meja = m
		self.penghapus = p

	def jumlahBenda(self):
		return self.kursi + self.meja + self.penghapus

	def cetakData(self):
		print("kursi\t: ", self.kursi)
		print("meja\t: ", self.meja)
		print("penghapus\t: ", self.penghapus)

	def cetakJH(self):
		print("Total dari semua benda diatas\t= ", self.jumlahbenda())

class warnabenda(Benda):
	def __init__(self, k, m , p, w):
		self.kursi = k
		self.meja = m
		self.penghapus = p
		self.warna = w
	def cetakData(self):
		print("kursi\t: ", self.kursi)
		print("meja\t: ", self.meja)
		print("penghapus\t: ", self.penghapus)
		print("warna dari semua benda tersebut adalah", self.warna)

def main():
	wh1 = warnaBenda(2, 3, 2,"HITAM" )

	wh1.cetakData()
	wh1.cetakJH()

if __name__ == "__main__":
	main()
