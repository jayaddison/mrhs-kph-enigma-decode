# Adapted from example1.py in the python3-enigma Debian (trixie) package

# Morse-decoded ciphertexts (some transmission/decoding errors occurred between these repeats, highlighted below)
# BSTHH GTEBOA WMOCL FNCYT VNUHDB TIAUJ ILIRX        NKQWV HVTXM VJGCF ZYUGP ZBDZW VLQFR ODBNC PPBDK  XBWTZ MXKGP JAFKA QKKFU UULYV WXSZK DUFXW FZOFT QXKFS
# BSTHH GMBOA  WGOCL FRCYT VQHDB  TIAUJ ILAR<...._.> NKQWV HVTXM VJGCF ZYUGP ZBBZW VLQFR ODBBC PPBTEK XBWTZ MXKGP JAFKA QKKFU UULYV WXUZK DUUXW FZOFT QVKFS
#          ___  _     _     __              _                                  _            _     __                                  _     _

ciphertext = "".join("GMBOA WGOCL FRCYT VQHDB TIAUJ ILARX NKQWV HVTXM VJGCF ZYUGP ZBBZW VLQFR ODBBC PPBDK XBWTZ MXKGP JAFKA QKKFU UULYV WXUZK DUUXW FZOFT QVKFS".split())

from enigma.machine import EnigmaMachine

machine = EnigmaMachine.from_key_sheet(
       rotors='II I IV',
       reflector='B',
       ring_settings=[3, 7, 9],
       plugboard_settings='BR CS DJ ET FO GH LZ MP NV QW')

# set machine initial starting position
machine.set_display('JXY')

# decrypt the message key
msg_key = machine.process_text('LYI')

# decrypt the cipher text with the unencrypted message key
machine.set_display(msg_key)

plaintext = machine.process_text(ciphertext)

print(plaintext)
