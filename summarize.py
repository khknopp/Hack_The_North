import cohere
co = cohere.Client('...')
# import transcription from transcription.py
# import 

text=(
 "so why is every mapping Quebec different well basically it boils down to the fact that Quebec believes it should own this huge piece of Territory called Labrador yes like The Lovable dog and this isn't exactly a small piece of land either at 294 000 kilometers squared this territory is larger than all of the states in the United States except three and you could even fit Belgium the Netherlands Luxembourg and even Montenegro all in this region and still have a little bit of room left over Quebec believes it has historic rights to this region and that the border between the two provinces doesn't make sense at 3 500 kilometers long its longest interproventional border in the country and the only land Border in Canada that is disputed between two provinces now this dispute has been going on for a while and can basically be traced all the way back to when the British first conquered New France way back in 1763. shortly after New France was taken over by the British Empire the colony in Newfoundland got to extend its jurisdiction to the coasts of Labrador officially this was done to administer fishing rights which if you've ever been to this part of Canada you'll know fishing's a massive deal here after a decade and a fair bit of squabbling the British decided to create the Quebec Act in 1774. this act was designed to improve relations with the francophone inhabitants in Quebec Canada and redrew the borders of the colony to include taking back the coast of Labrador from Newfoundland yet while officially this was now Quebec territory again Newfoundland got to continuing controlling serious fishing even though it wasn't technically their land this confusing overlap of authority created a fair bit of tension between the two colonies and Newfoundland especially wasn't happy about this Lobby to get the full coast of Labrador back again eventually after a few years of complaining London gave in to newfoundland's demands and re-re-extended its jurisdiction to the coastal area Labrador in 1809 stretching from radiales and Jean all the way to the Hudson Straits in the art a few years later the British Empire changed the borders again in 1825 with the British North America seniorial rights act that set the border between Quebec and Newfoundland as a straight line at blocks Avon to the 52nd parallel but the Inland border remained kind of fuzzy the dispute got a bit more complicated after Quebec joined with Ontario Nova Scotia and New Brunswick to form the Dominion of Canada and Quebec's territory was substantially expanded eventually annexing almost all of the labrador Peninsula by 1912. for their part Newfoundland interpreted that their control over the coast extended pretty deep into the interior to the height of land which essentially meant the top of the Laurentian mountain range where water flows either west of the Hudson Bay or east of the Atlantic Ocean along with the associated drainage basins Canada claimed that Quebec should have all of Mainland Labrador Newfoundland was only supposed to have the coast Canada said was a strip of land one mile wide away from the sea and you can see this on historic maps from that era the dispute became more serious In 1902 when Newfoundland issued a login license in the Churchill River Region the spark debate of over exactly who could issue the license and of course receive the revenues from the sale of Timber to settle the competing claims Canada and Newfoundland took the issue to the London privy Council Judicial Court to settle on the care a panel of five judges was created to answer the question on what the word Coast meant officially the panel couldn't create new boundary do any land swaps or suggest territory or compromises they just had to set the boundary at what previous laws interpreted it as before the court made its final opinion though Newfoundland actually offered to settle the dispute out of court by selling all of its Inland Labrador claims to get back for the small price of 30 million dollars which is about the equivalent of 450 million dollars in 2022 considering there's over a hundred billion dollars worth of Timber and valuable Metals in this region that probably would have been a pretty good deal for Quebec Newfoundland for its parts a little value in the territory aside from the fishing rights on the coast and hope this would help pay down its extremely high debt but Quebec turned this down because they believe the court would come out in its favor unfortunately forgive back the ruling went in newfoundland's favor with the privy Council going newfoundland's height of land argument up until Brew Lake where Then followed along the 52nd parallel East block sebon which is what the Border has remained at to this day for the rest of Canada after winning the case Newfoundland then repeated its offer this time to the federal government of Canada but they increased the price up to 110 million dollars which is about the equivalent of 1.9 billion in 2022 which is still honestly a pretty good deal but this was rejected by Canada which believed Newfoundland would end up joining Confederation eventually making the purchase kind of pointless when Newfoundland did end up joining Confederation in 1949 its boundary in Labrador was confirmed in the terms of Union despite some protests from Quebec so all done and dusted right well no Quebec continues to believe there was a conflict of interest in this case and the judges at the time would be inclined to favor the english-dominated island over the only francophone majority province in Canada on top of this Quebec believes the court went above its mandate by giving Newfoundland land Beyond The Watershed which Newfoundland didn't even ask for this territory is the focal point to the modern dispute by Quebec which has de facto recognized the rest of the border and is why every map in Quebec has this piece of dirty apart at Quebec instead of the straight line you see on most Maps outside the province altogether this area has slightly smaller than Belgium but unlike Belgium with its 11.6 million people this region has zero inhabitants funnily enough because of the competing claims this piece of territory is technically part of both the provincial writings of du plessis in Quebec and Lake Melvin Newfoundland So in theory at least if you move here you would be the best represented person in Canada and could be elected in both province's assemblies at the exact same time because Quebec has never officially recognized the Court's decision it has required that all government maps in Quebec put that piece of territory as part of Quebec while the rest of the Border has to have the world in 1927 do considered definitive in two spots along with a couple other interesting guidelines like the territory Labrador must appear but not be expressly identified and the Border symbol used for the border between Labrador and Quebec should be different from other inter-provincial or International boundaries in the 1960s Quebec proposed to trade a better deal for hydroelectricity in exchange for some of its claims in Labrador and this proposal really ticked off a lot of newfoundlanders who believe the dispute was settled this was the controversial hydroelectric deal to develop the Churchill Falls region which Islanders viewed as unfair contributed to a lot of animosity between the residents and governments of the two provinces which continues to this day in 2001 when Newfoundland sought to amend the 1982 Constitution by changing its official name to Newfoundland and Labrador to make mainlanders feel more included in the province to Quebec provincial ministers issued a joint statement which reminded the federal government that no Quebec government has recognized the boundary between Newfoundland and Quebec in the name changes only symbolic showing that the dispute really hasn't gone away over the last nearly 100 years not much has changed in this dispute the Border still has yet to be officially demarcated and every once in a while the issue boils back to the surface for some reason or the other for example the leaders spoke at a conference not long ago where the map of Quebec included all of Labrador and this stirred some concerns from labradorian as you know the mha for lab West what would be your message to the block on this issue fixture map what do you think of this poor dispute who do you think the territory really should belong to let me know in the comments below and if you liked the video please be sure to like it and consider subscribing it's free and you can always change your mind thanks for watching"
)

# summarize text
transcriptionSummary = co.summarize(
  text=text,
  format="bullets",
  extractiveness="auto",
  additional_command="Create a summary of the text's key takeaways and provide supporting evidence. Ensure that student at this lecture could easily understand it",
)
print(str(transcriptionSummary.summary).split('\n')) # get each bullet point as a string in a string array



#### Find which sentences in the summary are related to the missing section