# Description of database rows

|name|Function|
|:----:|:----:|
|Name|str: Name or alias of such ANIME/MOVIE; Should be input as natural language|
|StartDate|str: The start airing date of such ANIME/MOVIE; Should be input as DD/MM/YYYY format|
|Time|str: The start time of such MOVIE; Should be input as HH:MM format|
|Cinema|str: The cinema to watch such MOVIE|
|UpdateWeekDay|int: The update week day of such ANIME; Should be input as integer, e.g. 0=Sunday, 1=Monday etc.|
|UpdateTime|str: The update time of such ANIME; Should be input as HH:MM format|
|EpisodeNumber|int: The total episode number of such ANIME; Should be input as integer, e.g. 12=12 episodes|
|ViewStatus|str: The view status of such ANIME/MOVIE; Only following status should exist: "Not Start", "Watching", "Abandon", "Finish"|
|Special|str: Special broadcasting arrangement of such ANIME; Format: TBD|
|ViewPlatform|str: ViewPlatform of such ANIME; Should be input as natural language|
|Ratings|int: Ratings of such ANIME/MOVIE; Should be input as integer e.g. 1=Lowest rating, 5=Highest rating|
|Notes|str: Reminder or review of such ANIME/MOVIE; Should be input as natural language|
