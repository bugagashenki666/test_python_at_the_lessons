import re

regex = r"(.*)(gg)(.*)|(.*)"

test_str = ("Once upon a time there were three little pigs\n"
            "Who went out into the big world\n"
            "To build their homes and seek their fortunes\n\n"
            "The first little piggy, his house is made of wood\n"
            "He lives in a chicken turkey piggy neighborhood\n"
            "He likes to fuck his sister and drink his moonshine\n"
            "A typical redneck filthy fuckin' swine!\n"
            "I rode into town with my axe in my holsta\n"
            "Everybody knows about the wicked piggy roasta\n"
            "The sheriff at the border, he tried to take me out\n"
            "I drew my axe with the quickness-and cut his Adam's Apple out!\n"
            "Walked in the village and to the piggy's place\n"
            "He opened up his door and shot me in the face\n"
            "And blew me off the porch-and blew my head in half\n"
            "But I'm a Juggalo so it only made me laugh (ha ha!)\n"
            "Axe in hand, I rose like the dead\n"
            "And swung with all my might- made a thump noise in his head\n"
            "Since we out west, I grabbed a shotgun\n"
            "And blew his fuckin tongue out the back of his cranium!!\n\n"
            "CHORUS:\n"
            "Three little piggies, to make a piggy pie\n"
            "There's nothing like the sound when you hear a piggy die\n"
            "I might choose a gun (NO!)\n"
            "I might choose an axe (YES!)\n"
            "The Carnival's in town- come and get your piggy snacks\n\n"
            "The second little piggy, his house is made of brick\n"
            "And this little piggy is a mother fucking dick\n"
            "He lays down his rules and reads you your rights\n"
            "In that funny lookin car with the little blinking lights\n"
            "I drive a Volkswagon bug 17 deep\n"
            "Packed full of Juggalos, lights out and we creep\n"
            "To the piggy station and lay on the horn\n"
            "First piggy out- we blow his lungs out his uniform\n"
            "Now they in persuit like Starsky and Hutch\n"
            "But theres only two of them-the rest are out to lunch\n"
            "They call up Dunkin Donuts to gather up the rest\n"
            "25 piggies with they bullet-proof vests\n"
            "We lead them in a chase, they bustin' off rounds\n"
            "But now they all fucked cuz we at the Carney grounds\n"
            "And they gettin swallowed by their very own greed\n"
            "DARK CARNIVAL and wicked clowns because we need....\n\n"
            "CHORUS 2xs\n"
            "Three little piggies to make a piggy pie\n"
            "There's nothin like the sound when you hear a piggy die\n"
            "I might choose a gun (NO!)\n"
            "I might choose an axe (YES!)\n"
            "The carnival's in town come and get your piggy snacks\n\n"
            "The last little piggy, his house is made of gold\n"
            "He lives in a mansion on his own private road\n"
            "I started walking down it- the guard he told me wait\n"
            "I snapped his fuckin neck in two and slammed his nuts in the gate\n"
            "Cuz this little piggy must definitely die!\n"
            "I'm lop his nugget off and toss it in the sky\n"
            "And then I watch the moon take the form of the devil\n"
            "And pull it out the sky and beat it with a shovel\n"
            "People in my city, they fightin' for they meals\n"
            "He sleeps on a mattress stuffed with hundered dollar bills\n"
            "A richey is the devil- he never will admit it\n"
            "So I'mma cut his hand off and slap his face wit' it\n"
            "Opened up his door, he sleeping in his bed\n"
            "I grabbed a brick of gold and smacked it upside his head\n"
            "He begged for his life, I told him its too late\n"
            "And tied his neck in a knot and watch him suffocate\n"
            "Cuz I need...\n\n"
            "CHORUS 4x\n"
            "Three little piggies to make a piggy pie\n"
            "There's nothin like the sound when you hear a piggy die\n"
            "I might choose a gun (NO!)\n"
            "I might choose an axe (YES!)\n"
            "The carnival's in town come and get your piggy snacks")

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):

    print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
                                                                        end=match.end(), match=match.group()))

    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1

        print("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum, start=match.start(groupNum),
                                                                        end=match.end(groupNum),
                                                                        group=match.group(groupNum)))
