import operator
from nltk.corpus import stopwords
speech_text='''
Chief Justice Roberts, President Carter, President Clinton, President Bush, President Obama, fellow Americans and people of the world, thank you.
We, the citizens of America, are now joined in a great national effort to rebuild our country and restore its promise for all of our people. Together we will determine the course of America and the world for many, many years to come.
We will face challenges. We will confront hardships. But we will get the job done. Every four years, we gather on these steps to carry out the orderly and peaceful transfer of power.
And we are grateful to President Obama and First Lady Michelle Obama for their gracious aid throughout this transition. They have been magnificent. Thank you.
Today's ceremony, however, has very special meaning. Because today, we are not merely transferring power from one administration to another or from one party to another.
But we are transferring power from Washington D.C. and giving it back to you, the people.
For too long, a small group in our nation's capital has reaped the rewards of government while the people have borne the cost. Washington flourished, but the people did not share in its wealth. Politicians prospered, but the jobs left. And the factories closed.
The establishment protected itself but not the citizens of our country. Their victories have not been your victories. Their triumphs have not been your triumphs. And while they celebrated in our nation’s capital, there was little to celebrate for struggling families all across our land. That all changes starting right here and right now. Because this moment is your moment. It belongs to you.
It belongs to everyone gathered here today and everyone watching all across America. This is your day. This is your celebration. And this, the United States of America, is your country.
What truly matters is not which party controls our government but whether our government is controlled by the people. January 20th, 2017 will be remembered as the day the people became the rulers of this nation again.
The forgotten men and women of our country will be forgotten no longer.
Everyone is listening to you now. You came by the tens of millions to become part of a historic movement, the likes of which the world has never seen before.
At the center of this movement is a crucial conviction -- that a nation exist to serve its citizens. Americans want great schools for their children, safe neighborhoods for their families and good jobs for themselves.
These are just and reasonable demands of righteous people and a righteous public. But for too many of our citizens, a different reality exist. Mothers and children trapped in poverty in our inner cities, rusted out factories scattered like tombstones across the landscape of our nation, an education system flushed with cash but which leaves our young and beautiful students deprived of all knowledge. And the crime, and the gangs, and the drugs that have stolen too many lives and robbed our country of so much unrealized potential. This American carnage stops right here and stops right now.
We are one nation, and their pain is our pain. Their dreams are our dreams, and their success will be our success. We share one heart, one home and one glorious destiny.
The oath of office I take today is an oath of allegiance to all Americans. For many decades, we've enriched foreign industry at the expense of American industry, subsidized the armies of other countries while allowing for the very sad depletion of our military.
We defended other nation’s borders while refusing to defend our own.
And spent trillions and trillions of dollars overseas while America's infrastructure has fallen into disrepair and decay.
We've made other countries rich while the wealth, strength, and confidence of our country has dissipated over the horizon. One by one, the factories shuttered and left our shores with not even a thought about the millions and millions of American workers that were left behind.
The wealth of our middle class has been ripped from their homes and then redistributed all across the world.
But that is the past and now we are looking only to the future.
We assembled here today are issuing a new decree to be heard in every city, in every foreign capital and in every hall of power. From this day forward, a new vision will govern our land. From this day forward, it's going to be only America first -- America first.
Every decision on trade, on taxes, on immigration, on foreign affairs will be made to benefit American workers and American families. We must protect our borders from the ravages of other countries making our products, stealing our companies and destroying our jobs.
Protection will lead to great prosperity and strength. I will fight for you with every breath in my body. And I will never, ever let you down.
America will start winning again, winning like never before.
We will bring back our jobs. We will bring back our borders. We will bring back our wealth, and we will bring back our dreams. We will build new roads and highways and bridges and airports and tunnels and railways all across our wonderful nation. We will get our people off of welfare and back to work rebuilding our country with American hands and American labor. We will follow two simple rules -- buy American and hire American.
We will seek friendship and goodwill with the nations of the world.
But we do so with the understanding that it is the right of all nations to put their own interests first. We do not seek to impose our way of life on anyone but rather to let it shine as an example. We will shine for everyone to follow.
We will reinforce old alliances and form new ones. And unite the civilized world against radical Islamic terrorism, which we will eradicate completely from the face of the earth.
At the bedrock of our politics will be a total allegiance to the United States of America and through our loyalty to our country, we will rediscover our loyalty to each other. When you open your heart to patriotism, there is no room for prejudice.
The Bible tells us how good and pleasant it is when God's people live together in unity. We must speak our minds openly, debate our disagreement honestly but always pursue solidarity. When America is united, America is totally unstoppable.
There should be no fear. We are protected, and we will always be protected. And most importantly, We will be protected by the great men and women of our military and law enforcement. We will be protected by God.
Finally, we must think big and dream even bigger. In America, we understand that a nation is only living as long as it is striving. We will no longer accept politicians who are all talk and no action, constantly complaining but never doing anything about it.
The time for empty talk is over. Now arrives the hour of action.
Do not allow anyone to tell you that it cannot be done. No challenge can match the heart and fight and spirit of America. We will not fail. Our country will thrive and prosper again. We stand at the birth of a new millennium, ready to unlock the mysteries of space, to free the earth from the miseries of disease and to harness the energies, industries and technologies of tomorrow. A new national pride will stir ourselves, lift our sights and heal our divisions. It’s time to remember that old wisdom our soldiers will never forget -- that whether we are black or brown or white, we all bleed the same red blood of patriots.
We all enjoyed the same glorious freedoms, and we all salute the same great American flag.
And whether a child is born in the urban sprawl of Detroit or the windswept plains of Nebraska, They look up at the same night sky, they build a heart with the same dreams and they are infused with the breath of life by the same Almighty Creator.
So to all Americans in every city near and far, small and large, from mountain to mountain, from ocean to ocean, hear these words -- you will never be ignored again.
Your voice, your hopes and your dreams will define our American destiny. Together, And your courage and goodness and love will forever guide us along the way. We will make America strong again. We will make America wealthy again. We will make America proud again. We will make America safe again. And yes, together, thank you. we will make America great again. God bless you. And God bless America. Thank You.
'''

# Version 1
speech_text = speech_text.lower()
speech_text = speech_text.replace(',',' ')
speech_text = speech_text.replace('.',' ')
speech_text = speech_text.replace('\"',' ')
speech_text = speech_text.replace('\n',' ')
speech_text = speech_text.replace('  ',' ')
speech = speech_text.split(' ')
while '' in speech:
    speech.remove('')
print(speech)

word_count = {}
for word in speech:
    if word not in word_count:
        word_count[word] = 1
    else:
        word_count[word] = word_count[word] + 1
stop_words = stopwords.words('english')

sorted_words = sorted(word_count.items(), key=lambda d:d[1], reverse=True)

words_result =  []
for k,v in sorted_words:
    if k not in stop_words:
        words_result.append((k,v))

print(words_result)

# Version 2

from collections import Counter
c = Counter(speech)
for sw in stop_words:
    del c[sw]

print(c.most_common(10))