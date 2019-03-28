#######################################

#

# MESSAGE TASK for SES Persuasion Study

#

#


# Timings:

#

#   Message   5 secq

#   Relevance rating  2 secq

#   Fixation  1.5 sec (need to take this out --> with 5 dispersed rest fixations of 12 secs)

#

#

# trials    72 (18 Future/Gain + 18 Future/Loss + 18 Present/Gain + 18 Present/Loss)







# Import modules



import csv #imports excel .csv files



from psychopy import visual, core, event, gui, data, sound, logging # imports libraries from psycho py

import datetime

import random
import sys



# parameters

useFullScreen = False



frame_rate = 1

message_dur = 5 * frame_rate # message time

rating_dur = 2 * frame_rate # question time

fixation_dur = 1.5 # fixation cross time  -- THIS DURATION NEEDS TO BE RANDOM

# (no rest being used) rest_dur = 12 * frame_rate

disdaq_dur = 8 * frame_rate # need to figure out what this is defining

button_labels = { '1': 0, '2': 1, '3': 2, '4': 3 }

#button_labels = { '1': 0, '2': 1, '3': 2, '4': 3 }

buttons = button_labels.keys()



instruct_dur = 8 * frame_rate





# get subjID

subjDlg = gui.Dlg(title="HMS Messages Task")

subjDlg.addField('Enter Subject ID:')

subjDlg.show()



if gui.OK:

    subj_id=subjDlg.data[0]

else:

    sys.exit()


# great at least we can get it not to crash. now we can figure out why it's crashing by printing out logs along the way
# i have to go soon, but you can try to add print lines and exit at points further down the script and see how far we get before it crashes, that will tell us what's wrong
# i will do a few


log_filename = 'logs/%s.csv' % subj_id



run_data = {

    'Participant ID': subj_id,

    'Date': str(datetime.datetime.now()),

    'Description': 'HMS Message Task'

}







# Set up window

win=visual.Window([1024,768], fullscr=useFullScreen, monitor='testMonitor', units='deg')



# Define Stimulus



ready_screen = visual.TextStim(win, text="Ready.....", height=1.5, color="#FFFFFF")

fixation = visual.TextStim(win,text='+', height=5, color="#FFFFFF") # Cross Fixation



# message screen

#

#             IMAGE

#

#            message (no message needed, we are using pictures with messages)



pictureStim = visual.ImageStim(win, pos=(0,6.5), size=(18,10) )

# messageStim = visual.TextStim(win, text='', pos=(0,0), color="#FFFFFF", wrapWidth=20)



#  response screen

#

#           IMAGE (don't need)

#

#        message (don't need)

#

#       rating scale



#     1       2       3       4

#   not                       effective

#  effective



rate1 = visual.TextStim(win,text='1', color="#FFFFFF", pos=(-8,-4))

rate2 = visual.TextStim(win,text='2', color="#FFFFFF", pos=(-3,-4))

rate3 = visual.TextStim(win,text='3', color="#FFFFFF", pos=(3,-4))

rate4 = visual.TextStim(win,text='4', color="#FFFFFF", pos=(8,-4))

ratingStim = [rate1, rate2, rate3, rate4]



anchor1 = visual.TextStim(win, text='Not\neffective', color="#FFFFFF", pos=(-8,-6))

anchor4 = visual.TextStim(win, text='Effective', color="#FFFFFF", pos=(8,-6))







# instrcution screen

#instruction_image = visual.SimpleImageStim(win,image="buttonpad.png",pos=(-1,-3.5))

instruction_text = visual.TextStim(win, height=1.3,color="#FFFFFF",

        text="Please view each message carefully. \n\nThen use the keypad to indicate how effective you thought the message was. ",

        pos=(0,+5))



# sound test stimuli (don't need sound for this task)

test_instructions = visual.TextStim(win, text='', pos=(0,4), height=1.2, wrapWidth=20)

#test_message = visual.TextStim(win, text='Please listen to the message', pos=(0,2), height=1.2, color='#FFFFFF')

lower = visual.TextStim(win, text='Button 1 = Reduce volume', pos=(0,1))

higher = visual.TextStim(win, text='Button 2 = Increase volume', pos=(0,-1))

ok = visual.TextStim(win, text='Button 4 = Volume is good', pos=(0,-3))


stimuli = [i for i in csv.DictReader(open('stimuli.csv','rU'))]


# set up trial handler

#runs = []
runs = [ [], [] ]

# half the stimuli are in the first run and half are in the second run
for i in range(len(stimuli)):#

        # append a record to the first run
     runs[0].append(stimuli[i])#

    #else:
    #    # append stimuli to the second run
    #    runs[1].append(stimuli[i])


fixations = [[], []]


durs = [fixation_dur, fixation_dur, fixation_dur]


for j in range(len(stimuli)):

    fixations[0].append(random.randint(1,5))



print(fixations)


################

# setup logging #

log_file = logging.LogFile("logs/%s.log" % (subj_id),  level=logging.DATA, filemode="w")


globalClock = core.Clock()

logging.setDefaultClock(globalClock)


def do_sound_test():

    timer = core.Clock()

    test_message_text = '''blah'''



def do_run(run_number, trials):


    timer = core.Clock()

    ##############################


    # 1. display ready screen and wait for 'T' to be sent to indicate scanner trigger


    ready_screen.draw()

    win.flip()

    event.waitKeys(keyList='t')


    # reset globalClock

    globalClock.reset()



    # send START log event

    logging.log(level=logging.DATA, msg='******* START (trigger from scanner) - run %i *******' % run_number)



    ################

    # SHOW INSTRUCTIONS

    ################


    timer.reset()

    while timer.getTime() < instruct_dur:

        instruction_text.draw()

        win.flip()


    timer.reset()


    while timer.getTime() < fixation_dur:

            fixation.draw()

            win.flip()


    ################

    # MAIN LOOP

    # present trials

    for tidx, trial in enumerate(trials):

        trial_type = trial['type']

        theme = trial['theme']

        cond = trial['cond']

        image = "images/%s/%s_%s.png" % (cond, theme, trial_type)

        pictureStim.setImage(image)


        # send MESSAGE log event

        logging.log(level=logging.DATA, msg="MESSAGE: %s - %s - %s" % (cond, theme, trial_type))


        trials.addData('stim_onset', globalClock.getTime())


        timer.reset()

        while timer.getTime() < message_dur:

            pictureStim.draw()

            win.flip()


        # send SHOW RATING log event

        logging.log(level=logging.DATA, msg="SHOW RATING")


        trials.addData('resp_onset', globalClock.getTime())


        # clear event buffer

        event.clearEvents()

        resp_onset = globalClock.getTime()

        # show rating and collect response

        timer.reset()

        while timer.getTime() < rating_dur:

            pictureStim.draw()

            for rate_stim in ratingStim:

                rate_stim.draw()


            anchor1.draw()

            anchor4.draw()

            win.flip()

            # get key response

            resp = event.getKeys(keyList = buttons)


            if len(resp) > 0 :

                resp_value = resp[0]

                ratingStim[button_labels[resp_value]].setColor('red')


                # add response value to the trial handler logging

                trials.addData('resp',resp_value)

                trials.addData('rt', globalClock.getTime() - resp_onset)


        # reset rating number color

        for rate in ratingStim:

            rate.setColor('#FFFFFF')


        # ------------ FIXATION ------------

        # send FIXATION log event

        logging.log(level=logging.DATA, msg='FIXATION')

        # show fixation

        timer.reset()

        fixation_for_trial = fixations[run_number-1][tidx]

        while timer.getTime() < fixation_for_trial:

        #for frame in range(fixation_dur):

            fixation.draw()

            win.flip()

    # send END log event

    logging.log(level=logging.DATA, msg='******* END run %i *******' % run_number)

    # save the trial infomation from trial handler

    log_filename2 = "%s_%i.csv" % (log_filename[:-4], run_number )

    trials.saveAsText(log_filename2, delim=',', dataOut=('n', 'all_raw'))

    event.waitKeys(keyList=('space'))


# =====================

# MAIN

#

# - set up stimuli and runs
#sys.exit()

for idx, run in enumerate(runs):
    
    #print(run)
    
    trials = data.TrialHandler(run, nReps=1, extraInfo=run_data, dataTypes=['stim_onset', 'resp_onset', 'rt', 'resp'], method="random")
    
    nextrun = idx+1
    #print(trials)
    
    do_run(nextrun, trials)
    
    #print("stopping program here at: " + str(random.randint(0,100)))
    #sys.exit()
    
#sys.exit()
    
