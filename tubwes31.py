# Kamus untuk masing masing kategori
S = ["hilmi", "mereka", "arip", "hanip", "saya"]
P = ["baca", "lihat", "main", "tulis", "makan"]
O = ["bubur", "tugas", "apel", "musik", "komik"]
K = ["sekarang", "kemarin", "nanti", "lusa", "bersama"]
#Stack push down automata
PDA = []
#fungsi untuk pop bagian atas stack
def pop(PDA, i):
    if i in PDA:
        PDA.remove(i)
    print(PDA)
#fungsi untuk push ke stack
def push(PDA, i):
    PDA.append(i)
    print(PDA)
#fungsi untuk melihat stack paling atas
def top(PDA):
    return PDA[-1]
#Identifikasi kata subjek dari kamus
def isS(word):
    return word in S
#Identifikasi kata predikat dari kamus
def isP(word):
    return word in P
#Identifikasi kata objek dari kamus
def isO(word):
    return word in O
#Identifikasi kata keterangan dari kamus
def isK(word):
    return word in K
#Program utama untuk mengenali pola, pola yang diterima adalah spok spk spo sp
def isPattern(v):
    #Mengosongkan stack untuk mempersiapkan penggunaan selanjutnya
    PDA.clear()  
    #Push # dan Start symbol ke dalam stack 
    push(PDA, '#')
    push(PDA, 'Q')
    #untuk menyimpan inputtan hasil token recognizer
    output = ""

    # disini v adalah sebuah array dari masing masing kata yang ada dan untuk setiap
    # kata di v di lakukan pengecekan yaitu token recognizer untuk menghasilkan input
    for word in v:
        # jika kata adalah Subjek
        if isS(word):
            output += 's'
            pop(PDA, 'Q')
            push(PDA, 'S')
        # jika kata adalah predikat
        elif isP(word):
            output += 'p'
            pop(PDA, 'S')
            push(PDA, 'P')
        elif isO(word):
            output += 'o'
            pop(PDA, 'P')
            push(PDA, 'O')
        elif isK(word):
            output += 'k'
            if top(PDA) == 'P':
                pop(PDA, 'P')
            elif top(PDA) == 'O':
                pop(PDA, 'O')
            push(PDA, 'K')
        #else output tidak dikenal atau tidak ada di dalam kamus
        else:
            output += '_'
            push(PDA, ' ')

    #Mengosongkan stack
    if top(PDA) == 'P':
        pop(PDA, 'P')
    elif top(PDA) == 'O':
        pop(PDA, 'O')
    elif top(PDA) == 'K':
        pop(PDA, 'K')
    #mengosongkan stack
    if top(PDA) == '#':
        pop(PDA, '#')  # Pop the '#' marker
    #Jika stack kosong maka valid atau accepted
    print(output)
    return len(PDA) == 0  

if __name__ == "__main__":
    while True:
        # Input dari user
        sentence = input("Masukkan kalimat atau ketik 'exit' untuk keluar: ").strip().lower()

        if sentence == "exit":
            break
        
        # pisah perkata dan masukkan jadi array
        v = sentence.split()
     
        #Cek apakah pattern dari kalimat benar adanya SPOK, SPK, SPO atau SP
        if isPattern(v):
            print("Accepted")
        else:
            print("Rejected")