---
title: Audacity Audio Post Processing  
description: Mike Russel's Guide made simple of "5 Easy Steps for Sounding Better in Audacity"
date: 2026-01-10 05:00:00 -0500  
categories: []  
tags: [audio-editing, audacity, sound-improvement, tutorial, audio-processing]  
pin: false  
math: true  
mermaid: true
assets: assets/2026-01-10-Audacity-Audio-Post-Processing.jpg  
---
This is Mike Russell's Video "5 EASY Steps For Sounding Better in Audacity". However, I want it formatted for myself and slightly easier to read.
The fomat is ENCNL.

1. Equalize

    - Effect > EQ and Filter > Filter Curve EQ
    - Lows: Drop -18db from 100hz to 60z
    - Mid-Range: Peak at 200hz of 1.5db. Rounding from 100hz-300hz
    - Nasal: Drop -1.5db at 1000hz. Round from 600hz-2000hz
    - Highs: Increase 6db from 400hz to 6100 hz

    Effect > EQ and Filter > Filter Curve EQ > Presets & settings > Import this below as a text file

    ```txt
    FilterCurve:f0="59.249598" f1="98.876258" f2="137.07937" f3="198.621" f4="295.5167" f5="999.43922" f6="3997.4965" f7="4984.8605" FilterLength="8191" InterpolateLin="0" InterpolationMethod="B-spline" v0="-40.151863" v1="-0.060172081" v2="1.7621775" v3="1.9140396" v4="-0.060172081" v5="-1.5787964" v6="-0.060172081" v7="6.1661892"
    ```

2. Normalize
Effect > Volume and Compression > Normalize
Peak Amplitude to -1dB

3. Compress
Effect > Volume and Compression > Compressor
Threshold: -20db
Make-up gain: 3db
Knee Width: 5db
Ratio: 2 (I use this for Podcast Audio)

4. Normalize
Effect > Volume and Compression > Normalize
Peak Amplitude to -1dB

5. Limiter
Effect > Volume and Compression > Limiter



You can also [support Mike Russell](https://musicradiocreative.com/search?type=product&q=audacity*) by buying the preset that he has probably better fine tuned.
- His blog: [https://producer.musicradiocreative.com/5-steps-to-sound-better/](https://producer.musicradiocreative.com/5-steps-to-sound-better/)
- His video: [https://www.youtube.com/watch?v=WsmMMKRZp5g](https://www.youtube.com/watch?v=WsmMMKRZp5g)

For fading: Effects > Fading > Adjustable Fade > Fade Up, % of Original, Start = 0, End = 30