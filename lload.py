import time
def loading(total):
    for i in range(total + 1):
        persen = (i * 100) / total  # buat itung persen 
        bar = ''
        for j in range(i):
            bar += '='
        for k in range(total - i):
            bar += ' '
        #\r untuk menghapus baris sebelumnya
        print(f'\r[{bar}] {int(persen)}%', end='')
        time.sleep(0.3)
    print('\nLoading complete!')
loading(40)
