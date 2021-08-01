These scripts are for an HDA tool that i made for the riggers to record their screen, show off their work and uppload it onto ftrack,

and 1 way for them to do this was to use recordmydesktop, which is a library for linux, and to record your screen you would have to open up bash and type a really long command
that consists of the recordmydesktop name, the resolutoin and the full path , this was just too much effort to record your screen, so thats when i decided to make a quick
HDA tool that gets the correct paths (based on our environment variables already setup for certain projects ) allows you to quickly change the naming, add new directorys
to the output path, check the file size and ofcours start and stop the recording, this was supposed to be a quick and dirty tool to make, but i ended up running into some
issues, the main issue i ran into was trying to run a script on the same process as houdini ( any scipt that takes long to compute ) would freeze the entire houdini until the
the compute is complete, in this case, its a screen recorder,so it doesnt stop computting until you tell it to, so i had to find a way around this, iv read about multi threading 
and subprocess but for the life of me i couldnt get it to work the way i wanted to and at this point i was spending too much time on this mini project, so i ended up 
writing an external .py file which gets created instantly as the record button is pushed, the external file gets launched by another linux command 
and the screen recorder records as a seperate process in the backround, what a relief, to finally get this right, but now i ran into another problem, i couldmt find a way to
stop this recoding, which was a child process of the main process in linux, i spent an entire day trying to figure out how to send a signal to this specific child process
luckily our IT guy at BlackGinger helped me out with a usefull command to interupt that child process, so with that command i managed to build it into the stop button - and now
we have a neat little screen recorder =)

i also added a readme section, so artist can know what is required to use the tool and i added a feedback area for artist to send any bug reports, ideas or sugestions
this all writes out to an external file where all my tools write out to so i can readup on what people say





https://user-images.githubusercontent.com/80905013/127786299-a3bd03ea-aad6-4b91-8d26-08fc159af46a.mp4




