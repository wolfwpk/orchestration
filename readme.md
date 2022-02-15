#### Orchestration System

For the convenience of the artists to modify and improve their piano music before projective orchestration, save composer of time and effort, and help non-professional individuals try orchestral music creation, I developed a music generation system based on Deep Neural Networks, which can return the harmonious combination of orchestral according to the piano input. This system can help the composer complete projective orchestration. 



#### Demo 

`input_piano_clip.mid` :  Input from front-end 

`generated_orchestraion_clip.wav`  :  Output orchestration audio returning to front-end



#### Environment Requirement

Python 3.7

Flask

Magenta ( not Magenta.js)

Due to Github storage limited, check point has been ignored, download "all_instruments" checkpoint and put in /ckpt to recover: https://storage.googleapis.com/magentadata/models/gansynth/all_instruments.zip