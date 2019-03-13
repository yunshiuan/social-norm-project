#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.6),
    on Tue Mar 12 15:05:53 2019
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.0.6'
expName = 'SocialNormsTask'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/vimchiz/GitLab_local/social-norm-project/PsychoPy_NormsTask_Run/SocialNormsTask_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "Stimulus"
StimulusClock = core.Clock()
Norm_Stimulus = visual.ImageStim(
    win=win, name='Norm_Stimulus',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "Norm_Feedback"
Norm_FeedbackClock = core.Clock()
Feedback_Question = visual.TextStim(win=win, name='Feedback_Question',
    text='default text',
    font='Arial',
    pos=(0, 100), height=0.1, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Keypad_Screen = visual.ImageStim(
    win=win, name='Keypad_Screen',
    image='Norm Feedback.jpg', mask=None,
    ori=0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "Norm_Response"
Norm_ResponseClock = core.Clock()
Stimulus_With_Norm = visual.ImageStim(
    win=win, name='Stimulus_With_Norm',
    image='PictureStimulus', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
Norm_Statistic = visual.TextStim(win=win, name='Norm_Statistic',
    text='Any text\n\nincluding line breaks',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Jitter"
JitterClock = core.Clock()
Jitter_Cross = visual.ImageStim(
    win=win, name='Jitter_Cross',
    image='images/Jitter', mask=None,
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
Norm_Trials = data.TrialHandler(nReps=72, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('NormsTaskConditions.xlsx'),
    seed=None, name='Norm_Trials')
thisExp.addLoop(Norm_Trials)  # add the loop to the experiment
thisNorm_Trial = Norm_Trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNorm_Trial.rgb)
if thisNorm_Trial != None:
    for paramName in thisNorm_Trial:
        exec('{} = thisNorm_Trial[paramName]'.format(paramName))

for thisNorm_Trial in Norm_Trials:
    currentLoop = Norm_Trials
    # abbreviate parameter names if possible (e.g. rgb = thisNorm_Trial.rgb)
    if thisNorm_Trial != None:
        for paramName in thisNorm_Trial:
            exec('{} = thisNorm_Trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Stimulus"-------
    t = 0
    StimulusClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    Norm_Stimulus.setImage('PictureStimulus')
    # keep track of which components have finished
    StimulusComponents = [Norm_Stimulus]
    for thisComponent in StimulusComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Stimulus"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = StimulusClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Norm_Stimulus* updates
        if t >= 0.0 and Norm_Stimulus.status == NOT_STARTED:
            # keep track of start time/frame for later
            Norm_Stimulus.tStart = t
            Norm_Stimulus.frameNStart = frameN  # exact frame index
            Norm_Stimulus.setAutoDraw(True)
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Norm_Stimulus.status == STARTED and t >= frameRemains:
            Norm_Stimulus.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in StimulusComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Stimulus"-------
    for thisComponent in StimulusComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "Norm_Feedback"-------
    t = 0
    Norm_FeedbackClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    Feedback_Question.setText('Any text\n\nincluding line breaks')
    Keypad_Input = event.BuilderKeyResponse()
    # keep track of which components have finished
    Norm_FeedbackComponents = [Feedback_Question, Keypad_Screen, Keypad_Input]
    for thisComponent in Norm_FeedbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Norm_Feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Norm_FeedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Feedback_Question* updates
        if t >= 0.0 and Feedback_Question.status == NOT_STARTED:
            # keep track of start time/frame for later
            Feedback_Question.tStart = t
            Feedback_Question.frameNStart = frameN  # exact frame index
            Feedback_Question.setAutoDraw(True)
        frameRemains = 0.0 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Feedback_Question.status == STARTED and t >= frameRemains:
            Feedback_Question.setAutoDraw(False)
        
        # *Keypad_Screen* updates
        if t >= 0.0 and Keypad_Screen.status == NOT_STARTED:
            # keep track of start time/frame for later
            Keypad_Screen.tStart = t
            Keypad_Screen.frameNStart = frameN  # exact frame index
            Keypad_Screen.setAutoDraw(True)
        frameRemains = 0.0 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Keypad_Screen.status == STARTED and t >= frameRemains:
            Keypad_Screen.setAutoDraw(False)
        
        # *Keypad_Input* updates
        if t >= 0.0 and Keypad_Input.status == NOT_STARTED:
            # keep track of start time/frame for later
            Keypad_Input.tStart = t
            Keypad_Input.frameNStart = frameN  # exact frame index
            Keypad_Input.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(Keypad_Input.clock.reset)  # t=0 on next screen flip
        frameRemains = 0.0 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Keypad_Input.status == STARTED and t >= frameRemains:
            Keypad_Input.status = FINISHED
        if Keypad_Input.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2', '3', '4'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                Keypad_Input.keys.extend(theseKeys)  # storing all keys
                Keypad_Input.rt.append(Keypad_Input.clock.getTime())
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Norm_FeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Norm_Feedback"-------
    for thisComponent in Norm_FeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Keypad_Input.keys in ['', [], None]:  # No response was made
        Keypad_Input.keys=None
    Norm_Trials.addData('Keypad_Input.keys',Keypad_Input.keys)
    if Keypad_Input.keys != None:  # we had a response
        Norm_Trials.addData('Keypad_Input.rt', Keypad_Input.rt)
    
    # ------Prepare to start Routine "Norm_Response"-------
    t = 0
    Norm_ResponseClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    Norm_ResponseComponents = [Stimulus_With_Norm, Norm_Statistic]
    for thisComponent in Norm_ResponseComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Norm_Response"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Norm_ResponseClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Stimulus_With_Norm* updates
        if t >= 0.0 and Stimulus_With_Norm.status == NOT_STARTED:
            # keep track of start time/frame for later
            Stimulus_With_Norm.tStart = t
            Stimulus_With_Norm.frameNStart = frameN  # exact frame index
            Stimulus_With_Norm.setAutoDraw(True)
        frameRemains = 0.0 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Stimulus_With_Norm.status == STARTED and t >= frameRemains:
            Stimulus_With_Norm.setAutoDraw(False)
        
        # *Norm_Statistic* updates
        if t >= 0.0 and Norm_Statistic.status == NOT_STARTED:
            # keep track of start time/frame for later
            Norm_Statistic.tStart = t
            Norm_Statistic.frameNStart = frameN  # exact frame index
            Norm_Statistic.setAutoDraw(True)
        frameRemains = 0.0 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Norm_Statistic.status == STARTED and t >= frameRemains:
            Norm_Statistic.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Norm_ResponseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Norm_Response"-------
    for thisComponent in Norm_ResponseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "Jitter"-------
    t = 0
    JitterClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    JitterComponents = [Jitter_Cross]
    for thisComponent in JitterComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Jitter"-------
    while continueRoutine:
        # get current time
        t = JitterClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Jitter_Cross* updates
        if t >= 0.0 and Jitter_Cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            Jitter_Cross.tStart = t
            Jitter_Cross.frameNStart = frameN  # exact frame index
            Jitter_Cross.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in JitterComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Jitter"-------
    for thisComponent in JitterComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Jitter" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 72 repeats of 'Norm_Trials'

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
