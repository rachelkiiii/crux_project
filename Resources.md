## Resources 

A. Video Resources:
Using Open BCI for data collection: https://www.youtube.com/watch?v=Dgo7F-lpyYE
B. Literature reviews: 

Rachel : https://arxiv.org/pdf/1603.02869.pdf
Low cost EEG building with a 3D printed prosthetic arm. 
Used OPENVibe platform to collect brain signals. (Open BCI seems suitable for our project)

Darren: 



https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=c8646a15245732a8f91fb74294562b99d19628df
https://www.sciencedirect.com/science/article/pii/S092523121401323X?via%3Dihub (4 degrees of movement)
https://www.sciencedirect.com/science/article/pii/B9780444639349000081?via%3Dihub#bb0220 (6 degrees of movement?)



Danielle: 

https://doi.org/10.1038/s41598-020-58097-1



Katharine:

Ben: 

Nathan:

Experiment with time-frequency, frequency, and time domain (fastest)
FFT
PCA
RNN / SVM

Shane: https://iopscience.iop.org/article/10.1088/1741-2552/abf8cb/meta

Main point of this paper is the shared control strategy, which increases the effectiveness of non-invasive EEGs. If we’re thinking about increasing the accuracy of the prosthetic arm, following this group’s method of shared control assistance with automated reach correction, grasp, and placement will help (more specifics in section 2.2.3. Shared control strategy).

https://www.nature.com/articles/srep38565#Sec17

If we’re planning on sticking with more simple movements, looking into how this group accomplished the first stage of their brain control task would be useful. It talks about how they first worked with virtual cursor movement left-right-up-down (probably also useful if we end up simplifying further and going virtual with our project). 

Ayesha: 
A Brain-Actuated Robotic Arm System Using Non-invasive Hybrid Brain-Computer Interface and Shared Control Strategy 
https://iopscience.iop.org/article/10.1088/1741-2552/abf8cb/meta 
Here, researchers used a hybrid strategy to ensure that the control of the robotic arms was better as the quality of EEG signals gleaned using non-invasive BCIs can be poor. 
85% vs 50% accuracy with pure BCI use
Shared control strategy w/ hybrid BCI improve the performance of the brain-actuated robotic arm system 
Three different shared control assist modes: reaching correction, automatic grasp, and automatic place
Shared controller decided whether or not to provide shared control assistance and what kind to provide, based on current robot position and the output commands from human and machine agents
Created regions where once the robot reached there based solely on BCI control, the machine agent would provide assistance to ensure that the performance of the robotic arm was ideal 
Did this by setting a reaching correction region, wherein when the robot reached there, the machine agent provides partial traction assistance 

Noninvasive Neuroimaging Enhances Continuous Neural Tracking for Robotic Device Control 
https://www.science.org/doi/10.1126/scirobotics.aaw6844  
Presents a framework that increased user engagement and spatial resolution of noninvasive neural data through EEG source imaging
Unable to gain access but will try to look into more later 

Review of Latest Noninvasive EEG-based Robotic Devices
https://ras.papercept.net/images/temp/AIM/files/0138.pdf 
Summarizes different methods used for BCIs and control strategies  and then speaks on the issues with current BCI-based devices and the need for evaluation by disabled users.

Noninvasive EEG Based Control of a Robotic Arm for Reach and Grasp Tasks
https://www.nature.com/articles/srep38565 
Combined two sequential low dimensional controls to have users control a robotic arm 
Dividing the reach and grasp task into two stages 
Guiding the robotic arm w/ in a 2D plane to a region above a target object 
Then if the subject selected the correct object, they were to guide the arm down in the 3D and grasp the object 
This reduced the number of DOF that the BCi need to interpret 


Nishad:

Arms: 
$50 wooden arm (laser cutters in boelter makerspace (olympic makerspace has 3D printers mostly))

$140 metal arm
$135 metal arm

Tutorial for DIY Arm

3D Printed and Wooden Materials
