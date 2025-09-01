Maritime Radio Historical Society
=================================

Enigma crypto transmission from KPH coastal radio station
---------------------------------------------------------

On 2025-08-30 at 20:00 UTC, radio station [KPH](https://www.radiomarine.org) on the coast of Northern California transmitted an [Enigma](https://cipherhistory.com)-encoded radio transmission; a fragment related to <details><summary>(spoilers!)</summary>[Operation Sea Lion](https://en.wikipedia.org/wiki/Operation_Sea_Lion)</details>.

I attempted to capture and decrypt the transmission; this was my second time participating in one of these cryptography-related events hosted by the MRHS.

This repository documents the process that I followed, and the results.

Capturing the transmission
--------------------------

The first, and perhaps most important, part of the decryption process is to ensure that we have a copy of the encrypted message that was transmitted.

For this event, the precise time, location, and radio frequencies to tune into were published by MRHS.

However, these transmissions do not tend to [propagate](https://en.wikipedia.org/wiki/Radio_propagation) to my home in Edinburgh, UK.  In future perhaps I'll try to co-ordinate with friends elsewhere for the transmission capture step, but this time I used KPH's convenient [WebSDR service](https://www.radiomarine.org/kph-sdrs) to tune into the message.

I use [Debian Linux](https://www.debian.org) on my laptop computer, in combination with the [GNOME](https://www.gnome.org) desktop environment - and by default the Debian distribution uses an audio processing engine called [PipeWire](https://www.pipewire.org/) on the desktop.

Although there may be more advanced/precise ways to achieve the audio capture, I used a command-line tool called `pw-record` to record a PCM Wave audio file directly from the running system while I had the KPH WebSDR webpage open in the Firefox web browser.  This meant that I could listen to the output from my laptop while simultaneously writing an audio recording to the computer's filesystem.

A [BZIP2](https://en.wikipedia.org/wiki/Bzip2)-compressed copy of the transmission that I captured that spans the 20:00 UTC transmission is included in [this GitHub repository](https://github.com/jayaddison/mrhs-kph-enigma-decode).

First decoding stage: from Morse Code to a character stream
-----------------------------------------------------------

The rapid series of dits and dots heard when the `2000Z.pcm` audio file is played are [Morse Code](https://en.wikipedia.org/wiki/Morse_code).

I'm not familiar enough with morse code to be able to decode Morse Code by ear, even at fairly slow rates and without time pressure.  So for this challenge, I opted to use an open source utility called `multimon-ng`, available as a Debian package, that can decode various types of radio transmission, including Morse.

The command to do this, and the output that appears, is shown below:

```sh
$ multimon-ng -a MORSE_CW -t wav 2000Z.pcm 
multimon-ng 1.3.1
  (C) 1996/1997 by Tom Sailer HB9JNX/AE4WA
  (C) 2012-2024 by Elias Oenal
Available demodulators: POCSAG512 POCSAG1200 POCSAG2400 FLEX FLEX_NEXT EAS UFSK1200 CLIPFSK FMSFSK AFSK1200 AFSK2400 AFSK2400_2 AFSK2400_3 HAPN4800 FSK9600 DTMF ZVEI1 ZVEI2 ZVEI3 DZVEI PZVEI EEA EIA CCIR MORSE_CW DUMPCSV X10 SCOPE
Enabled demodulators: MORSE_CW
VVV VVV VVV DE KPH KPH KP5 NESX 4/6/8/12/16/22 OBS? ANVER? QRU? ANS 500/HF ITSI CH3 + K T IE CEK CTKKTKDE KPHE KPH KANH ENITNEKTEST EKSAT <.._...>UM<...._.>/ HP = E CQ CQ CQ DE KPS KPH NPH CG CQ CNA DE KPIE KPH KGH ENIGMA MESSAGE FOL<._...>OWS DEQ CQ ERQ DE KPH KPH KPH CQ CQ FQ DE KPH KPEI KPH ENIGMA MESSAGE FÖBLOWS <..._..>KAPT REINEKE FROM ADM RAEDER 231HM MAY Ü7 = <___..>20 = JXY LYI = BSTHH GTEBOA WM OCL FNCYT VNUHDB TIAUJ ILIRX NKQWV HVTXM VJGCF ZYUGP ZBDZW VLQFR ODBN C PPBDK XBWTZ MXKGP JAFKA QKKFU UULYV WXSZK DUFXW FZOFT QXKFS REPEAT KAPT REINEKE FROM ADM RAEDER EÜ312 MAY 27 = 120 = JXY LYI = BSTHH GMBOA WGOCL FRCYT VQHDB TIAUJ ILAR<...._.>NKQWV HVTXM VJGCF ZYUGP ZBBZW VLQFR ODBBC PPBTEK XBWTZ MXKGP JAFKA QKKFU UULYV WXUZK DUUXW FZOFT QVKFS END OF ENIGMA MEHSAGE VY 73 ES GR DE KPH SÄ <..._..._>V VVV VVIDE KPH KPS KPH QSX ST/6/8/J 2/16/2<_.._..>OBS? AMVEREZ QRU? ANS 500/HF ITU CH3 + B
```
