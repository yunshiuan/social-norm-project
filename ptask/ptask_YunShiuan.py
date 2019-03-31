'''
# Author: Chuang, Yun-Shiuan (Sean)
# Date: 2019/03/29
# Note:
# (1) Testing and commenting the codes based on "testCode.py"
# (2) Modify the file for the social-norm task
'''
# Overview of the task:
# (1) MESSAGE TASK for SES Persuasion Study
# (2) Timings:
#   Message   5 secq
# (3)
# In the social norms code, we need to run 72 loops of this sequence: 
# Each run has 36 trials
#-- fixation cross (1-5 seconds)
#-- image1 (3 seconds)
#---- trials: 72 (18 Future/Gain + 18 Future/Loss + 18 Present/Gain + 18 Present/Loss)
#-- Feedback -- button box feedback  "Do you practice [norm]?" with a 1-4 Likert scale (2 seconds)
#-- image2 (3 seconds) 
# Import modules
import csv #imports excel .csv files
from psychopy import visual, core, event, gui, data, logging # imports libraries from psycho py
import datetime
import random
import sys




#################### Constants ####################
#-Parameters
# Switch to TRUE for real session 
# (note that when using the fullscreen, it is hard to abort the sesion)
USE_FULL_SCREEN = False 
FRAME_RATE = 1
MESSAGE_DUR = 3 * FRAME_RATE # message time
RATING_DUR = 2 * FRAME_RATE # rating time
FIXATION_DUR = 1.5 # pre-task fixation (the fixation between trials is a random int between 1 and 5)
BUTTON_LABELS = { '1': 0, '2': 1, '3': 2, '4': 3 }
BUTTONS = BUTTON_LABELS.keys()
INSTRUCT_DUR = 8 * FRAME_RATE

#-Path
# #Change working directory to where the script locates
import os
os.getcwd()
PATH_ROOT = '/Users/vimchiz/GitLab_local/social-norm-project/ptask'
os.chdir(PATH_ROOT)

#-File
#This could be adjusted according to the number of stimulus
FILE_STIMULI_LIST = 'stimuli.csv' 

#################### Set up Environment ####################

# get subjID
subjDlg = gui.Dlg(title="HMS Messages Task")
subjDlg.addField('Enter Subject ID:')
subjDlg.show()

if gui.OK:
    # This will save the key-in value to subj_id
    subj_id=subjDlg.data[0]
else:
    sys.exit()

# The csv file to write (e.g., log.001.csv)
log_filename = 'logs/%s.csv' % subj_id

run_data = {
    'Participant ID': subj_id,
    'Date': str(datetime.datetime.now()),
    'Description': 'HMS Message Task'
}

# Set up window
# use the unit 'deg' (see: https://www.psychopy.org/general/monitors.html)
win = visual.Window([1024,768], fullscr=USE_FULL_SCREEN, monitor='testMonitor', units='deg')

# Define Stimulus
ready_screen = visual.TextStim(win, text="Ready.....", height=1.5, color="#FFFFFF")
fixation = visual.TextStim(win,text='+', height=5, color="#FFFFFF") # Cross Fixation

# Message screen
#             IMAGE
#            message (no message needed, we are using pictures with messages)

#visual.ImageStim inherits the unit from "visual.Window (i.e., 'deg'")
pictureStim_image1 = visual.ImageStim(win, pos=(0,6.5), size=(18,10)) 
pictureStim_image2 = visual.ImageStim(win, pos=(0,0), size=(36,20))
#  Response screen
#           IMAGE (don't need)
#        message (don't need)
#       rating scale
#     1       2       3       4
#   not                       effective
#  effective

rate1 = visual.TextStim(win,text='1', color="#FFFFFF", pos=(-8,-4))
rate2 = visual.TextStim(win,text='2', color="#FFFFFF", pos=(-3,-4))
rate3 = visual.TextStim(win,text='3', color="#FFFFFF", pos=(3,-4))
rate4 = visual.TextStim(win,text='4', color="#FFFFFF", pos=(8,-4))
ratingStim = [rate1, rate2, rate3, rate4]

anchor1 = visual.TextStim(win, text='Never', color="#FFFFFF", pos=(-8,-6))
anchor4 = visual.TextStim(win, text='Very\nOften', color="#FFFFFF", pos=(8,-6))

# instrcution screen
#instruction_image = visual.SimpleImageStim(win,image="buttonpad.png",pos=(-1,-3.5))
instruction_text = visual.TextStim(win,height=1.3,color="#FFFFFF",
text="Please view each message carefully. \n\nThen use the keypad to indicate how often you practice the activity. ",
    pos=(0,+5))


test_instructions = visual.TextStim(win, text='', pos=(0,4), height=1.2, wrapWidth=20)

#lower = visual.TextStim(win, text='Button 1 = Reduce volume', pos=(0,1))
#higher = visual.TextStim(win, text='Button 2 = Increase volume', pos=(0,-1))
#ok = visual.TextStim(win, text='Button 4 = Volume is good', pos=(0,-3))
stimuli = [i for i in csv.DictReader(open(FILE_STIMULI_LIST,'rU'))]

# Randomize the order of stimuli (an OrderedDict)
random.shuffle(stimuli)

# set up trial handler
# two runs, each with 36 trials
runs = [[],[]]

for i in range(len(stimuli)):
    # half of trials for the first run
    if i<=len(stimuli)/2:
        runs[0].append(stimuli[i])#
    # half of trials for the second run
    else:
        runs[1].append(stimuli[i])

# The fixation durations are random integers between 1 and 5
fixations = [[], []] 

for j in range(len(stimuli)):
    #random fixation times
    
    # half of trials for the first run
    if j<=len(stimuli)/2:
        fixations[0].append(random.randint(1,5))
    # half of trials for the second run
    else:
        fixations[1].append(random.randint(1,5))

# print(fixations)


################

# setup logging #

log_file = logging.LogFile("logs/%s.log" % (subj_id),  level=logging.DATA, filemode="w")
globalClock = core.Clock()
logging.setDefaultClock(globalClock)

# def do_sound_test():
#     timer = core.Clock()
#     test_message_text = '''blah'''

#################### Specify the do_run() function ####################

def do_run(run_number, trials):
    timer = core.Clock()
    ##############################
    # 1. display ready screen and wait for 't' to be sent to indicate scanner trigger
    ready_screen.draw()
    # Change to the next slide
    win.flip() #showing "Ready"
    # wait until the key 't' appears
    event.waitKeys(keyList='t') 
    # reset globalClock
    globalClock.reset()
    # send START log event
    logging.log(level=logging.DATA, msg='******* START (trigger from scanner) - run %i *******' % run_number)

    ################

    # SHOW INSTRUCTIONS

    ################

    timer.reset()

    #Change to the next slide:
    # - "Please review..." for "INSTRUCT_DUR" (8s)
    while timer.getTime() < INSTRUCT_DUR:
        instruction_text.draw()
        win.flip() 


    timer.reset()
    #Change to the next slide:
    # - "pre-task fixation" for "FIXATION_DUR" (1.5 s)
    while timer.getTime() < FIXATION_DUR:
        fixation.draw()
        win.flip()


    ################

    # MAIN LOOP
    # present trials
    for tidx, trial in enumerate(trials.trialList):
        # Set up local parameters--------------------------------
        # Image 1---------------------
        trial_type = trial['type']
        theme = trial['theme']
        cond = trial['cond']
        image = "images/image1/%s/%s_%s.png" % (cond, theme, trial_type)
        pictureStim_image1.setImage(image)
        # send MESSAGE log event
        logging.log(level=logging.DATA, msg="MESSAGE: %s - %s - %s" % (cond, theme, trial_type))
        trials.data.add('stim_onset', globalClock.getTime())
        timer.reset()
        #Change to the next slide:---------------------------------
        # - "trial picture" for "MESSAGE_DUR" (3s)
        while timer.getTime() < MESSAGE_DUR:
            pictureStim_image1.draw()
            win.flip()

        # send SHOW RATING log event
        logging.log(level=logging.DATA, msg="SHOW RATING")
        trials.data.add('resp_onset', globalClock.getTime())

        # clear event buffer
        event.clearEvents()
        resp_onset = globalClock.getTime()

        #Change to the next slide:---------------------------------
        # - trial picture along with"rating" for "RATING_DUR" (2s)
        # show rating and collect response
        timer.reset()
        while timer.getTime() < RATING_DUR:
            # draw the trial picture
            pictureStim_image1.draw()
            
            # draw the rating scale and anchors
            for rate_stim in ratingStim:
                rate_stim.draw()
            anchor1.draw()
            anchor4.draw()
            # Show the rating stimulus
            win.flip() 
            # get key response
            resp = event.getKeys(keyList = BUTTONS)
            # the case when the subject did press a button
            if len(resp) > 0 :
                # get the first button response
                resp_value = resp[0]
                # Mark the pressed value as red 
                # (will be shown at the next win.flip())
                ratingStim[BUTTON_LABELS[resp_value]].setColor('red')
                
                # Logging: add response value to the trial handler logging
                trials.addData('resp',resp_value)
                trials.addData('rt', globalClock.getTime() - resp_onset)
        # End of the rating slide
        
        #Change to the next slide:---------------------------------
        # - image2 (3s)
        # show rating and collect response
        image2 = "images/image2/image_in_progress.png"
        pictureStim_image2.setImage(image2)
        timer.reset()        
        while timer.getTime() < MESSAGE_DUR:
            pictureStim_image2.draw()
            win.flip()
        
        # Reset rating number color
        for rate in ratingStim:
            rate.setColor('#FFFFFF')
        # ------------ FIXATION ------------
        # logging: send FIXATION log event
        logging.log(level=logging.DATA, msg='FIXATION')
        
        # Get the fixation duration (a random int from 1 to 5)
        fixation_for_trial = fixations[run_number-1][tidx]
        
        timer.reset()
        #Change to the next slide:
        # - "rating" for "RATING_DUR" (1-5s)
        while timer.getTime() < fixation_for_trial:
        #for frame in range(FIXATION_DUR):
            fixation.draw()
            win.flip()
    # End of all trials

    # Logging: Send END log event
    logging.log(level=logging.DATA, msg='******* END run %i *******' % run_number)


    # Save the trial infomation from trial handler
    log_filename2 = "%s_%i.csv" % (log_filename[:-4], run_number)
    trials.saveAsText(log_filename2, delim=',', dataOut=('n', 'all_raw')) #####FAIL with "-1"
    # Press 'space' to and the run (will move on to the next run if there is one)
    event.waitKeys(keyList=('space'))

# =====================
# MAIN
#
# - set up stimuli and runs
#sys.exit()
#################### MAIN ####################

for idx, run in enumerate(runs): # 2 runs in total
    
    #print(run)
    #note the the input 'run' has already been raddomized, so it is okay to use 'sequential' here
    trials = data.TrialHandler(run, nReps=1, extraInfo=run_data, 
    dataTypes=['stim_onset', 'resp_onset', 'rt', 'resp'],
    method='sequential') 

    nextrun = idx+1
    #print(trials)
    
    do_run(nextrun, trials)
    
    #print("stopping program here at: " + str(random.randint(0,100)))
    #sys.exit()
    
win.close()
core.quit()
#sys.exit()

#trials.__dict__.keys()

#dict_keys(['name', 'autoLog', 'trialList', 'nReps', 'nTotal', 'nRemaining', 'method', 'thisRepN', 'thisTrialN', 'thisN',
#           'thisIndex', 'thisTrial', 'finished', 'extraInfo', 'seed', 'data', 'sequenceIndices', 'originPath', 'origin', '_exp'])