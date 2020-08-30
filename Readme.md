## Simple Pause with orientation plugin for Craftbeerpi

This simple plugin allows you to include a pause step with some orientation like to manually do something, a timer to wait for the manual action and the automatic move to next step after time elapses.

#### To use it just add a new step:
    Choose PauseStep from step type
    Optionally include an orientation message: Like separe x liters of water to sparge
    Define the timer to stay in pause
    Optionally include the title to be showed of orientation message (the one that appears on notification header)

It's finished.
When the process is running Craftbeerpi will start the timer, open a notification on the screen, if the orientation message was filled it will be shown as a notification.
After the time has elapsed the process automatically moves forward.
