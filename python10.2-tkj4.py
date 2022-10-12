# Membuat tipe data koleksi

koleksi_data_str = ["Pisang" , "Mangga" , "Jambu" , "Semangka" ]

koleksi_data_int = [200, 300, 400, 500]

koleksi_data_mix = ["Rizky Billar", 100 , True , "Reza Arap"]

print("koleksi data string:", koleksi_data_str)

print("koleksi data integear:", koleksi_data_int)

print("koleksi data campuran:", koleksi_data_mix)

# Buatlah 3 kumpulan data: nama hewan, nilai uts, nama teman sebangku kalian

koleksi_nama_hewan = ["sapi" , "burung" , "kambing" , "domba"]

koleksi_nilai_uts = [90 , 75 , 80 , 86 ]

koleksi_nama_teman = ["luul mukaromah", "mikha", "kazu", "nazla levianna"]

print("koleksi data string", koleksi_nama_hewan)

print("koleksi data integear", koleksi_nilai_uts)

print("koleksi data campuran", koleksi_nama_teman)

# data ke 2 nama hewan

print("data pertama nama hewan:", koleksi_nama_hewan[0])

# data pertama nilai uts

print("data pertama nilai uts:", koleksi_nilai_uts[0])

# data terakhir nama teman sebangku

print("data terakhir teman sebangku:", koleksi_nama_teman[3])

# tambahkan 1 data di setiap data koleksi 

koleksi_nama_hewan.append("singa")

koleksi_nilai_uts.append("88")

koleksi_nama_teman.append("yuna")

print(koleksi_nama_hewan, koleksi_nilai_uts, koleksi_nama_teman)

# ubahlah data terakhir nilai uts

koleksi_nilai_uts[-1] = 66

# ubahlah data ketiga nama hewan

koleksi_nama_hewan[2] = "gajah"

print(koleksi_nilai_uts, koleksi_nama_hewan)