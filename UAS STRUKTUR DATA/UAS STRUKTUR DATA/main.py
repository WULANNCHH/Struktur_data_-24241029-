def main():
    # 1. Input nama customer dan tanggal belanja, simpan dalam tuple
    nama = input("Masukkan nama customer: ")
    tanggal = input("Masukkan tanggal belanja (DD-MM-YYYY): ")
    data_customer = (nama, tanggal)

    # 2. Input jumlah barang yang akan dibeli
    try:
        jumlah_barang = int(input("Masukkan jumlah barang yang akan dibeli: "))
    except ValueError:
        print("Input harus berupa angka.")
        return

    # 3. Input detail tiap barang, simpan dalam dictionary
    daftar_barang = []

    for i in range(jumlah_barang):
        print(f"\nBarang ke-{i+1}")
        nama_barang = input("Nama barang: ")
        try:
            harga_satuan = float(input("Harga satuan barang: "))
            qty = int(input("Jumlah qty: "))
        except ValueError:
            print("Harga dan qty harus berupa angka.")
            return

        barang = {
            'nama': nama_barang,
            'harga': harga_satuan,
            'qty': qty,
            'total': harga_satuan * qty
        }
        daftar_barang.append(barang)

    # 5. Tampilkan data customer, daftar belanja, dan total bayar
    print("\n--- STRUK BELANJA ---")
    print(f"Nama Customer: {data_customer[0]}")
    print(f"Tanggal Belanja: {data_customer[1]}")
    print("\nDaftar Belanja:")

    total_bayar = 0
    for idx, item in enumerate(daftar_barang, 1):
        print(f"{idx}. {item['nama']} - {item['qty']} x {item['harga']} = {item['total']}")
        total_bayar += item['total']

    print(f"\nTotal Bayar: Rp {total_bayar:,.2f}")

if __name__ == "__main__":
    main()
