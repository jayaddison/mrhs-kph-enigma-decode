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
