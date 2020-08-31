## Simple Pause with orientation plugin for Craftbeerpi

This simple plugin allows you to include a pause step with some orientation like to manually do something, a timer to wait for the manual action and the automatic move to next step after time elapses.

If you cloned the original plugins repoisitory of Crafbeerpi (https://github.com/Manuel83/craftbeerpi-plugin) and followed ths instructions in my fork(https://github.com/MarcioMonego/craftbeerpi-plugins) then you can find the plugin in addon list of Craftbeerpi.  

![Plugin Selection](/images/PauseStepAddOn.png)
Just download it.

If you don't want to clone it just to add a single addon then:
Create a new folder under `\modules\addons` named `PauseStep` and put the files of this repo inside it or do a git clone under it

### To use it just add a new step: 

    Choose PauseStep from step type
    Optionally include an orientation message: Like separe x liters of water to sparge
    Define the timer to stay in pause
    Optionally include the title to be showed of orientation message (the one that appears on notification header)

### Example:   
![Step Configuration](/images/PauseStepConfiguration.png)

It's finished.
When the process is running Craftbeerpi will start the timer, open a notification on the screen, if the orientation message was filled it will be shown as a notification.
After the time has elapsed the process automatically moves forward.

### Step into the recipe   
![Step Configuration](/images/PauseStepInfo.png)

### Step running with notification  
![Step Configuration](/images/PauseStepRunning.png)