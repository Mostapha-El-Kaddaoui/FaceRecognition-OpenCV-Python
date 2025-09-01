# Face Recognition for Class Presence Logic

Ce projet a été créé en 2024. Il s'agit d'un système de **prise de présence par reconnaissance faciale en temps réel** développé en Python, OpenCV et avec la bibliothèque `face_recognition`. Il permet d'identifier les étudiants via une webcam, de marquer leur présence et de distinguer les étudiants présents des absents.

## Features
- Détection et reconnaissance faciale en temps réel via webcam.
- Supporte plusieurs visages connus avec des images préchargées.
- Marque automatiquement les étudiants comme présents lorsqu'ils sont reconnus.
- Suit les absents à la fin de la session.
- Utilise le multithreading pour un traitement plus rapide des frames.
- Affiche les visages reconnus avec les noms dans le flux vidéo en direct.

## Requirements
- Python 3.8+
- OpenCV (`cv2`)
- face_recognition
- numpy
- dlib (nécessaire pour face_recognition)

## How It Works
1. Le système charge les images des étudiants connus et génère leurs encodages faciaux.
2. La webcam commence à capturer les frames vidéo en temps réel.
3. Toutes les quelques frames, le système détecte les visages présents et les compare aux encodages connus.
4. Si une correspondance est trouvée, le nom de l’étudiant est affiché et il est marqué comme présent.
5. Lorsque le programme est arrêté (touche `q`), il affiche les listes :
   - Tous les étudiants
   - Étudiants présents
   - Étudiants absents


![Face Recognition](./face-rec.png)
---
Copyright © 2024, All Rights Reserved For ELKADDI-Solutions


