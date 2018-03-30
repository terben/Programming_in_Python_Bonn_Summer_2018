# Necessary knowledge on the Linux command-line

Our course requires some basic knowledge on using a *Unix*-system via the command-line (terminal). In the following you find some test questions representing the level of knowledge you should have. I do not ask you to actually do them or to hand them in but you should be able to solve them if somebody asked you to. You will need to do similar tasks regularly during our course work. Each task is followed by the topic(s) it is testing so that you can look it up if you want to.

## Book recommendations

If you would like to fresh up your knowledge on the *Unix/Linux* command-line, you could have a look at the following two books. They bascically are a German and English version of the same topics:

- [Einführung in Unix/Linux für Naturwissenschaftler](http://www.springer.com/de/book/9783662503003). The essential chapters are: 3, 4, 5, 7, 9, 10. The book is available in the physics-library and at AIfA.

- [Unix and Perl to the Rescue](http://www.cambridge.org/de/academic/subjects/life-sciences/genomics-bioinformatics-and-systems-biology/unix-and-perl-rescue-field-guide-life-sciences-and-other-data-rich-pursuits?format=PB&isbn=9780521169820#D6pdUYVvJ6vm0bQ6.97). The needed material is *Part 3 (Essential Unix)*. I do not know about the availability of this book in our libraries.

## Test questions

1. Open a *Linux*-terminal. In which directory are you when you open a new terminal? With which *Unix*-command do you find out the directory you are currently in? *(Unix-shell and terminal)*

2. How do you find out which *shell* you are working with?

2. Launch your favourite text-editor and create a file ```me.txt``` containing your name. Can you launch the editor in a way so that you can continue to use your shell while the editor is running? *(usage of text-editors, foreground and background jobs)*

3. Make a new subdirectory ```test1``` in your home directory *(Unix file-system commands)*

4. Copy the file ```me.txt``` into the subdirectory as ```me_copy.txt``` *(file copy-command)*

5. Use the ```cd```-command to move between your home-directory and the subdiretory *(Unix file-system commands)*

6. Rename the copy ```me_copy.txt``` to ```me_renames.txt``` **while being in your home-directory** *(absolute and relative paths)*

7. Using ```echo``` and a redirection of the standard output, add your date of birth the the copy *(redirection of ```STDOUT``` to a file)*

8. Use the ```diff```-command to compare the two files ```me.txt``` and ```me_copy.txt```. If you did not yet use the ```diff```-command, then look it up at the internet. Understanding its output is very useful in many circumstances!

9. Delete the subdirectory ```test1``` and the copy of ```me.txt``` in it. Can you do this with a single command? *(Unix file-system commands)*

10. Put two copies of ```me.txt``` (choose your own file names) into a new subdirectory ```test2```. Use the ```tar```-command to backup that directory to ```test2.tar.gz``` *(```tar```-command and archive-files)*

11. Use ```tar``` to restore the contents of ```test2.tar.gz``` into a sub-directory ```test3``` *(```tar```-command)*

12. Type ```sleep 2000 &```. Use the ```ps```-command to identify the ```sleep```-process. Use the ```kill```-command to get rid of it *(process control under Unix)*
