meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            'LOL': 'Tanggapan umum terhadap sesuatu yang lucu',
            'TTYL': 'Talk to you later',
            'GTG': 'got to go',
            'NGL': 'not gonna lie',
            'ETC': 'Etcetera/ Dan lain lain',
            'IDK': 'i dont know',
            'IDC': 'I dont care',
            'delish': 'enak',
            'chop-chop': 'cepetan',
            'All-nighter': 'belajar sambil begadang',
            'salfok': 'salah fokus',
            'salting': 'salah tingkah',
            'YTTA': 'Yang tau tau aja',
            'GG': 'Ga guna/good game',
            'aka': 'alias',
            'Yg': 'Yang',
            'nn': 'naon',
            }
word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")
if word in meme_dict.keys():
    # Apa yang harus kita lakukan jika kata itu ditemukan?
    print(meme_dict[word])
    
else:
    # Apa yang harus kita lakukan jika kata itu tidak ditemukan?
    print('kata yang kamu cari tidak ada')
