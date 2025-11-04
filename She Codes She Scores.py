# description: 
from earsketch import *

setTempo(120)

#Intro - inspired by Aretha Franklin's I say a little prayer. 
#Played this piece on a midi keyboard connected to apple pro logic and exported it as a wav file to inport into earsketch. 
fitMedia(JESSICA_STRATI_CLASSICAL_PIANO_1, 5, 1,8)
fitMedia(JESSICA_STRATI_GRAND_PIANO_AND_PAD_1, 7, 1, 8)

#Verse 1 
fitMedia(AK_UNDOG_LEAD_VOCALS_BRIDGE_2, 1, 3, 4) 
setEffect(1, VOLUME, GAIN, -10) #makes vocal quieter so it fits better with the piano track
fitMedia(AK_UNDOG_PERC_TAMBOURINE_1, 3, 1, 8)
fitMedia(AK_UNDOG_CLAPS_SNAPS_1, 4, 4, 8)
fitMedia(AK_UNDOG_PAD_1, 6, 4, 5)
fitMedia(AK_UNDOG_LEAD_VOCALS_PRE_CHORUS_2, 8,5,10)
setEffect(8, VOLUME, GAIN, -5)
fitMedia(DUBSTEP_FILTERCHORD_001, 11, 9, 15) # working on a transition that incorporates new music/Dj inspired transitions to break up the heavy female vocals. 
fitMedia(AK_UNDOG_VOCAL_BELT_7, 10, 9, 13)

#chorus 
setTempo(130) #speeds up tempo 
fitMedia(AK_UNDOG_BASS_4, 34, 10, 15)
#"The makeBeat function creates a drum pattern by specifying the rhythm of a given instrument as a text string". (2022, Horn, M.S., West, M., Roberts, C.)
makeBeat(BOYKINZ_NIGHT_BEAT_TOMS_2, 13, 11, "0---0---0---0---")
makeBeat(AK_UNDOG_STRINGS, 14, 10, "0-0-0-0-0-0-0-0")

#bridge 
fitMedia(CIARA_SET_THEME_MELSYNTH, 15, 12 , 16)
setEffect(15, VOLUME, GAIN, -20) 
# Loop created here to play on repeat once the initial classical piano ceases & the vocals begin.  
for measure in range (6,10):
    fitMedia(RD_RNB_808SOLOFILL_2, 30, measure, measure + 1)
fitMedia(CIARA_ROOTED_VOX_PRECHORUS_2, 33, 13, 17)

#Outro 
for measure in range (12,18):
    fitMedia(AK_UNDOG_STRINGS, 12, measure, measure +1)
fitMedia(IRCA_BOMBA_SICA_PIANO, 21, 16, 18)
setEffect(21, VOLUME, GAIN, -10) 
fitMedia(AK_UNDOG_PAD_1,31, 17, 20)
fitMedia(JESSICA_STRATI_GRAND_PIANO_AND_PAD_1, 22, 17, 20) # Replay the grand piano keys utilised in the introduction. 
fitMedia(AK_UNDOG_VOCAL_BELT_7, 32, 19, 21) # have a clear and strong finish to the song. 

(finish)





