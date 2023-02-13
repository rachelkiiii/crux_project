# Crux Team 5 Proposal

## Prosthetic arm controlled by human brain

***Team Lead: Rachel K.***

***Team Members: Nathan C., Shane C., Nishad E., Ben F., Danielle F., Katharine J., Ayesha M., Darren N.***

## Table of contents
1. Narrative
2. Specific Aims
3. Research Strategy 
    A. Data Collection
    B. Signal Processing
    C. Robotics
4. References Cited

### Concept Map
<img width="260" alt="Screen Shot 2023-02-12 at 4 24 28 PM" src="https://user-images.githubusercontent.com/114251753/218346392-7fd34828-4542-419e-93c9-706ec1cc8eb8.png">

### Data Flow Diagram
<img width="586" alt="Screen Shot 2023-02-12 at 4 25 48 PM" src="https://user-images.githubusercontent.com/114251753/218346457-5eaaa9cd-5d9d-481a-b194-0ccff8bc0a27.png">

#### 1. Narrative
Robotic arms are needed for some individuals who suffer from physical disabilities with the lost ability to freely control their muscles. Although there are robotic arms that are already developed for use, it is crucial for further study and development of prosthetic arms for advancement of robotic arms with a reasonable cost for people in need. In this research, we will demonstrate moving a prosthetic arm controlled by the human brain through BCI (Brain Computer Interface). BCI is based on electroencephalography (EEG), which uses electrical brain activity using small electrodes attached to the scalp.

#### 2. Specific Aims
We propose a method that will enable the movement of a simplified robotic arm using EEG signals. Usual costs for prosthetic arms in current use range at least a couple thousand dollars because of the high costs of maintenance and materials used such as titanium and carbon fiber. Our robotic arm will minimize such costs with the use of affordable materials such as wood. We specifically will focus on left-right and up-down movement, but if time allows, we will develop a hand that grasps objects. We will use keylogging software to accurately measure and separate the interval times for each left-right and up-down event. Greater accuracy with this four directional movement will be achieved by having subjects use different concentration tasks (e.g. mentally reciting numbers or alphabet backwards) for the up-down movement.
Our goals include:
    - **Accurately obtain data through an OpenBCI headset**: We will use an OpenBCI headset that has at least 8 electrodes for data collection and OpenBCI to visualize signals. While collecting data, to maximize obtaining clean signals, we will reduce unnecessary movements and noises. We will use two strategies for collecting data, one is from a software that we can use keys to record left and right arm movements using the left/right keys. The second strategy is to use an image stimulus of up and down after two seconds of a beep noise. We might have to use both hands due to our restricted number of electrodes (16 needed for one hand up and down movements). Our goal is to obtain signals from 5 subjects with 3 sessions for each subject and 160 trials per session. 
    - **Clean and filter signals so that we can obtain meaningful signals in the correct frequency range**: We will disregard the buffer areas of the signals and Independent Component Analysis (ICA) based algorithm to clear up the data. We will be using the channels C3 and C4 for our analysis. For C3 we will be using the difference between F3 and P3, and for C4 we will be using the difference between F4 and P4. We will also use a bipolar montage to obtain meaningful signals. The code will be stored in github.
    - **Classify and reduce dimensionality of the cleaned data to obtain an accuracy rate over 80%**: We will overcome getting a higher accuracy by going step by step on each dataset. We will use an 80/20 train-test split for our data to obtain the accuracy. Left and right movements data first, then up-down, then grasping an object. This would allow us to work on each dataset and higher the accuracy rate through modification. To overcome computation times, we might use PCA dimensionality reduction. 
    - **Build a cost-effective two prong hand/prosthetic arm with wood and 3D printer**: To build a cost-effective prosthetic hand, we will use a 3D printer and wood. We will be building the arm in Boelter hall makerspace, or in a study room if we have the tools.
    - **Use a prosthetic arm for left/right and up/down movements and grasping objects**: With 3 motors, we would be able to make a prosthetic arm robot that would be able to do left/right, up/down and grasping movements.

#### 3. Research Strategy

   ***A. Data Collection***
   
   Our goal is to examine individual patients in depth rather than superficially observe many people. Ideally, we would test each subject for around 2 hours. We would limit testing to one subject per day to allow enough time for setup, briefing, consent and cleanup.
We will keep good practice while collecting data; subjects will be tested in a quiet environment with minimal noise and movement. We will control our position and mood as much as possible. We will ensure minimal data artifacts by annotating trials which include actions such as blinking, head jerks, clenching, etc. 
There will be two ways to collect data. The first way is using a simple interface for users where the screen prompts left/right motion and records ensuing keystrokes (the code for the software is here: https://github.com/rachelkiiii/crux_project/blob/main/simple_motion_gui.py). The person will imagine a left movement while pressing the left button, and right motion for the right button. For grasping motion, we will use a different key to record data. This will increase the effectiveness of the data since we will be getting data at the exact time stamp when the user pressed the keys. Since up/down motion requires a different set of data, we will be using a different way to collect these data sets.

<img width="396" alt="Screen Shot 2023-02-12 at 4 32 25 PM" src="https://user-images.githubusercontent.com/114251753/218346822-2e894dc7-8f10-4057-84f0-095f6e4edf3f.png">

For the second way, each trial will display a fixation cross in the center of a monitor. As shown in the image above, after two seconds give a warning stimulus in the form of a "beep“. From second 3 until 4.25 show an arrow (cue stimulus), pointing up and down on the screen. Instruct the subject to imagine an up and down hand movement, depending on the direction of the arrow. (Note: the imagery used by participants does not reflect a natural muscle movement, although it provides a viable decoding strategy. We might have to use both hands up and down to collect data. And 3 dimensional movement will require more time as participants need to learn how to modulate the amplitude of specific frequency bands). Between second 4.25 and 8 classify the EEG on-line and use the classification result to control the prosthesis. If the person imagines up movement, then have the prosthesis move to the up and vice versa (correct classification assumed). Have each session consist of 160 trials. Aim to have three sessions per subject, beginning with one subject. 

There are two options for adding additional degrees of freedom to the arm. The first way would be to have the mental imagery of moving both left and right hands represent one movement of the robotic arm, and the relaxation of both hands be the last movement. This could correspond to up and down movements of the arm, respectively. The second option would require the utilization of the 16 electrodes Fz, FC5, FC1, FCz, FC2, FC6, C3, Cz, C4, CP5, CP1, CP2, CP6, P3, Pz and P4 that include the motor function area and close to the Wernicke area. The procedure can be the same as in the first experiment but this time the subject engages in mental recitation of the alphabet backwards to move the arm down, and a mental countdown from 20 to 0 to move it up. On paper it would be more convenient to use the first method because it does not require as many electrodes, but we will have to choose based on which mental tasks give us sufficiently discernable signals.

Programming the arm to have more than 4 degrees of freedom can be accomplished using a time delay, and switching one of the previously explained mental tasks to dictate a new movement. For example, the up/down action can be replaced with open/close motion of the palm once the arm is positioned over its target for 2 seconds. 


   ***B. Signal Processing***
   
For signal processing, the coding will be done with python. We will take the EEG data collected from each subject and parse it into distinct events for each motor movement (left/right, up/down, grasping). We will discard all buffer periods and pauses in between events.
Then, we will clean the data. This will include passing each channel through an ICA-based algorithm. If any particular channel is noisy or contains artifacts, it will be discarded.

Then we will apply a bipolar montage to further extract meaningful signals. This means that we will calculate the difference between two neighboring channels in order to find out which signal features are most important.
We will be using the channels C3 and C4 for our analysis. For C3 we will be using the difference between F3 and P3, and for C4 we will be using the difference between F4 and P4.

After this we will pass each event through a Morlet filter, which will reshape the signals into a frequency time domain. We will be separating the epoch into a frequency range of 4-30 Hz.

We will then log all of the values across all of these time frequency decompositions. After this, we will calculate a z-score based on frequency bands between left-right signals. A detailed explanation is below:

Calculate the average value of each row of each event, for all events for a subject. Calculate the standard deviation between these averages. Calculate the z-score based off of these values for all frequencies 4-30 Hz.

After this step, we will average our events across time. We will end this step of signal processing with a set of 26x1 arrays, each corresponding to an event of left/right motion. Each value in each array will denote a frequency from 4-30 Hz.

For training, we will use a 80-20 train-test split for our data. We will experiment with running the data through PCA since dimensionality reduction, in theory, leads to increased discriminative power as well as faster computation times. If we do this, we will run the training data and the test test data through PCA separately to minimize the possibility of introducing bias into our classification algorithm.

However, dimensionality reduction is complicated by our plan to use an SVM classifier. The use of a non-linear kernel in SVM transforms the data into a higher-dimensional feature space in an effort to compute a more effective decision boundary. As one can imagine, this somewhat counter-intuitive process of dimensionality reduction followed by a dimensionality increase can lead to mixed results, which is currently an active field of research. Our target classification accuracy will be above 80% for all subjects.

 
   ***C. Robotics***

We will use a translational algorithm using the processed signals and the established action threshold for the robotic arm. This algorithm will utilize the SVM classified signal and generate instructions for each task. These instructions will be executed by the terminal, Raspberry Pi, which is a great choice when coding with python language.  

<img width="260" alt="Screen Shot 2023-02-12 at 4 34 23 PM" src="https://user-images.githubusercontent.com/114251753/218346924-b0f20724-2baf-4ee2-9ce3-bd17dcb9114b.png">

For the robotic arm itself, we plan to make it using wood and a 3D printer. This allows for the prosthetic arm to be cheaper, and therefore more accessible. Additionally, the design of the hand will be more simple - a “two-prong hand”- that will be able to grasp objects, but will not necessarily look like a traditional prosthetic hand. This arm will have 2 degrees of freedom (DOF), and three motors. Typically, the number of motors is equivalent to the DOF. However, in this case, the third motor will cause the “two-prong” hand to grasp, and does not allow for any increased movement (translational or rotational). 

<img width="342" alt="Screen Shot 2023-02-12 at 4 35 13 PM" src="https://user-images.githubusercontent.com/114251753/218346976-464c5edc-5048-4b62-a081-374ecac50247.png">

Additionally, this arm will only be able to grasp things within reach, it will not be able to extend to grasp objects. As shown in image 3, since the data collection was made in a certain range of a rectangle, we would be able to move the arm at the range of the rectangle. Motor 1 in image 2 will allow the arm to move up and down. Motor 2 will rotate the base, thus allowing for the arm to move right and left. Finally, motor 3 will allow for the hand to grasp onto objects.

#### 4. References Cited

- Prosthetic Control by an EEG-based BrainComputer Interface (BCI) https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=c8646a15245732a8f91fb74294562b99d19628df
- SVM-based Brain–Machine Interface for controlling a robot arm through four mental tasks https://www.sciencedirect.com/science/article/pii/S092523121401323X?via%3Dihub 
- Applications of brain-computer interfaces to the control of robotic and prosthetic arms https://www.sciencedirect.com/science/article/pii/B9780444639349000081?via%3Dihub#bb0220 
- Neural Representation of Observed, Imagined, and Attempted Grasping Force in Motor Cortex of Individuals with Chronic Tetraplegia https://doi.org/10.1038/s41598-020-58097-1
- A brain-actuated robotic arm system using non-invasive hybrid brain–computer interface and shared control strategy https://iopscience.iop.org/article/10.1088/1741-2552/abf8cb/meta
- A brain-actuated robotic arm system using non-invasive hybrid brain–computer interface and shared control strategy https://www.nature.com/articles/srep38565#Sec17
- A Brain-Actuated Robotic Arm System Using Non-invasive Hybrid Brain-Computer Interface and Shared Control Strategy https://iopscience.iop.org/article/10.1088/1741-2552/abf8cb/meta 
- Noninvasive Neuroimaging Enhances Continuous Neural Tracking for Robotic Device Control https://www.science.org/doi/10.1126/scirobotics.aaw6844  
- Review of Latest Noninvasive EEG-based Robotic Devices https://ras.papercept.net/images/temp/AIM/files/0138.pdf 
- Noninvasive EEG Based Control of a Robotic Arm for Reach and Grasp Tasks https://www.nature.com/articles/srep38565 
- 3D printed and Wooden Materials
https://drive.google.com/drive/folders/0B77d7bcO_gwvfjcya3lfZXQxaVNXX2RGalRaai1YZ3Vja3JjNzdFNG1SLXJVcEE2MEdkTVk?resourcekey=0-1PHFgg39DJxGQgqoX52uCA
- Tutorial for DIY Arm: 
https://www.instructables.com/DIY-Robotic-Arm/


