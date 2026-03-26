#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# SPDX-License-Identifier: GPL-3.0-only
# SPDX-FileCopyrightText: 2026 Carupp Security
#
# Secure Data Eraser - Community Edition
# Copyright (C) 2026 Carupp Security
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import os
import sys
import argparse
import random
import time
import math


BLOCK_SIZE = 4096  
PROGRESS_INTERVAL = 0.5  


PATTERN_ZERO = b'\x00'
PATTERN_ONE  = b'\xff'
RANDOM_MAX   = 256

def random_block(length):
    """Rastgele bayt bloğu üretir."""
    return bytes(random.getrandbits(8) for _ in range(length))

def zero_block(length):
    """Sıfır bloğu üretir."""
    return PATTERN_ZERO * length

def one_block(length):
    """0xFF bloğu üretir."""
    return PATTERN_ONE * length


def write_pass(fd, size, pattern_func, verify=False):
    """
    Bir geçiş yapar: pattern_func(size) ile bloğu yazar.
    verify=True ise yazılan veriyi okuyup karşılaştırır.
    """
    bytes_written = 0
    while bytes_written < size:
        remaining = size - bytes_written
        chunk_size = min(BLOCK_SIZE, remaining)
        data = pattern_func(chunk_size)
        try:
            fd.write(data)
            fd.flush()
            os.fsync(fd.fileno())
        except OSError as e:
            raise RuntimeError(f"Yazma hatası: {e}")

        if verify:
           
            fd.seek(bytes_written)
            read_data = fd.read(chunk_size)
            if read_data != data:
                raise RuntimeError(f"Doğrulama hatası: beklenen desen bulunamadı (offset={bytes_written})")
            fd.seek(bytes_written + chunk_size)  

        bytes_written += chunk_size
        yield bytes_written 

def secure_wipe(fd, size, method, verify=False, progress_callback=None):
    """
    fd: açık dosya nesnesi (yazılabilir)
    size: silinecek alan boyutu (bayt)
    method: 'zero', 'random', 'dod3', 'dod7'
    verify: doğrulama yapılsın mı
    progress_callback: her ilerleme adımında çağrılacak fonksiyon
    """
    if method == 'zero':
        passes = [('zero', zero_block)]
    elif method == 'random':
        passes = [('random', random_block)]
    elif method == 'dod3':
        passes = [
            ('zero', zero_block),
            ('one', one_block),
            ('random', random_block)
        ]
    elif method == 'dod7':
       
        passes = [
            ('zero', zero_block),
            ('one', one_block),
            ('random', random_block),
            ('random', random_block),
            ('random', random_block),
            ('random', random_block),
            ('random', random_block)
        ]
    else:
        raise ValueError(f"Geçersiz silme yöntemi: {method}")

    total_passes = len(passes)
    for pass_idx, (name, pattern_func) in enumerate(passes):
        print(f"Geçiş {pass_idx+1}/{total_passes}: {name} deseni yazılıyor...")
        fd.seek(0)
        start = time.time()
        last_progress = 0
        for written in write_pass(fd, size, pattern_func, verify=verify):
            percent = (written / size) * 100
            if progress_callback:
                progress_callback(pass_idx+1, total_passes, percent)
            else:
              
                if percent - last_progress >= 10:
                    sys.stderr.write(f"\r{percent:.1f}% tamamlandı")
                    sys.stderr.flush()
                    last_progress = percent
        if not progress_callback:
            sys.stderr.write("\r%100 tamamlandı.\n")
        elapsed = time.time() - start
        print(f"Geçiş {pass_idx+1} tamamlandı. Süre: {elapsed:.2f} saniye.\n")


def wipe_file(path, method, verify):
    """Bir dosyayı siler (dosya boyutuna göre)."""
    if not os.path.isfile(path):
        raise FileNotFoundError(f"Dosya bulunamadı: {path}")

    size = os.path.getsize(path)
    print(f"Dosya: {path}, boyut: {size} bayt ({size/(1024**2):.2f} MB)")

    try:
       
        with open(path, 'r+b') as f:
            secure_wipe(f, size, method, verify)
    except Exception as e:
        raise RuntimeError(f"Dosya silinirken hata: {e}")

   
    os.remove(path)
    print(f"Dosya {path} başarıyla silindi ve kaldırıldı.")

def wipe_device(device_path, method, verify):
    """Bir blok aygıtı (örn. /dev/sdb) siler."""
    if not os.path.exists(device_path):
        raise FileNotFoundError(f"Aygıt bulunamadı: {device_path}")

   
    try:
        with open(device_path, 'rb') as f:
            f.seek(0, os.SEEK_END)
            size = f.tell()
    except Exception as e:
        raise RuntimeError(f"Aygıt boyutu alınamadı: {e}")

    print(f"Aygıt: {device_path}, boyut: {size} bayt ({size/(1024**3):.2f} GB)")
    print("UYARI: Bu işlem geri alınamaz! Devam etmek için 'yes' yazın.")
    confirm = input("> ")
    if confirm.lower() != 'yes':
        print("İptal edildi.")
        return

    try:
        with open(device_path, 'r+b') as f:
            secure_wipe(f, size, method, verify)
    except Exception as e:
        raise RuntimeError(f"Aygıt silinirken hata: {e}")

    print(f"Aygıt {device_path} başarıyla silindi.")

-
def main():
    parser = argparse.ArgumentParser(
        description="Secure Data Eraser - Güvenli veri imha aracı (Community Edition)",
        epilog="Örnek kullanımlar:\n"
               "  python secure_eraser.py --file gizli.txt --method dod3\n"
               "  sudo python secure_eraser.py --device /dev/sdb --method zero --verify\n"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--file', '-f', help='Silinecek dosya yolu')
    group.add_argument('--device', '-d', help='Silinecek blok aygıt yolu (örn. /dev/sdb)')

    parser.add_argument('--method', '-m', choices=['zero', 'random', 'dod3', 'dod7'],
                        default='dod3', help='Silme yöntemi (varsayılan: dod3)')
    parser.add_argument('--verify', '-v', action='store_true',
                        help='Her geçişten sonra yazılan veriyi doğrula (daha yavaş)')
    parser.add_argument('--version', action='version', version='Secure Data Eraser 1.0 (Community)')

    args = parser.parse_args()

    try:
        if args.file:
            wipe_file(args.file, args.method, args.verify)
        elif args.device:
          
            if os.geteuid() != 0:
                print("Blok aygıt silmek için root yetkisi gereklidir. 'sudo' ile tekrar deneyin.",
                      file=sys.stderr)
                sys.exit(1)
            wipe_device(args.device, args.method, args.verify)
    except Exception as e:
        print(f"Hata: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
