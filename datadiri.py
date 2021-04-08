class Datadiri():
    def __init__(self, no_peserta, namalengkap, tgl_lahir, jk, hobi, goldar):
        self.no_peserta = no_peserta
        self.namalengkap = namalengkap
        self.tgl_lahir = tgl_lahir
        self.jk = jk
        self.hobi = hobi
        self.goldar = goldar

    def getNo_peserta(self):
        return self.no_peserta

    def getNamalengkap(self):
        return self.namalengkap

    def getTgl_lahir(self):
        return self.tgl_lahir

    def getJk(self):
        return self.jk

    def getHobi(self):
        return self.hobi

    def getGoldar(self):
        return self.goldar